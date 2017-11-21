# -*- coding: utf-8 -*-
"""
/***************************************************************************
 FeatureTemplatesDockWidget
                                 A QGIS plugin
 test
                             -------------------
        begin                : 2017-11-17
        git sha              : $Format:%H$
        copyright            : (C) 2017 by fake
        email                : fake
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""

import os

from PyQt4 import QtGui, uic
from PyQt4.QtCore import pyqtSignal

FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'feature_template_dockwidget_base.ui'))
items = {
    "water pipe - 100mm":
        {
            "type": "water pipe",
            "size": 100
        },
    "sewer pipe - 200mm":
        {
            "type": "sewer pipe",
            "size": 200
        }
}

class FeatureTemplatesDockWidget(QtGui.QDockWidget, FORM_CLASS):

    templateApplied = pyqtSignal(str, dict)
    closingPlugin = pyqtSignal()


    def __init__(self, parent=None):
        """Constructor."""
        super(FeatureTemplatesDockWidget, self).__init__(parent)
        # Set up the user interface from Designer.
        # After setupUI you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        self.applyButton.pressed.connect(self.apply_template)

    def closeEvent(self, event):
        self.closingPlugin.emit()
        event.accept()

    def load_items(self):
        self.templatesList.clear()
        for key in items:
            self.templatesList.addItem(key)	
    def apply_template(self):
        # Don't do anything if there is no selection text
        if not self.templatesList.currentItem():
            return

        name = self.templatesList.currentItem().text()
        # Get the fields from the items list
        fields = items[name]
        self.templateApplied.emit(name, fields)
