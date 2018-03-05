#-*-coding: utf-8 -*-
import time

from qgis.utils import iface
from PyQt4.QtCore import *
from PyQt4.QtGui import *

progressMessageBar = iface.messageBar().createMessage("Traitement en cours...")
progress = QProgressBar()

progress.setMaximum(10)
progress.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
progressMessageBar.layout().addWidget(progress)
iface.messageBar().pushWidget(progressMessageBar, iface.messageBar().INFO)
for i in range(10):
    time.sleep(1)
    progress.setValue(i + 1)
iface.messageBar().clearWidgets()