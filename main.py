#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget
from utils import colors


class ColorApp(QWidget):
    def __init__(self, app):
        super().__init__()
        self.clipboard = app.clipboard()
        uic.loadUi('./ui/mainWindow.ui', self)
        self.onChange(0)
        self.addListeners()

    def addListeners(self):
        self.uiRedInput.valueChanged.connect(self.onChange)
        self.uiGreenInput.valueChanged.connect(self.onChange)
        self.uiBlueInput.valueChanged.connect(self.onChange)
        self.uiAlphaBox.toggled.connect(self.onChange)
        self.uiAlphaSlider.valueChanged.connect(self.onChange)
        self.uiCopyRgb.clicked.connect(self.rgbWillCopy)
        self.uiCopyHex.clicked.connect(self.hexWillCopy)

    def hexWillCopy(self):
        self.clipboard.setText(self.uiHexInput.text())

    def onChange(self, value):
        self.updateHex()
        self.updateOutput()

    def rgbWillCopy(self):
        self.clipboard.setText(self.uiLabelRgbaResult.text())

    def updateOutput(self):
        output = 'rgb({}, {}, {})'
        if self.uiAlphaBox.isChecked():
            output = 'rgba({}, {}, {}, {:.2})'
        self.uiLabelRgbaResult.setText(
            output.format(
                self.uiRedInput.value(),
                self.uiGreenInput.value(),
                self.uiBlueInput.value(),
                self.uiAlphaSlider.value() * 0.01))

    def updateHex(self):
        rgb = (self.uiRedInput.value(), self.uiGreenInput.value(), self.uiBlueInput.value())
        hex = colors.colorRgbToHex(rgb)
        self.uiHexInput.setText(hex)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ColorApp(app)
    window.show()
    sys.exit(app.exec_())
