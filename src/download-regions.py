#! /usr/bin/env python

import os
import requests
import shutil

os.makedirs("regions", exist_ok=True)

if not os.path.isfile("regions/infuse_rgn_2011.zip"):
    with open("regions/infuse_rgn_2011.zip", "wb") as file:
        url = "https://borders.ukdataservice.ac.uk/ukborders/easy_download/prebuilt/shape/infuse_rgn_2011.zip"
        data = requests.get(url)
        data = data.content
        file.write(data)

if not os.path.isfile("regions/infuse_rgn_2011.shp"):
    shutil.unpack_archive(
        "regions/infuse_rgn_2011.zip", "regions"
    )

if not os.path.isfile("regions/Scotland_ol_2001.zip"):
    with open("regions/Scotland_ol_2001.zip", "wb") as file:
        url = "https://borders.ukdataservice.ac.uk/ukborders/easy_download/prebuilt/shape/Scotland_ol_2001.zip"
        data = requests.get(url)
        data = data.content
        file.write(data)

if not os.path.isfile("regions/Scotland_ol_2001.shp"):
    shutil.unpack_archive(
        "regions/Scotland_ol_2001.zip", "regions"
    )

if not os.path.isfile("regions/Wales_ol_2011.zip"):
    with open("regions/Wales_ol_2011.zip", "wb") as file:
        url = "https://borders.ukdataservice.ac.uk/ukborders/easy_download/prebuilt/shape/Wales_ol_2011.zip"
        data = requests.get(url)
        data = data.content
        file.write(data)

if not os.path.isfile("regions/Wales_ol_2011.shp"):
    shutil.unpack_archive(
        "regions/Wales_ol_2011.zip", "regions"
    )
