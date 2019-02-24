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

![Map of mean house price by local authority July 2016. Greater height indicates greater mean price (£). This map was converted to 3D using the qgis2threejs plugin](images/house-price-stl.png)

Area is important because it affects multiple aspects of our lives.
For example, baby boys born in the UK in 2012-2014 can expect to live to 79.5 years on average, but boys born in the richest part of the country can expect to live nearly a decade longer than boys born in the poorest part of the country (ONS, <https://goo.gl/s4E8Pm>).

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

So that we can get started promptly on the day, before the course date it would help if you could download and install the software and some of the data we will be using.

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

Be sure to download a version 3.x of QGIS.
Versions beginning 2.x (currently 2.18) are being discontinued, so it is worth starting with the current version.
I strongly recommend you download the long--term release version (currently 3.4).

You can download LibreOffice from:

```
https://www.libreoffice.org/download/download/
```

Either version is fine, but if you are in any doubt choose the lower version number, currently 6.1.5.

Don't worry if you don't manage to install these; I can help you on the day if necessary.

<!--TODO Add link to data download zip-->


# Software

## QGIS

To produce our maps we will use QGIS, a mature, open-source GIS used extensively in academia, public organisations, and private companies.
QGIS is open source software and is free to download and use for any purpose.

I **strongly** recommend you download verion 3.x of QGIS; not version 2.x as this is being deprecated.
I also recommend you use the current long--term release (LTR), which is currently 3.4.

To open QGIS:

- On Windows press the Windows key and start typing QGIS.
- On Mac you can press Cmd + space, then start typing QGIS.
- On Linux your desktop manager will have a run shortcut (on Ubuntu it's the Super key).

If you have a choice of packages choose QGIS Desktop.
The default interface looks like Figure \ref{qgis-interface}.

![The QGIS interface\label{qgis-interface}](images/qgis-interface.png)

The default configuration options for QGIS are quite sensible and do not need much tweaking.
I would suggest the following two changes.

### Rendering with multiple cores

QGIS should already have rendering with multiple cores enabled.
The change I suggest is specifying the maximum number of cores to the number of cores available minus 1.
This can prevent your system from temporarily locking up by always ensuring at least one core is available for tasks other than rendering.
To do this open `Settings` > `Options` menu, and click the `Rendering` tab.

![Rending options in QGIS](images/qgis-rendering-options.png)

Tick `Max cores to use` and enter a number.
If you do not know how many cores your computer has QGIS is pretty good at detecting this, so click up until you can no longer increase the number of cores, then simply drop one.
If in doubt, most consumer computers have four, so specify three and press `Ok`.

### Default CRS

If most of your mapping will be of the UK (England, Scotland, Wales, and Northern Ireland) it may make sense to change the default coordinate reference system (CRS).
Most sources of UK spatial data, such as Ordnance Survey or UK Data Service, use the British National Grid CRS (nothing to do with electricity) so it may be worth specifying this as the default.
Don't worry too much what this is at this stage; I will explain this in a later section.

Change the default CRS by opening the `Settings` > `Options` menu if it's not still open, and click the `CRS` tab.

![QGIS CRS options](images/qgis-crs-options.png)

By `Default CRS for new projects` click `Select CRS` (the little globe to the right).
Then type `27700` (the code for British National Grid) and select it and press ok.

![QGIS CRS Selector](images/qgis-crs-selector.png)

You can always change the CRS for other projects if necessary.
Of course, if most of your mapping will be for a country or region other than the UK a different default CRS might make more sense!

## Spreadsheet

If you are using Microsoft Excel I will assume you are relatively familiar with it.
However, we are only using the spreadsheet programme to store and retrieve data; we are not using any advanced functionality.
The steps I demonstrate in LibreOffice Calc are therefore very similar to the steps in Microsoft Excel.

LibreOffice is a free and open source suite of office applications similar in function to Microsoft Office.
LibreOffice Calc is the spreadsheet programme.

If you are using Calc it's interface looks like Figure \ref{calc-interface}.

![The LibreOffice Calc interface\label{calc-interface}](images/calc-interface.png)


## Open source

Both these packages (QGIS and LibreOffice) are free software.
This means they are free to download and use for any purpose, and also that their source code is free to obtain.

This does not mean that they are inferior to their licensed counterparts (and in some ways could be considered superior).
They are both robust, professionally--written software.
It just means that instead of charging the end user a license fee their development is paid for by individuals and organisations from all over the world through sponsorship and donations.

Much of the backbone of the internet is underpinned by open source software contributed to by well--known companies like Google and Microsoft, so don't worry that 'free' means unsatisfactory.


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
England has nine regions, while Scotland and Wales are each considered a region, making 11 in total.
We will use the `Easy Download` service to download the regions of England, Scotland, and Wales individually, and we will combine these in QGIS.

Download and unzip the following files if you have not already downloaded the data archive:

```
https://borders.ukdataservice.ac.uk/ukborders/easy_download/prebuilt/shape/England_gor_2011.zip
https://borders.ukdataservice.ac.uk/ukborders/easy_download/prebuilt/shape/Scotland_ol_1991.zip
https://borders.ukdataservice.ac.uk/ukborders/easy_download/prebuilt/shape/Wales_ol_2011.zip
```

I suggest you create a project folder to store these files in.
I have called mine `regions`.


## Clipped and generalised polygons

At this point it is worth making a small aside to discuss simplified polygons.
For this example I have specified exactly which file to download, but when obtaining spatial data it is common for services to offer clipped and/or generalised polygons.
These typically are simplified and as such are a smaller file size than the unmodified files.
However, from experience these often have 'slivers' or gaps between the polygons so the resulting polygons may not be valid which can be problematic for analysis.

<!--TODO image of sliver -->

I therefore recommend downloading the original or unmodified shapefiles.
Bandwidth and disk space are cheap; your time spent correcting topology errors is not!
If you later decide you need to simplify the polygons, for example for serving on a website for users to interact with or simply to make plotting faster, it is quite straightforward to do this and you get more dependable results.

There are many tools that are 'topologically--aware' that do not create slivers.
In QGIS if you need to perform a topologically--aware simplification, use `v.generalize` in the GRASS Toolbox (under `Processing` > `Toolbox`).
See Figure \ref{qgis-grass-v-generalize} for where to find this tool.

![v.generalize GRASS tool\label{qgis-grass-v-generalize}](images/qgis-grass-v-generalize.png)

If you need to install GRASS you can obtain this from:

```
https://grass.osgeo.org/download/
```

(If you're using Linux you can use your package manager to install `qgis-plugin-grass`, for example on an Ubuntu system run `sudo apt install qgis-plugin-grass`).


## Projections and Coordinate Reference Systems

To produce a map you must specify (or use the default) coordinate reference system (CRS).
A coordinate reference system specifies:

- how coordinates are assigned to points on the Earth, and
- the origin and scale of the coordinate system.

A projection describes how the three--dimensional surface of the Earth is distorted to fit a two--dimensional map, either on the screen or in print.
You can explore the size of the distortions of the Mercator projection using <https://thetruesize.com>.

Fundamentally the CRS and projection specifies what the coordinates 'mean' so the they can be plotted correctly, and as a result the two terms are often used interchangeably.

The CRS and projection are often specified in the same step and in practice you will typically download a spatial data file and specify the correct CRS for that data.
Often the data you download will have a CRS/projection bundled with it and when you load the file the correct CRS will be applied.
For example, the English regions zip file contained a `.prj` file which QGIS uses to apply the correct CRS to the file as it is loaded.
You can open these `.prj` files with any text editor and the contents looks something like this:

```
PROJCS["OSGB_1936_British_National_Grid",GEOGCS["GCS_OSGB 1936",DATUM["D_OSGB_1936",SPHEROID["Airy_1830",6377563.396,299.3249646]],PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]],PROJECTION["Transverse_Mercator"],PARAMETER["latitude_of_origin",49],PARAMETER["central_meridian",-2],PARAMETER["scale_factor",0.9996012717],PARAMETER["false_easting",400000],PARAMETER["false_northing",-100000],UNIT["Meter",1]]
```

This `.prj` specifies the British National Grid.
It uses the OSGB 1936 coordinate system, the Airy 1830 spheroid (the Earth is not a perfect sphere), and the unit is metre (i.e. each unit increase in coordinate is equivalent to one metre).

Don't worry too much about these; in practice most spatial data now specifies a CRS so this is automatic.
You only need to know about these if:

- the spatial data does not bundle a CRS and you need to specify it manually, or
- you have data sets in different CRSs and you need to *transform* one or more data sets to be consistent.

If you are using UK data from sources such as the OS the CRS is almost certainly the British National Grid (27700).

The CRS is specified using a unique code called an EPSG code.
A full list of all EPSG codes can be obtained from:

```
http://spatialreference.org/ref/epsg/
```

The EPSG codes for the two most common CRSs you will use (at least in the UK) are:

- British National Grid `27700`
- Mercator WGS84 (most common for web maps such as Google Maps) `4326`


## Opening spatial data in QGIS

From the QGIS window (Figure \ref{qgis-interface}) use the browser in the left sidebar to navigate to your project folder.
In this folder select the file(s) that you want to open (you can hold Ctrl/Cmd and click to select multiple files) then press `Add selected layers`, or drag these into the `Layers` panel.

Select the following files and add them as layers:

- `england_gor_2011.shp`
- `scotland_ol_1991.shp`
- `wales_ol_2011.shp`

Your map should look something like this:

![Great Britain regions](images/gb-regions.png)

Congratulations!
You've just produced your first map!


## Other spatial data types

So far we have used file formats called shapefiles to plot our maps.
These are probably the most common file format for storing boundary data, but they are not the only file format.
You might see other file formats including:

- GeoJSON - JSON (Javascript Object Notation) is a common format for transmitting data across the web. GeoJSON simply extends this with geograhical boundary information.
- KML is an XML--based file format originally developed for use with Google Earth.
- GPX, commonly used for sharing GPS routes.

XML (i.e. KML) is a more verbose file format than (Geo)JSON, so I recommend you download GeoJSON when given a choice.
Open these in QGIS in exactly the same way as we opened the shapefile earlier, or simply drag and drop the layer in to QGIS from your file browser.

In addition to file formats you may also see OGC data services and database formats listed, such as:

- WMS
- WCS
- WFS
- PostGIS

Instead of downloading a file to your system locally, these formats work by connecting to the database from from within QGIS and using QGIS as a browser to obtain the boundary extent you require.
Performing these steps is beyond the scope of this one--day course, but it is quite straightforward.
If you wish to explore this the following link to the QGIS documentation will get you started (documentation for version 3.x of QGIS is still a work--in--progress so this page is written for version 2.18 of QGIS which is now out of date, but the steps are largely the same):

```
https://docs.qgis.org/2.18/en/docs/user_manual/working_with_ogc/ogc_client_support.html
```

<!--
TODO
Editing shapefiles: select by attribute; clipping; manual
-->

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

### EPSG codes

```
http://spatialreference.org/ref/epsg/
```

### Projections

```
https://thetruesize.com
```
