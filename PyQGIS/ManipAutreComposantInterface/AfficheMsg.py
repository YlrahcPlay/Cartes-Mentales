#-*-coding: utf-8 -*-
from qgis.gui import QgsMessageBar
from qgis.utils import iface

iface.messageBar().pushMessage(u"Erreur", u"Désolé, mais cette action n'est pas possible ...", level=QgsMessageBar.CRITICAL)
# iface.messageBar().pushMessage(u"Erreur", u"Désolé, mais cette action n'est pas possible ...", level=QgsMessageBar.INFO)
# iface.messageBar().pushMessage(u"Erreur", u"Désolé, mais cette action n'est pas possible ...", level=QgsMessageBar.WARNING)
# iface.messageBar().pushMessage(u"Géotraitment", u"L'opération s'est correctement déroulé...", level=QgsMessageBar.SUCCESS)