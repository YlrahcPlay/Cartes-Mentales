#-*-coding: utf-8 -*-
from qgis.gui import QgsMessageBar
from qgis.utils import iface

from PyQt4.QtGui import *

def showError():
    pass

elementBarreMessage = iface.messageBar().createMessage("Couche absente", "Explications")
unBouton = QPushButton(elementBarreMessage)
unBouton.setText("Explications")
unBouton.pressed.connect(showError)
elementBarreMessage.layout().addWidget(unBouton)
iface.messageBar().pushWidget(elementBarreMessage, QgsMessageBar.WARNING)