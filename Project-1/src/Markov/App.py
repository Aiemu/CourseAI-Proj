import sys
import random
import math

from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QTableWidget, QMessageBox, QAbstractItemView, QTableWidgetItem
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt

from pagesetting import *
from pagemain import *
from Markov import *

class Pages:
    def __init__(self):
        self.pageSetting = Ui_pageSetting()
        self.pageMain = Ui_pageMain()

pages = Pages()
markov = Markov()
countN = 0
start = [-1, -1]

def main():
    global countN
    arr = []
    app = QApplication(sys.argv)

    pageMain = QMainWindow()
    pages.pageMain.setupUi(pageMain)
    pageMain.show()

    pages.pageMain.btn_map.clicked.connect(lambda: setParams(pageMain))
    QApplication.processEvents()
    pages.pageMain.btn_next.clicked.connect(lambda: getNext())

    sys.exit(app.exec_())

def setParams(pageMain):
    pageSetting = QDialog(pageMain)
    pages.pageSetting.setupUi(pageSetting)
    pageSetting.show()

    pages.pageSetting.btn_generate.clicked.connect(lambda: getParams(pageSetting))

    pages.pageSetting.btn_random.clicked.connect(lambda: randomParams(pageSetting))

    QApplication.processEvents()

def getParams(pageSetting):
    global start
    xStr = pages.pageSetting.edit_x.text()
    yStr = pages.pageSetting.edit_y.text()
    
    trapsStr = pages.pageSetting.edit_trap.text().split(' ')
    barriersStr = pages.pageSetting.edit_barrier.text().split(' ')
    goalsStr = pages.pageSetting.edit_e.text().split(' ')

    sStr = pages.pageSetting.edit_s.text()[1:-1].split(',')

    if xStr == '' or yStr == '' or trapsStr == '' or barriersStr == '' or sStr == '' or goalsStr == '':
        QMessageBox.information(pageSetting,"Warning",  
                                pageSetting.tr("Please fill in all the blank"))  
        return;

    traps = []
    barriers = []
    goals = []
    s = []

    try:
        x = int(xStr)
        y = int(yStr)

        for i in trapsStr: 
            tmpList = []
            for j in i[1:-1].split(','):
                tmpList.append(int(j))
            traps.append(tmpList)

        for i in barriersStr: 
            tmpList = []
            for j in i[1:-1].split(','):
                tmpList.append(int(j))
            barriers.append(tmpList)

        for i in goalsStr: 
            tmpList = []
            for j in i[1:-1].split(','):
                tmpList.append(int(j))
            goals.append(tmpList)

        for i in sStr: 
            s.append(int(i))
    except:
        QMessageBox.information(pageSetting,"Warning",  
                                pageSetting.tr("Please use the correct input format, separate each node with a space."))  
        return

    # print(xStr, yStr, pages.pageSetting.edit_trap.text(), '_', pages.pageSetting.edit_barrier.text(), sStr, goalsStr)
    start = s

    for i in range(0, x):
        for j in range(0, y):
            item = QTableWidgetItem()
            item.setBackground(QColor('white'))
            item.setText("")
            pages.pageMain.table_left.setItem(i, j, item)

            item = QTableWidgetItem()
            item.setBackground(QColor('white'))
            item.setText("")
            pages.pageMain.table_right.setItem(i, j, item)

    pages.pageMain.table_left.setRowCount(x)
    pages.pageMain.table_left.setColumnCount(y)
    
    pages.pageMain.table_right.setRowCount(x)
    pages.pageMain.table_right.setColumnCount(y)

    xList = []
    for i in range(0, x):
        xList.append(str(i))

    yList = []
    for i in range(0, y):
        yList.append(str(i))

    pages.pageMain.table_left.setHorizontalHeaderLabels(yList)
    pages.pageMain.table_left.setVerticalHeaderLabels(xList)

    pages.pageMain.table_right.setHorizontalHeaderLabels(yList)
    pages.pageMain.table_right.setVerticalHeaderLabels(xList)

    pages.pageMain.table_left.setEditTriggers(QAbstractItemView.NoEditTriggers) 
    pages.pageMain.table_left.setSelectionMode(QAbstractItemView.NoSelection) 

    pages.pageMain.table_right.setEditTriggers(QAbstractItemView.NoEditTriggers) 
    pages.pageMain.table_right.setSelectionMode(QAbstractItemView.NoSelection) 

    size = 70
    # if 434 / y * x <= 560:
    #     size = 425 / y
    # else:
    #     size = 560 / x

    pages.pageMain.table_left.horizontalHeader().setDefaultSectionSize(size)
    pages.pageMain.table_left.verticalHeader().setDefaultSectionSize(size)

    pages.pageMain.table_right.horizontalHeader().setDefaultSectionSize(size)
    pages.pageMain.table_right.verticalHeader().setDefaultSectionSize(size)

    for i in traps:
        item = QTableWidgetItem()
        item.setBackground(QColor('grey'))
        item.setText("-1")
        item.setForeground(QColor('white'))
        item.setTextAlignment(Qt.AlignCenter)
        pages.pageMain.table_left.setItem(i[0], i[1], item)
        item = QTableWidgetItem()
        item.setBackground(QColor('grey'))
        pages.pageMain.table_right.setItem(i[0], i[1], item)

    for i in barriers:
        item = QTableWidgetItem()
        item.setBackground(QColor('black'))
        pages.pageMain.table_left.setItem(i[0], i[1], item)
        item = QTableWidgetItem()
        item.setBackground(QColor('black'))
        pages.pageMain.table_right.setItem(i[0], i[1], item)

    item = QTableWidgetItem()
    item.setBackground(QColor('blue'))
    pages.pageMain.table_left.setItem(s[0], s[1], item)
    item = QTableWidgetItem()
    item.setBackground(QColor('blue'))
    pages.pageMain.table_right.setItem(s[0], s[1], item)

    for i in goals:
        item = QTableWidgetItem()
        item.setBackground(QColor('red'))
        item.setText("1")
        item.setForeground(QColor('white'))
        item.setTextAlignment(Qt.AlignCenter)
        pages.pageMain.table_left.setItem(i[0], i[1], item)
        item = QTableWidgetItem()
        item.setBackground(QColor('red'))
        pages.pageMain.table_right.setItem(i[0], i[1], item)

    pageSetting.close()

    markov.read_map([x, y], s, barriers, traps, goals)
    markov.initialize_state()

    global countN
    countN = 0
    pages.pageMain.label_n.setText(str(countN))

    tmpDialog = QDialog()
    tmpDialog.show()
    tmpDialog.close()

    QApplication.processEvents()

def getNext():
    global countN
    global start

    if pages.pageMain.label_n.text() != '?':
        markov.update_value_once()
        arrPolicy = markov.get_policy()
        arrValue = markov.get_value()

        for i in range(0, len(arrValue)):
            for j in range(0, len(arrValue[0])):
                if arrValue[i][j] != 0:
                    item = QTableWidgetItem()
                    item.setText(str(arrValue[i][j]))
                    item.setTextAlignment(Qt.AlignCenter)
                    if i == start[0] and j == start[1]:
                        item.setBackground(QColor('blue'))
                    pages.pageMain.table_left.setItem(i, j, item)

        for i in range(0, len(arrPolicy)):
            for j in range(0, len(arrPolicy[0])):
                if arrPolicy[i][j] != '.':
                    item = QTableWidgetItem()
                    item.setText(arrPolicy[i][j])
                    item.setTextAlignment(Qt.AlignCenter)
                    if i == start[0] and j == start[1]:
                        item.setBackground(QColor('blue'))
                    pages.pageMain.table_right.setItem(i, j, item)

        countN = countN + 1
        pages.pageMain.label_n.setText(str(countN))
        tmpDialog = QDialog()
        tmpDialog.show()
        tmpDialog.close()

    QApplication.processEvents()

def randomParams(pageSetting):
    x = random.randint(3, 20)
    y = random.randint(3, 20)

    pages.pageSetting.edit_x.setText(str(x))
    pages.pageSetting.edit_y.setText(str(y))

    if math.floor(x * y / 8) > 0:
        numTraps = random.randint(1, math.floor(x * y / 8))
        numBarriers = random.randint(1, math.floor(x * y / 7))
    else:
        numTraps = 0
        numBarriers = 0


    strS = '(' + str(random.randint(0, x - 1)) + ',' + str(random.randint(0, y - 1)) + ')'
    pages.pageSetting.edit_s.setText(strS)

    strE = '(' + str(random.randint(0, x - 1)) + ',' + str(random.randint(0, y - 1)) + ')'
    while (strE == strS):
        strE = '(' + str(random.randint(0, x - 1)) + ',' + str(random.randint(0, y - 1)) + ')'
    pages.pageSetting.edit_e.setText(strE)

    strTraps = ''
    for i in range(0, numTraps):
        if i == 0:
            tmpStr = '(' + str(random.randint(0, x - 1)) + ',' + str(random.randint(0, y - 1)) + ')'
            while tmpStr == strS or tmpStr == strE:
                tmpStr = '(' + str(random.randint(0, x - 1)) + ',' + str(random.randint(0, y - 1)) + ')'

            strTraps = tmpStr
        else:
            tmpStr = '(' + str(random.randint(0, x - 1)) + ',' + str(random.randint(0, y - 1)) + ')'
            while tmpStr == strS or tmpStr == strE:
                tmpStr = '(' + str(random.randint(0, x - 1)) + ',' + str(random.randint(0, y - 1)) + ')'

            strTraps = strTraps + ' ' + tmpStr
    pages.pageSetting.edit_trap.setText(strTraps)

    strBarriers = ''
    for i in range(0, numTraps):
        if i == 0:
            tmpStr = '(' + str(random.randint(0, x - 1)) + ',' + str(random.randint(0, y - 1)) + ')'
            while tmpStr == strS or tmpStr == strE or strTraps.find(tmpStr) != -1:
                tmpStr = '(' + str(random.randint(0, x - 1)) + ',' + str(random.randint(0, y - 1)) + ')'

            strBarriers = tmpStr
        else:
            tmpStr = '(' + str(random.randint(0, x - 1)) + ',' + str(random.randint(0, y - 1)) + ')'
            while tmpStr == strS or tmpStr == strE or strTraps.find(tmpStr) != -1:
                tmpStr = '(' + str(random.randint(0, x - 1)) + ',' + str(random.randint(0, y - 1)) + ')'

            strBarriers = strBarriers + ' ' + tmpStr
    pages.pageSetting.edit_barrier.setText(strBarriers)


    QApplication.processEvents()

if __name__ == '__main__':
    main()