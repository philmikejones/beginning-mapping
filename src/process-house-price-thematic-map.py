#!/usr/bin/env python3

import os
import shutil
import pandas as pd
import geopandas

os.makedirs("data/external", exist_ok=True)

if not os.path.isfile("data/external/Average-prices-2016-07.csv"):
    file = "http://publicdata.landregistry.gov.uk/market-trend-data/house-price-index-data/Average-prices-2016-07.csv"
    file = pd.read_csv(file)
    file.to_csv("data/external/Average-prices-2016-07.csv")
    print("Saved Average-prices-2016-07.csv")

try:
    shutil.unpack_archive(
        "data/external/infuse_dist_lyr_2011.zip",
        "data/external"
    )
except TypeError():
    "Problem unzipping local authorities"

house_prices = pd.read_csv("data/external/Average-prices-2016-07.csv")
lad = geopandas.read_file("data/external/infuse_dist_lyr_2011.shp")

house_prices = house_prices[house_prices.Date == "2016-07-01"]
house_prices = house_prices[["Region_Name", "Average_Price"]]

house_prices.Region_Name

house_prices.Region_Name[house_prices.Region_Name == "Na h-Eileanan Siar"] = "Eilean Siar"
house_prices.Region_Name[house_prices.Region_Name == "City of Glasgow"] = "Glasgow"
lad.geo_label[lad.geo_label == "Glasgow City"] = "Glasgow"

lad[pd.isnull(lad.Average_Price)]


lad.head()

joined[pd.isnull(joined.Average_Price)]
