# Récupération des coordonnées (SCR de la carte) d’un point cliqué

#-*-coding: utf-8 -*-
from qgis.core import *
from qgis.gui import *
from qgis.utils import iface

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class OutilEmitPointPerso(QgsMapToolEmitPoint):
    def __init__(self, interface):
        QgsMapToolEmitPoint.__init__(self, interface.mapCanvas())
        self.maCarte = interface.mapCanvas()

    def canvasPressEvent(self, e):
        if e.button() == Qt.RightButton:
            self.maCarte.unsetMapTool(self)
            self.maCarte.setMapTool(None)
        else:
            print(u"Coordonnees du point : ", e.mapPoint())

monOutilEmitPointPerso = OutilEmitPointPerso(iface)
iface.mapCanvas().setMapTool(monOutilEmitPointPerso)