# Le but est d’afficher dans la console les coordonnées de la carte du point cliqué en début de pan et décliqué en fin de pan et de désactiver l’outil lorsqu’un clic droit est émis.

#-*-coding: utf-8 -*-
from qgis.core import *
from qgis.gui import *
from qgis.utils import iface

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class OutilPanPerso(QgsMapToolPan):
    def __init__(self, carte, ancienOutilCarto):
        QgsMapToolPan.__init__(self, iface.mapCanvas())

        self.maCarte = carte
        self.ancienOutilCarto = ancienOutilCarto

    def canvasPressEvent(self, e):
        QgsMapToolPan.canvasPressEvent(self, e)

        if e.button() == Qt.RightButton:
            iface.mapCanvas().setMapTool(self.ancienOutilCarto)
        else:
            print(u"Coordonnees de debut de pan", e.mapPoint())

    def canvasReleaseEvent(self, e):
        QgsMapToolPan.canvasReleaseEvent(self, e)
        print(u"Coordonnees de fin de pan", e.mapPoint())

ancienOutilCarto = iface.mapCanvas().mapTool()
monOutilPanPerso = OutilPanPerso(iface.mapCanvas(), ancienOutilCarto)
iface.mapCanvas().setMapTool(monOutilPanPerso)