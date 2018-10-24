---
title: Windows installation
weight: 15
chapter: true
---

# Install QGIS on Windows

- Navigate to [QGIS downloads](https://qgis.org/en/site/forusers/download.html)
- Open 'Download for Windows' if it's not already opened
- Choose the appropriate standalone installer (not the OSGeo4W network installer).
    - If your laptop is less than five years old you almost certainly want the 64-bit installer

{{% notice tip %}}
Ordinarily I recommend you download the latest long term release (LTR) version of QGIS, as this is the most stable.
However, QGIS 2 (the current LTR) is being deprecated so I recommend you learn with the latest version 3 (currently 3.2)
{{% /notice %}}

- Install the software as normal by double-clicking on the icon
- You will need to tell User Account Control to allow the software to make changes to your system by clicking yes

![](../../../images/windows-user-account-control.png)

- Click Next
- Agree to the license terms
- Choose your installation location (leave the default if you're not sure)
- You do not need to install any of the example data sets (North Carolina, South Dakota, and Alaska) unless you want to
- Finally Install
- When QGIS has finished installing you will have several new start menu items

{{% notice tip %}}
To load QGIS click 'QGIS Desktop 3.x.y' or 'QGIS Desktop 3.x.y with GRASS 7.b.c'.<br />
GRASS extends QGIS with extra functions; you do not need to load them for basic plotting.
{{% /notice %}}

- If asked to import settings from QGIS 2 select, 'I want a clean start. Don't import my QGIS 2 settings'.
