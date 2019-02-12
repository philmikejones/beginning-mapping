---
title: Beginning mapping
author: Dr. Phil Mike Jones
date: "2019"
titlepage: true
toc: true
toc-own-page: true
logo: images/uk-orthographic-projection.png
logo-width: 500
---

# Introduction

Welcome to beginning mapping and spatial analysis for social researchers course.
This one--day course is being run on behalf of the Social Research Association.

<!--TODO contribution to CPD? -->


## About your instructor

My name is Phil, and I am your instructor on this course.

I have a PhD in geography from the University of Sheffield.
I specialise in computer simulations of small--area geographical data, but undertake all types of GIS and geographical analysis.

I now work at the University of Derby on an ESRC--funded research project.
For over ten years I have worked in both private and public--sector organisations as a data analyst.

I write blog posts and post tutorials about GIS on my website, which is <https://philmikejones.me>.
I enjoy teaching and have taught variations of much of this material to postgraduate level.

I hope you enjoy your course and come away with the skills and confidence to produce your own maps for spatial analysis; the world needs more geographers!


## Course aims

By the end of this course you will be able to:

- Obtain spatial data (e.g. shapefiles, GeoJSON).
- Obtain suitable thematic data, including:
  - points (e.g. business locations)
  - aggregate (e.g. population data)
- Spatially 'join' the data.
- Understand which projection and coordinate reference systems (CRS) to use.
- Produce a thematic map using appropriate software.
- Export your thematic map.
- Analyse and interpret it and explain the relationships between areas and themes.


## Before the course starts

So that we can get started promptly on the day, before the course date it would help if you could download and install the software we will be using.

You will need two pieces of software on the day.
One is QGIS, which is the GIS software that we will use to produce our maps.
The second is a spreadsheet programme to edit numerical data.
Both can be downloaded free of charge and can be used for any purpose.

You may already have Microsoft Excel installed on your computer.
If you do not you can download LibreOffice and use the Calc programme.
Either Excel or Calc will be more than adequate for our needs on the course.

You can download QGIS from:

```
https://qgis.org/en/site/forusers/download.html
```

Be sure to download a version 3.x (currently version 3.4) of QGIS.
Versions beginning 2.x (currently 2.18) are being discontinued, so it is worth starting with the current version.

You can download LibreOffice from:

```
https://www.libreoffice.org/download/download/
```

Either version is fine, but if you are in any doubt choose the lower version number, currently 6.1.5.

Don't worry if you don't manage to install these; I can help you on the day if necessary.


# Software

## QGIS

To produce our maps we will use QGIS, a mature, open-source GIS used extensively in academia, public organisations, and private companies.
QGIS is open source software and is free to download and use for any purpose.

I **strongly** recommend you download verion 3.x (currently 3.4) of QGIS; not version 2.x as this is being deprecated.

To open QGIS:

- On Windows press the Windows key and start typing QGIS.
- On Mac you can press Cmd + space, then start typing QGIS.
- On Linux your desktop manager will have a run shortcut (on Ubuntu it's the Super key).

If you have a choice of versions choose QGIS Desktop.
The default interface looks like Figure \ref{qgis-interface}.

![The QGIS interface\label{qgis-interface}](images/qgis-interface.png)


## Spreadsheet

If you are using Microsoft Excel I will assume you are relatively familiar with it.
However, we are only using the spreadsheet programme to store and retrieve data; we are not using any advanced functionality.
The steps I demonstrate in LibreOffice Calc are therefore very similar to the steps in Microsoft Excel.

LibreOffice is a free and open source suite of office applications similar in function to Microsoft Office.
LibreOffice Calc is the spreadsheet programme.

If you are using Calc it's interface looks like Figure \ref{calc-interface}.

![The LibreOffice Calc interface\label{calc-interface}](images/calc-interface.png)


# Obtaining spatial data

To plot a map we must first obtain some spatial data that describes the polygons and geometry of the map.
There are a number of sources of spatial data.
You can see the full list in the [References][] section.

For these exercises we will download our boundary data from:

```
https://census.ukdataservice.ac.uk/get-data/boundary-data.aspx
```

This service offers a comprehensive range of high quality shapefiles covering a range of administrative geographies for all of the UK.



## Projections and Coordinate Reference Systems


# Obtain thematic data

## Points

## Aggregate


# Join spatial and thematic data

# Plot the map

# Export the map

# Analyse spatial data

# Where to get help

### GIS StackExchange

```
https://gis.stackexchange.com/
```


# Acknowledgements

This document contains maps produced using boundary data used under the terms of the Open Government License.

**Contains National Statistics data © Crown copyright and database right [2019]
    Contains OS data © Crown copyright [and database right] (2019)**


# References


## Spatial data

### UK

```
https://census.ukdataservice.ac.uk/get-data/boundary-data.aspx
http://geoportal.statistics.gov.uk/
https://www.ordnancesurvey.co.uk/business-and-government/products/finder.html?Licensed%20for=OpenData%20(Free)
http://casweb.ukdataservice.ac.uk/
```

### World

StatSilk (https://www.statsilk.com/maps/download-free-shapefile-maps) also maintain a list of up--to--date sources of shapefiles.

```
https://data.humdata.org/search?ext_geodata=1
http://download.geofabrik.de/
http://www.diva-gis.org/Data
https://gadm.org/data.html
https://www.naturalearthdata.com/downloads/
```

### Programming and interactive

```
https://developers.google.com/maps/documentation/
https://wiki.openstreetmap.org/wiki/Overpass_API
```
