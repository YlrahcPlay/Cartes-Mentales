#-*-coding: utf-8 -*-
from qgis.core import QgsProject

# recupere instance projet courant
leProjet = QgsProject.instance()
# QgsProject = « Singleton »

# Les méthodes writeEntry() permettent d’écrire la valeur et utilisent trois paramètres :
# - Le nom du domaine (nom libre qui permet de catégoriser la variable)
# - Le nom de la variable
# - La valeur de la variable (de type String, Integer, Float, Boolean ou List)
leProjet.writeEntry("domaine", "variableChaine", "valeur")
leProjet.writeEntry("domaine", "variableEntier", 12)
leProjet.writeEntryDouble("domaine", "variableFlottant", 3.14)
leProjet.writeEntryBool("domaine", "variableBooleen", True)
leProjet.writeEntry("domaine", "variableListe", (["10", "20", "50"]))


# Les méthodes readEntry() permettent de lire la valeur et utilisent trois paramètres (le dernier est optionnel) :
# - Le nom du domaine (nom libre qui permet de catégoriser la variable)
# - Le nom de la variable
# - La valeur de substitution si le nom de variable n’est pas retrouvé
leProjet.readEntry("domaine", "variableChaine", "valeur defaut")[0]
leProjet.readNumEntry("domaine", "variableEntier", 0)[0]
leProjet.readDoubleEntry("domaine", "variableFlottant", 1.31)[0]
leProjet.readBoolEntry("domaine", "variableBooleen", False)[0]
leProjet.readListEntry("domaine", "variableListe", ["500"])[0]

# Les fonctions readEntry() renvoient un tuple composé de la valeur de la variable et d’un booléen (pour l’instant non utilisé : toujours égal à True).