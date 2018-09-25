# Le but est d’afficher dans une QMessageBox toutes les données attributaires d’une commune identifiée même si la couche « commune » n’est pas la couche active. Un clic droit permet de désactiver l’outil.

#-*-coding: utf-8 -*-
from qgis.core import *
from qgis.gui import *
from qgis.utils import iface

from PyQt4.QtCore import *
from PyQt4.QtGui import *

class OutilIdentificationPerso(QgsMapToolIdentify):
    def __init__(self, interface):
        QgsMapToolIdentify.__init__(self, interface.mapCanvas())
        self.interface = interface
        self.maCarte = interface.mapCanvas()

        leRegistre = QgsMapLayerRegistry.instance()
        listeCouche = leRegistre.mapLayersByName("commune")
        self.coucheCommune = None
        if len(listeCouche) > 0:
            self.coucheCommune = listeCouche[0]

    def canvasPressEvent(self, e):
        if e.button() == Qt.RightButton:
            self.maCarte.unsetMapTool(self)
            self.maCarte.setMapTool(None)

    def canvasReleaseEvent(self, e):
        if self.coucheCommune:
            communesIdentifiees = self.identify(e.x(), e.y(), [self.coucheCommune], QgsMapToolIdentify.TopDownStopAtFirst)
            if len(communesIdentifiees) > 0:
                uneCommune = communesIdentifiees[0].mFeature
                print(uneCommune.attributes())
                print(uneCommune.fields())
                print(uneCommune.fields()[0].name())
                msg = []
                for i in range(len(uneCommune.attributes())):
                    msg.append(uneCommune.fields()[i].name() + " : " + str(uneCommune.attributes()[i]))
                    QMessageBox.information(self.interface.mainWindow(), "Informations sur la commune", "\n".join(msg))

monOutilIdentificationPerso = OutilIdentificationPerso(iface)
iface.mapCanvas().setMapTool(monOutilIdentificationPerso)