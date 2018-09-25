# Gestion des informations d’une ou de plusieurs couches qui sont disponibles à l’emplacement du point clické.

#-*-coding: utf-8 -*-
from qgis.gui import *
from qgis.utils import iface

outilIdentification = QgsMapToolIdentify(iface.mapCanvas())
outilIdentification.activate()
listeResultat = []

parametrageRendu = iface.mapCanvas().mapSettings()
pointCoordonneesPixels = parametrageRendu.mapToPixel().transform(-1.15687828351, 46.158552887)

listeResultat.append(outilIdentification.identify(pointCoordonneesPixels.x(),
pointCoordonneesPixels.y(), QgsMapToolIdentify.TopDownStopAtFirst, QgsMapToolIdentify.VectorLayer ))

iface.mapCanvas().setMapTool(outilIdentification)
#print(listeResultat)

for i in listeResultat[0]:
    layer = i.mLayer
    feature = i.mFeature
    print(feature.attributes()) # [1456L, u'17300', u'LA ROCHELLE', 74344L, 2L, u'2017-01-02', 1L]

    # layer.select(feature.id()) # permet de sélectionner l'entité


# Les deux premiers paramètres de la méthode identify() correspondent aux coordonnées de la fenêtre carte exprimées en pixels (d’où la nécessité de faire la conversion).
#
# Le troisième paramètre est le mode d’identification ; ses différentes valeurs possibles sont :
#     ActiveLayer : uniquement sur la couche active (couche courante)
#     TopDownStopAtFirst : uniquement sur la première couche rencontrée (on tient compte de l’ordre de la pile des couches)
#     TopDownAll : sur toutes les couches
#     LayerSelection : sur la couche qui fait déjà l’objet d’une sélection
#
# Le quatrième paramètre est le type d’identification ; ses différentes valeurs possibles sont :
#     VectorLayer : uniquement les couches vectorielles
#     RasterLayer : uniquement les couches raster
#     AllLayers : tout type de couche