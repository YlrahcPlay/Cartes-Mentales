# Le but est d’afficher dans la console les coordonnées de la carte du point cliqué et décliqué, de désactiver l’outil lorsqu’un clic droit est émis et dans ce cas, afficher le nombre de clics effectués.

#-*-coding: utf-8 -*-
from qgis.core import *
from qgis.gui import *
from qgis.utils import iface

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class OutilZoomPerso(QgsMapToolZoom):
    def __init__(self, iface, ancienOutilCarto, estZoomMoins):
        QgsMapToolZoom.__init__(self, iface.mapCanvas(), estZoomMoins)

        self.interface = iface
        self.maCarte = iface.mapCanvas()
        self.ancienOutilCarto = ancienOutilCarto
        self.nombreClic = 0
        self.deactivated.connect(self.desactivation)

    def canvasPressEvent(self, e):
        QgsMapToolZoom.canvasPressEvent(self, e)

        if e.button() == Qt.RightButton:
            iface.mapCanvas().setMapTool(self.ancienOutilCarto)
        else:
            self.nombreClic += 1
            print(u"Coordonnees de debut de zoom", e.mapPoint())

    def canvasReleaseEvent(self, e):
        QgsMapToolZoom.canvasReleaseEvent(self, e)

        print(u"Coordonnees de fin de zoom", e.mapPoint())

    def desactivation(self):
        QMessageBox.warning(self.interface.mainWindow(), u"Désactivation de l'outil de zoom", u"Vous avez cliqué %i fois ..." % (self.nombreClic))

ancienOutilCarto = iface.mapCanvas().mapTool()
monOutilZoomPerso = OutilZoomPerso(iface, ancienOutilCarto, False) # False = zoom Plus
iface.mapCanvas().setMapTool(monOutilZoomPerso)