# Gestion des événements de zoom.

#-*-coding: utf-8 -*-
from qgis.core import *
from qgis.gui import *
from qgis.utils import iface

nouvelOutilCarto = QgsMapToolZoom(iface.mapCanvas(), False) # False = zoom plus
#nouvelOutilCarto = QgsMapToolZoom(iface.mapCanvas(), True) # True = zoom moins

iface.mapCanvas().setMapTool(nouvelOutilCarto)
print(u"L'outil courant est un ", iface.mapCanvas().mapTool())
# (u"L'outil courant est un ", <qgis._gui.QgsMapToolZoom object at 0x1314BA80>)