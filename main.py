#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from utils import colors


class ColorApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('./ui/mainWindow.ui', self)
        self.onChangedRgb(0)
        self.addListeners()

    def addListeners(self):
        self.uiRedInput.valueChanged.connect(self.onChangedRgb)
        self.uiGreenInput.valueChanged.connect(self.onChangedRgb)
        self.uiBlueInput.valueChanged.connect(self.onChangedRgb)

    def onChangedRgb(self, value):
        self.updateHex()
        self.updateOutput()

    def updateOutput(self):
        pass

    def updateHex(self):
        rgb = (self.uiRedInput.value(), self.uiGreenInput.value(), self.uiBlueInput.value())
        hex = colors.colorRgbToHex(rgb)
        self.uiHexInput.setText(hex)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorApp()
    window.show()
    sys.exit(app.exec_())
