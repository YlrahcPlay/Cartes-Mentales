#-*-coding: utf-8 -*-
from qgis.core import QgsMapLayerRegistry, QgsMapLayer

leRegistre = QgsMapLayerRegistry.instance()

mesCouchesDico = QgsMapLayerRegistry.instance().mapLayers()

for cle, valeur in mesCouchesDico.items():
     print(cle)
     print(valeur)
     print(type(valeur))


for cle, valeur in mesCouchesDico.items():
     if (valeur.type() == QgsMapLayer.VectorLayer):
          print(valeur.name(), " est vectorielle.") # .name() renvoie nom couche
     elif (valeur.type() == QgsMapLayer.RasterLayer):
          print(valeur.name(), " est un raster.")
     else:
          print(valeur.name(), " n'est ni vectorielle, ni raster.")


print(leRegistre.mapLayer(cle)) # Renvoie instance unique de QgsMapLayer

print(leRegistre.mapLayersByName(NomDeLaCouche)) # Renvoie liste d’instances de QgsMapLayer