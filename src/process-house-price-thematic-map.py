#!/usr/bin/env python3

import os
import shutil
import requests
import pandas as pd
import geopandas

os.makedirs("data/external", exist_ok=True)
os.makedirs("data/processed", exist_ok=True)

if not os.path.isfile("data/external/Average-prices-2016-07.csv"):
    file = "http://publicdata.landregistry.gov.uk/market-trend-data/house-price-index-data/Average-prices-2016-07.csv"  # pylint: disable=line-too-long
    file = pd.read_csv(file)
    file.to_csv("data/external/Average-prices-2016-07.csv")

if not os.path.isfile("data/external/infuse_dist_lyr_2011.zip"):
    with open("data/external/infuse_dist_lyr_2011.zip", "wb") as file:
        url = "https://borders.ukdataservice.ac.uk/ukborders/easy_download/prebuilt/shape/infuse_dist_lyr_2011.zip"  # pylint: disable=line-too-long
        data = requests.get(url)
        data = data.content
        file.write(data)

if not os.path.isfile("data/external/infuse_dist_lyr_2011.shp"):
    shutil.unpack_archive(
        "data/external/infuse_dist_lyr_2011.zip", "data/external"
    )

house_prices = pd.read_csv("data/external/Average-prices-2016-07.csv")
house_prices = house_prices[house_prices.Date == "2016-07-01"]
house_prices = house_prices[["Region_Name", "Average_Price"]]

# No geo code in house_prices so need to join on Region_Name
house_prices.loc[
    house_prices.Region_Name == "City of Westminster", "Region_Name"
] = "City of London,Westminster"
house_prices.loc[
    house_prices.Region_Name == "City of London", "Region_Name"
] = "City of London,Westminster"
house_prices.Region_Name = house_prices.Region_Name.str.replace(
    " And ", " and ", case=True, regex=False
)
house_prices.Region_Name = house_prices.Region_Name.str.replace(
    "^City of ", "", regex=True
)
house_prices.loc[
    house_prices.Region_Name == "Na h-Eileanan Siar", "Region_Name"
] = "Eilean Siar"

house_prices = house_prices.groupby("Region_Name")["Average_Price"].mean()
house_prices = pd.DataFrame(house_prices)


lad = geopandas.read_file("data/external/infuse_dist_lyr_2011.shp")
lad = lad[~lad.label.str.contains("^N")]

lad.geo_label = lad.geo_label.str.replace(
    ", County of", "", case=True, regex=False
)
lad.geo_label = lad.geo_label.str.replace(
    ", City of", "", case=True, regex=False
)
lad.geo_label = lad.geo_label.str.replace(
    " City", "", case=True, regex=False
)
lad.geo_label = lad.geo_label.str.replace(
    " & ", " and ", case=True, regex=False
)
lad.geo_label[lad.geo_label == "Cornwall,Isles of Scilly"] = "Cornwall"
lad.geo_label[lad.geo_label == "The Vale of Glamorgan"] = "Vale of Glamorgan"
lad = lad.set_index("geo_label")

house_prices = lad.join(house_prices)
house_prices = house_prices.set_geometry("geometry")

house_prices.to_file("data/processed/house_prices.shp", driver="ESRI Shapefile")
