#!/usr/bin/env python

import os
import pandas as pd

os.makedirs("data/external", exist_ok=True)

if not os.path.isfile("data/external/Average-prices-2016-07.csv"):
    file = "http://publicdata.landregistry.gov.uk/market-trend-data/house-price-index-data/Average-prices-2016-07.csv"
    file = pd.read_csv(file)
    file.to_csv("data/external/Average-prices-2016-07.csv")

hp = pd.read_csv("data/external/Average-prices-2016-07.csv")
hp.head()
