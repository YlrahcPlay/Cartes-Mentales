# L’instance est créée avec QgsRasterLayer() en spécifiant :
# - l’identifiant de la source de données : pour un raster, il s’agit toujours du chemin vers le fichier
# - un nom pour la couche

#-*-coding: utf-8 -*-
from qgis.core import QgsMapLayerRegistry, QgsRasterLayer
from qgis.utils import iface
from PyQt4.QtGui import QMessageBox

leRegistre = QgsMapLayerRegistry.instance()

raster = QgsRasterLayer("E:/.../ex.img", "Nom")

if raster.isValid():
     leRegistre.addMapLayer(raster)
else:
     QMessageBox.warning(iface.mainWindow(), "Erreur", u"La couche %s n'a pas pu être chargée !" % ("Nom"))