#!/usr/bin/env python3

import os
import shutil
import pandas as pd

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
