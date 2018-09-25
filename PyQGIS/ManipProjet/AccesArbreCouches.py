#-*-coding: utf-8 -*-
from qgis.core import QgsProject

leProjet = QgsProject.instance()

root = leProjet.layerTreeRoot()