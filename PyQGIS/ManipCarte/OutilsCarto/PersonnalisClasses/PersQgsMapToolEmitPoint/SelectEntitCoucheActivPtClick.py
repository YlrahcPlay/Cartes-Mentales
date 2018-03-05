# Sélection d’entité(s) de la couche active à partir du point cliqué avec possibilité de sélection multiple si les touche SHIFT ou CTRL sont appuyées

#-*-coding: utf-8 -*-
from qgis.core import *
from qgis.gui import *
from qgis.utils import iface

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class OutilEmitPointPerso(QgsMapToolEmitPoint):
    def __init__(self, interface):
        QgsMapToolEmitPoint.__init__(self, interface.mapCanvas())
        self.interface = interface
        self.maCarte = interface.mapCanvas()

    def canvasPressEvent(self, e):
        if e.button() == Qt.RightButton:
            self.maCarte.unsetMapTool(self)
            self.maCarte.setMapTool(None)

    def canvasReleaseEvent(self, e): # e est une instance de QgsMapMouseEvent
        coucheActive = self.interface.activeLayer()
        if coucheActive == None:
            QMessageBox.critical(self.interface.mainWindow(), u"Outil de sélection perso", u"Une couche doit être active !")
        else:
            tolerance = 5 # pixels
            # construction d'un rectangle à partie du point cliqué (coordonnées en pixels) + une tolérance
            point1Pixel = QPoint(e.pixelPoint().x() - tolerance, e.pixelPoint().y() - tolerance)
            point2Pixel = QPoint(e.pixelPoint().x() + tolerance, e.pixelPoint().y() + tolerance)

            # conversion dans le SCR de la carte
            point1Carte = self.maCarte.mapSettings().mapToPixel().toMapCoordinates(point1Pixel)
            point2Carte = self.maCarte.mapSettings().mapToPixel().toMapCoordinates(point2Pixel)
            rectangleRecherche = QgsRectangle(point1Carte, point2Carte)

            # conversion du rectangle dans le SCR de la couche
            rectangleRecherche = self.maCarte.mapSettings().mapToLayerCoordinates(coucheActive, rectangleRecherche)

            if not((e.modifiers() and Qt.ShiftModifier) or (e.modifiers() and Qt.ControlModifier)): # si la touche SHIFT ou CTRL n'est pas appuyée
                coucheActive.removeSelection() # suppression de la sélection courante
                coucheActive.select(rectangleRecherche, True) # True ou False ne change rien : bug ? + deprecated en 2.18

monOutilEmitPointPerso = OutilEmitPointPerso(iface)
iface.mapCanvas().setMapTool(monOutilEmitPointPerso)