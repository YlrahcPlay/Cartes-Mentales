# Modification de la méthode canvasReleaseEvent() de l’exemple précédent

#-*-coding: utf-8 -*-
from qgis.core import *
from qgis.gui import *
from qgis.utils import iface

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class RectangleMapTool(QgsMapToolEmitPoint):
    def __init__(self, canvas):
        self.canvas = canvas
        QgsMapToolEmitPoint.__init__(self, self.canvas)

        self.dessinTemporaire = QgsRubberBand(self.canvas, QGis.Polygon)
        self.dessinTemporaire.setColor(QColor(255,0,0,125)) # rouge et à moitié transparent
        self.dessinTemporaire.setWidth(1)
        self.initialise()

    def initialise(self):
        self.pointDebut = self.pointFin = None
        self.pointEmis = False
        self.dessinTemporaire.reset(QGis.Polygon)

    def canvasPressEvent(self, e):
        if e.button() == Qt.RightButton:
            self.canvas.unsetMapTool(self)
            self.canvas.setMapTool(None)
            self.initialise()
        else:
            self.pointDebut = self.toMapCoordinates(e.pos())
            self.pointFin = self.pointDebut
            self.pointEmis = True
            self.afficheRectangle(self.pointDebut, self.pointFin)

    def canvasReleaseEvent(self, e):
        self.pointEmis = False
        coucheActive = iface.activeLayer()
        if coucheActive == None:
            QMessageBox.critical(iface.mainWindow(), u"Outil de sélection perso", u"Une couche doit être active !")
        else:
            rectangleRecherche = QgsRectangle(self.pointDebut, self.pointFin)
            # conversion du rectangle dans le SCR de la couche
            rectangleRecherche = self.canvas.mapSettings().mapToLayerCoordinates(coucheActive, rectangleRecherche)

            if not ((e.modifiers() and Qt.ShiftModifier) or (e.modifiers() and Qt.ControlModifier)):  # si la touche SHIFT ou CTRL n'est pas appuyée
                coucheActive.removeSelection()  # suppression de la sélection courante
                coucheActive.select(rectangleRecherche, True)  # True ou False ne change rien : bug ? + deprecated en 2.18

    def canvasMoveEvent(self, e):
        if not self.pointEmis:
            return
        self.pointFin = self.toMapCoordinates(e.pos())
        self.afficheRectangle(self.pointDebut, self.pointFin)

    def afficheRectangle(self, pointDebut, pointFin):
        self.dessinTemporaire.reset(QGis.Polygon)
        if pointDebut.x() == pointFin.x() or pointDebut.y() == pointFin.y():
            return
        point1 = QgsPoint(pointDebut.x(), pointDebut.y())
        point2 = QgsPoint(pointDebut.x(), pointFin.y())
        point3 = QgsPoint(pointFin.x(), pointFin.y())
        point4 = QgsPoint(pointFin.x(), pointDebut.y())
        self.dessinTemporaire.addPoint(point1, False)
        self.dessinTemporaire.addPoint(point2, False)
        self.dessinTemporaire.addPoint(point3, False)
        self.dessinTemporaire.addPoint(point4, True)  # true pour mettre à jour la     carte
        self.dessinTemporaire.show()

monOutilEmitPointPerso = RectangleMapTool(iface.mapCanvas())
iface.mapCanvas().setMapTool(monOutilEmitPointPerso)