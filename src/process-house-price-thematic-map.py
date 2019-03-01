#!/usr/bin/env python3

import os
import shutil
import requests
import pandas as pd
import geopandas

os.makedirs("data/external", exist_ok=True)

if not os.path.isfile("data/external/Average-prices-2016-07.csv"):
    file = "http://publicdata.landregistry.gov.uk/market-trend-data/house-price-index-data/Average-prices-2016-07.csv"
    file = pd.read_csv(file)
    file.to_csv("data/external/Average-prices-2016-07.csv")

with open("data/external/infuse_dist_lyr_2011.zip", "wb") as file:
    url = "https://borders.ukdataservice.ac.uk/ukborders/easy_download/prebuilt/shape/infuse_dist_lyr_2011.zip"
    data = requests.get(url)
    data = data.content
    file.write(data)

try:
    shutil.unpack_archive(
        "data/external/infuse_dist_lyr_2011.zip",
        "data/external"
    )
except TypeError():
    "Problem unzipping local authorities"

house_prices = pd.read_csv("data/external/Average-prices-2016-07.csv")

# lad = gpd.read_file("data/external/infuse_dist_lyr_2011.shp")

house_prices = house_prices[house_prices.Date == "2016-07-01"]
house_prices = house_prices[["Region_Name", "Average_Price"]]

house_prices.head()
