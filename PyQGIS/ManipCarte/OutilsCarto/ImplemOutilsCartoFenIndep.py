# Construire une fenêtre contenant un canevas de carte et des outils cartographiques sommaires pour se déplacer dans la carte et zoomer.
# Les actions sont créées pour l’activation de chaque outil :
#     le déplacement est réalisé avec la classe QgsMapToolPan, le zoom avec une paire d’instances de la classe QgsMapToolZoom.
# Les actions sont paramétrées pour pouvoir être cochées et sont assignées ensuite aux outils pour gérer automatiquement l’état activé / désactivé des actions.
# Les outils cartographiques sont activés par la méthode setMapTool().

#-*-coding: utf-8 -*-
from qgis.core import *
from qgis.gui import *
from qgis.utils import iface

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class MaFenetre(QMainWindow):
    def __init__(self, uneCouche):
        QMainWindow.__init__(self)
        self.laCarte = QgsMapCanvas()
        self.laCarte.setCanvasColor(Qt.white)
        self.laCarte.setExtent(uneCouche.extent())
        self.laCarte.setLayerSet([QgsMapCanvasLayer(uneCouche)])
        self.setCentralWidget(self.laCarte)

        actionZoomPlus = QAction(u"Zoom plus", self)
        actionZoomMoins = QAction(u"Zoom moins", self)
        actionDeplacement = QAction(u"Déplacement", self)
        actionZoomPlus.setCheckable(True)
        actionZoomMoins.setCheckable(True)
        actionDeplacement.setCheckable(True)

        self.connect(actionZoomPlus, SIGNAL("triggered()"), self.zoomPlus)
        self.connect(actionZoomMoins, SIGNAL("triggered()"), self.zoomMoins)
        self.connect(actionDeplacement, SIGNAL("triggered()"), self.Deplacement)
        self.toolbar = self.addToolBar("Actions de la carte")
        self.toolbar.addAction(actionZoomPlus)
        self.toolbar.addAction(actionZoomMoins)
        self.toolbar.addAction(actionDeplacement)

        self.toolDeplacement = QgsMapToolPan(self.laCarte)
        self.toolDeplacement.setAction(actionDeplacement)
        self.toolZoomPlus = QgsMapToolZoom(self.laCarte, False)
        self.toolZoomPlus.setAction(actionZoomPlus)
        self.toolZoomMoins = QgsMapToolZoom(self.laCarte, True)
        self.toolZoomMoins.setAction(actionZoomMoins)
        self.Deplacement()

    def zoomPlus(self):
        self.laCarte.setMapTool(self.toolZoomPlus)

    def zoomMoins(self):
        self.laCarte.setMapTool(self.toolZoomMoins)

    def Deplacement(self):
        self.laCarte.setMapTool(self.toolDeplacement)

fenetre = MaFenetre(iface.activeLayer())
fenetre.show()