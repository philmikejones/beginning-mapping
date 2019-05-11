import pandas as pd

pc = pd.read_csv(
    "data/open_postcode_geo.csv", header=None, prefix="c"
)

pc = pc.rename(columns = {
    "c0": "postcode",
    "c3": "easting",
    "c4": "northing",
    "c6": "country"
})

pc = pc[{"postcode", "easting", "northing", "country"}]
pc = pc.query('country == "England"')

gp = pd.read_csv("data/gp-london-postcodes.txt")

pc["london"] = pc.postcode.isin(gp.postcode)
pc = pc[pc.london == True]

pc.to_csv("data/postcode-geocoded.csv")
