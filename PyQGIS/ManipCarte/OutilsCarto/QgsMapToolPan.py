# Gestion du déplacement panoramique de la carte.

#-*-coding: utf-8 -*-
from qgis.core import *
from qgis.gui import *
from qgis.utils import iface

nouvelOutilCarto = QgsMapToolPan(iface.mapCanvas())
iface.mapCanvas().setMapTool(nouvelOutilCarto)
print(u"L'outil courant est un ", iface.mapCanvas().mapTool())
# (u"L'outil courant est un ", <qgis._gui.QgsMapToolPan object at 0x1314B3F0>)