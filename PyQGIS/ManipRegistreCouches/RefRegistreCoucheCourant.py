#-*-coding: utf-8 -*-
from qgis.core import QgsMapLayerRegistry

leRegistre = QgsMapLayerRegistry.instance()
# QgsMapLayerRegistry = "singleton"

# count() renvoie le nombre de couches ouvertes (présentes dans le registre)
print(leRegistre.count())