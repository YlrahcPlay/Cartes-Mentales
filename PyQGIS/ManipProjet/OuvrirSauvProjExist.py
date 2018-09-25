#-*-coding: utf-8 -*-
from qgis.core import QgsProject
from PyQt4.QtCore import QFileInfo

leProjet = QgsProject.instance()

# Ouvrir un projet existant
leProjet.read(QFileInfo("C:/.../projet.qgs"))


# enregistre les modifification du projet sous le même nom.
leProjet.write()

# ou enregistre les modifification du projet sous un nom différent
leProjet.write(QFileInfo("C:/.../projet2.qgs"))