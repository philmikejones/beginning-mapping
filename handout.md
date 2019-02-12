---
title: Beginning mapping
author: Dr. Phil Mike Jones
date: "2019"
top-level-division: chapter
titlepage: true
toc: true
toc-own-page: true
book: true
logo: images/uk-orthographic-projection.png
logo-width: 500
---

# Introduction

Welcome to beginning mapping and spatial analysis for social researchers course.


## About your instructor

My name is Phil and I'm a geographer.
I have a PhD in geography from the University of Sheffield[^thesis], in which I specialised in computer simulations of small--area geographical data.
I now work at the University of Derby on an ESRC--funded research project; I use GIS and geographical methods extensively in my work.
I previously worked in both private and public--sector organisations as a data analyst.

I write blog posts and post tutorials about GIS on my website[^website].
I enjoy teaching and have taught variations of much of this material to postgraduate level.
I hope you enjoy your course and come away with the skills and confidence to produce your own maps for spatial analysis; the world needs more geographers!

[^thesis]: http://etheses.whiterose.ac.uk/19283/
[^website]: My website is https://philmikejones.me


## Course aims

By the end of this course you will be able to:

- Obtain spatial data.
- Obtain suitable thematic data.
- Spatially 'join' the data.
- Produce a thematic map using appropriate software.
- Export your thematic map.
- Analyse and interpret it and explain the relationships between areas and themes.

We will cover:

- Spatial data (e.g. shapefiles, GeoJSON).
- Thematic data (points (e.g. business locations); aggregate (e.g. population)).
- 'Joining' these data.
- Projections and coordinate reference systems (CRS).
- Identifying, understanding, and describing spatial patterns.
- Exporting maps for reports or publications.


## Before the course starts

To produce our maps we will use QGIS, a mature, open-source GIS used extensively in academia, public organisations, and private companies.
QGIS is open source software and is free to download and use for any purpose.

So that we can get started promptly on the day, before the course date it would help if you could download and install version 3 or greater of QGIS[^qgis].

[^qgis]: Download QGIS from https://qgis.org/en/site/forusers/download.html

Don't worry if you don't manage to install QGIS; I can help you on the day.

You will also need a spreadsheet programme to edit numerical data.
If you do not have Microsoft Excel you can use LibreOffice Calc[^libreoffice-calc].
This is free and open source, just like QGIS, and will be more than adequate for working with our numerical data.
Either version of LibreOffice is fine (if in doubt, choose the lower version number, currently 6.1.5).

[^libreoffice-calc]: Download LibreOffice from https://www.libreoffice.org/download/download/

## QGIS

Load QGIS.
On Windows press the Windows key and start typing QGIS.
On Mac you can press Cmd + space, then start typing QGIS.
On Linux your desktop manager will have a run shortcut (on Ubuntu just the Super key).
If you have a choice of versions choose QGIS Desktop.
The default interface looks like Figure \ref{qgis-interface}.

![The QGIS interface\label{qgis-interface}](images/qgis-interface.png)
