#-*-coding: utf-8 -*-
from qgis.core import QgsProject

leProjet = QgsProject.instance()

# fileName() renvoie :
# - chaine vide si aucun projet ouvert
# - chemin complet du fichier projet
print(leProjet.fileName())