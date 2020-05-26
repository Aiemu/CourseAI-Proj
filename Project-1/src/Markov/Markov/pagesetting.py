# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pagesetting.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!

import random
import math

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidget, QMessageBox, QAbstractItemView, QTableWidgetItem
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt


class Ui_pageSetting(object):
    def setupUi(self, pageSetting):
        pageSetting.setObjectName("pageSetting")
        pageSetting.setWindowModality(QtCore.Qt.ApplicationModal)
        pageSetting.resize(240, 320)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(pageSetting.sizePolicy().hasHeightForWidth())
        pageSetting.setSizePolicy(sizePolicy)
        pageSetting.setMinimumSize(QtCore.QSize(240, 320))
        pageSetting.setMaximumSize(QtCore.QSize(240, 320))
        pageSetting.setLayoutDirection(QtCore.Qt.LeftToRight)
        pageSetting.setAutoFillBackground(True)
        self.horizontalLayout = QtWidgets.QHBoxLayout(pageSetting)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtWidgets.QLabel(pageSetting)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_3 = QtWidgets.QLabel(pageSetting)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.edit_x = QtWidgets.QLineEdit(pageSetting)
        self.edit_x.setText("")
        self.edit_x.setObjectName("edit_x")
        self.horizontalLayout_6.addWidget(self.edit_x)
        self.edit_y = QtWidgets.QLineEdit(pageSetting)
        self.edit_y.setObjectName("edit_y")
        self.horizontalLayout_6.addWidget(self.edit_y)
        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 4)
        self.horizontalLayout_6.setStretch(2, 4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(pageSetting)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.edit_trap = QtWidgets.QLineEdit(pageSetting)
        self.edit_trap.setObjectName("edit_trap")
        self.horizontalLayout_3.addWidget(self.edit_trap)
        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 8)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_2 = QtWidgets.QLabel(pageSetting)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.edit_barrier = QtWidgets.QLineEdit(pageSetting)
        self.edit_barrier.setObjectName("edit_barrier")
        self.horizontalLayout_5.addWidget(self.edit_barrier)
        self.horizontalLayout_5.setStretch(0, 2)
        self.horizontalLayout_5.setStretch(1, 8)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_5 = QtWidgets.QLabel(pageSetting)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        self.edit_s = QtWidgets.QLineEdit(pageSetting)
        self.edit_s.setObjectName("edit_s")
        self.horizontalLayout_7.addWidget(self.edit_s)
        self.label_6 = QtWidgets.QLabel(pageSetting)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6)
        self.edit_e = QtWidgets.QLineEdit(pageSetting)
        self.edit_e.setObjectName("edit_e")
        self.horizontalLayout_7.addWidget(self.edit_e)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_random = QtWidgets.QPushButton(pageSetting)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.btn_random.setFont(font)
        self.btn_random.setObjectName("btn_random")
        self.horizontalLayout_2.addWidget(self.btn_random)
        self.btn_generate = QtWidgets.QPushButton(pageSetting)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        self.btn_generate.setFont(font)
        self.btn_generate.setObjectName("btn_generate")
        self.horizontalLayout_2.addWidget(self.btn_generate)
        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout.setStretch(0, 4)
        self.verticalLayout.setStretch(1, 2)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(3, 2)
        self.verticalLayout.setStretch(4, 2)
        self.verticalLayout.setStretch(5, 2)
        self.verticalLayout.setStretch(7, 2)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(pageSetting)
        self.btn_random.clicked.connect(self.randomParams)
        QtCore.QMetaObject.connectSlotsByName(pageSetting)

    def retranslateUi(self, pageSetting):
        _translate = QtCore.QCoreApplication.translate
        pageSetting.setWindowTitle(_translate("pageSetting", "Setting"))
        self.label_4.setText(_translate("pageSetting", "Map Setting"))
        self.label_3.setText(_translate("pageSetting", "Size"))
        self.edit_x.setPlaceholderText(_translate("pageSetting", "x"))
        self.edit_y.setPlaceholderText(_translate("pageSetting", "y"))
        self.label.setText(_translate("pageSetting", "Traps"))
        self.edit_trap.setPlaceholderText(_translate("pageSetting", "(a,b) (c,d),..."))
        self.label_2.setText(_translate("pageSetting", "Barriers"))
        self.edit_barrier.setPlaceholderText(_translate("pageSetting", "(e,f) (g,h),..."))
        self.label_5.setText(_translate("pageSetting", "Start"))
        self.edit_s.setPlaceholderText(_translate("pageSetting", "(sx,sy)"))
        self.label_6.setText(_translate("pageSetting", "End"))
        self.edit_e.setPlaceholderText(_translate("pageSetting", "(ex,ey)"))
        self.btn_random.setText(_translate("pageSetting", "Random"))
        self.btn_generate.setText(_translate("pageSetting", "Generate"))

    def randomParams(self):
        x = random.randint(3, 20)
        y = random.randint(3, 20)

        self.edit_x.setText(str(x))
        self.edit_y.setText(str(y))

        if math.floor(x * y / 8) > 0:
            numTraps = random.randint(1, math.floor(x * y / 8))
            numBarriers = random.randint(1, math.floor(x * y / 7))
        else:
            numTraps = 0
            numBarriers = 0

        strTraps = ''
        for i in range(0, numTraps):
            if i == 0:
                strTraps = '(' + str(random.randint(0, x - 1)) + ',' + str(random.randint(0, y - 1)) + ')'
            else:
                strTraps = strTraps + ' (' + str(random.randint(0, x - 1)) + ',' + str(random.randint(0, y - 1)) + ')'
        self.edit_trap.setText(strTraps)

        strBarriers = ''
        for i in range(0, numTraps):
            if i == 0:
                strBarriers = '(' + str(random.randint(0, x - 1)) + ',' + str(random.randint(0, y - 1)) + ')'
            else:
                strBarriers = strBarriers + ' (' + str(random.randint(0, x - 1)) + ',' + str(random.randint(0,  y - 1)) + ')'
        self.edit_barrier.setText(strBarriers)

        strS = '(' + str(random.randint(0, x - 1)) + ',' + str(random.randint(0, y - 1)) + ')'
        self.edit_s.setText(strS)

        strE = '(' + str(random.randint(0, x - 1)) + ',' + str(random.randint(0, y - 1)) + ')'
        while (strE == strS):
            strE = '(' + str(random.randint(0, x - 1)) + ',' + str(random.randint(0, y - 1)) + ')'
        self.edit_e.setText(strE)

        QApplication.processEvents()