#-*-coding: utf-8 -*-
from qgis.gui import QgsMessageBar
from qgis.utils import iface

iface.messageBar().pushMessage(u"Géotraitement", u"L'opération s'est correctement déroulée ...", level=QgsMessageBar.SUCCESS, duration=4) # en secondes