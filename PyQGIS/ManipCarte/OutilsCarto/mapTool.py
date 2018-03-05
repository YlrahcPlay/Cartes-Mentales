#-*-coding: utf-8 -*-
from qgis.utils import iface

# Référencer l’outil actif de la carte (il ne peut y en avoir qu’un)
outilCourant = iface.mapCanvas().mapTool() # renvoie une instance de QgsMapTool

# Changer d’outil courant :
iface.mapCanvas().setMapTool(unAutreOutil) # pour changer d'outil courant