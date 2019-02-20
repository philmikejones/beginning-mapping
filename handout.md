---
title: Beginning mapping and spatial analysis for social researchers
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

Maps are more than just navigational tools.
Almost all aspects of our lives can be mapped and analysed.
Maps of air pollution, cars per household, education, ethnicity, greenspace, religion, disease, life expectancy, even the number and location of take-away outlets can help us gain insight into the spatial nature of our world.

Maps are used to depict variables and information (themes) of relevance to social researchers.
These thematic maps are then used to understand the relationship between area and the theme of interest.

Area is important because it affects multiple aspects of our lives.
For example, baby boys born in the UK in 2012-2014 can expect to live to 79.5 years on average, but boys born in the richest part of the country can expect to live nearly a decade longer than boys born in the poorest part of the country (ONS, https://goo.gl/s4E8Pm).

This course will equip you with the skills you need to produce your own thematic maps, and the knowledge you need to analyse and interpret them.
The majority of the day will be practical.

The course will be of relevance to academics, students, researchers, analysts, policy makers, commissioners, and managers who want to understand the spatial nature of social themes and issues.
You might already have some data that you want to map, and just want to learn to do that, or you might want to complement your existing data and analyses with additional (spatial) evidence.

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

### Bio

Dr Phil Mike Jones is a geographer.
He holds a PhD in human geography from the University of Sheffield. He specialises in spatial analysis and GIS, and has written software for spatial analysis and spatial simulation.
He has extensive experience of social research, especially quantitative methods, in a variety of sectors.
Phil has taught geography, GIS, and quantitative methods to undergraduates, postgraduates, academics, and practitioners, in a variety of settings.
Phil uses open software and data in his teaching where possible to make these skills as accessible as possible.


## Course aims

By the end of this course you will be able to:

- Obtain spatial data (e.g. shapefiles, GeoJSON).
- Obtain suitable thematic data, including:
  - points (e.g. business locations)
  - aggregate (e.g. population data)
- Spatially 'join' the data.
- Understand which projection and coordinate reference systems (CRS) to use.
- Produce a thematic map using appropriate software.
- Export your thematic map for reports and publications.
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

For our first map we will make a simple plot of regions in Great Britain (England, Wales, and Scotland).
England has nine regions, which Scotland and Wales are each considered a region, making 11 in total.
We will use the `Easy Download` service to download the regions of England, Scotland, and Wales individually, and we will combine these in QGIS.
Download the following files:

```
https://borders.ukdataservice.ac.uk/ukborders/easy_download/prebuilt/shape/England_gor_2011.zip
https://borders.ukdataservice.ac.uk/ukborders/easy_download/prebuilt/shape/Scotland_ol_1991.zip
https://borders.ukdataservice.ac.uk/ukborders/easy_download/prebuilt/shape/Wales_ol_2011.zip
```

I suggest you create a project folder to store these files in.
I have called my `regions`.


## Clipped and generalised polygons

Some services offer clipped and/or generalised polygons.
These typically are simplified and as such are a smaller file size than the unmodified files.
However, from experience these often have 'slivers' or gaps between the polygons so the resulting polygons may not be valid which can be problematic for analysis.

<!--TODO image of sliver -->

I therefore strongly recommend downloading the unmodified shapefiles.
Bandwidth and disk space are cheap; your time spent correcting topology errors is not!

If you later decide you need to use the polygons for serving on a website for users to interact with, it makes sense to simplify the polygons at this stage, and there are tools that are 'topologically--aware' that do not create slivers.

If you need to perform a topologically--aware simplification, use `v.generalize` in the GRASS Toolbox (under `Processing` > `Toolbox`).
See Figure \ref{qgis-grass-v-generalize} for where to find this tool.

![v.generalize GRASS tool\label{qgis-grass-v-generalize}](images/qgis-grass-v-generalize.png)


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
