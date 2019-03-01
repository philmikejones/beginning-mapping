#!/usr/bin/env python3

import os
import shutil
import requests
import statistics
import pandas as pd
import geopandas

os.makedirs("data/external", exist_ok=True)

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

try:
    shutil.unpack_archive(
        "data/external/infuse_dist_lyr_2011.zip", "data/external")
except TypeError():
    "Problem unzipping local authorities"

house_prices = pd.read_csv("data/external/Average-prices-2016-07.csv")
house_prices = house_prices[house_prices.Date == "2016-07-01"]
house_prices = house_prices[["Region_Name", "Average_Price"]]

house_prices.Region_Name = house_prices.Region_Name.str.replace(
    " And ", " and ",
    case=True, regex=False
)
house_prices.Region_Name = house_prices.Region_Name.str.replace(
    "^City of ", "", regex=True
)
house_prices[house_prices.Region_Name == "Na h-Eileanan Siar"] = "Eilean Siar"
house_prices[house_prices.Region_Name == "City of Nottingham"] = "Nottingham"

# Using the .loc[row.index, col.index] prevents a copy warning
house_prices.loc[house_prices["Region_Name"] == "City of London", "Average_Price"] = statistics.mean([
    float(house_prices.Average_Price[house_prices.Region_Name == "City of London"]),
    float(house_prices.Average_Price[house_prices.Region_Name == "City of Westminster"])
])
house_prices = house_prices[house_prices.Region_Name != "City of Westminster"]
house_prices = house_prices.Region_Name.str.replace("City of London", "City of London, Westminster")

# No geo code in house_prices so need to join on Region_Name
# This, of course, means we need to match them!

lad = geopandas.read_file("data/external/infuse_dist_lyr_2011.shp")

lad.geo_label = lad.geo_label.str.replace(
    ", County of", "",
    case=True, regex=False
)
lad.geo_label = lad.geo_label.str.replace(
    ", City of", "",
    case=True, regex=False
)
lad.geo_label = lad.geo_label.str.replace(
    " City", "",
    case=True, regex=False
)
lad.geo_label = lad.geo_label.str.replace(
    " & ", " and ",
    case=True, regex=False
)
lad[lad.geo_label == "Cornwall,Isles of Scilly"] = "Cornwall"
lad[lad.geo_label == "The Vale of Glamorgan"] = "Vale of Glamorgan"

house_prices
