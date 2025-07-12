# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mafiaGui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Mafs(object):
    def setupUi(self, Mafs):
        Mafs.setObjectName("Mafs")
        Mafs.resize(713, 531)
        self.mafsGB = QtWidgets.QGroupBox(Mafs)
        self.mafsGB.setGeometry(QtCore.QRect(0, -10, 711, 541))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.mafsGB.setFont(font)
        self.mafsGB.setTitle("")
        self.mafsGB.setObjectName("mafsGB")
        self.availableRolesList = QtWidgets.QListWidget(self.mafsGB)
        self.availableRolesList.setGeometry(QtCore.QRect(20, 60, 151, 331))
        self.availableRolesList.setStyleSheet("QListWidget{\n"
"background: white;\n"
"border: 1px solid darkgray;\n"
"border-radius: 20px;\n"
"padding: 10px;\n"
"}")
        self.availableRolesList.setObjectName("availableRolesList")
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.availableRolesList.addItem(item)
        self.deviceTypeLabel = QtWidgets.QLabel(self.mafsGB)
        self.deviceTypeLabel.setGeometry(QtCore.QRect(30, 30, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.deviceTypeLabel.setFont(font)
        self.deviceTypeLabel.setObjectName("deviceTypeLabel")
        self.deviceTypeLabel_2 = QtWidgets.QLabel(self.mafsGB)
        self.deviceTypeLabel_2.setGeometry(QtCore.QRect(180, 30, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.deviceTypeLabel_2.setFont(font)
        self.deviceTypeLabel_2.setObjectName("deviceTypeLabel_2")
        self.generatedRoleList = QtWidgets.QListWidget(self.mafsGB)
        self.generatedRoleList.setGeometry(QtCore.QRect(540, 60, 151, 331))
        self.generatedRoleList.setStyleSheet("QListWidget{\n"
"background: white;\n"
"border: 1px solid darkgray;\n"
"border-radius: 20px;\n"
"padding: 10px;\n"
"}")
        self.generatedRoleList.setObjectName("generatedRoleList")
        self.saveDeckPB = QtWidgets.QPushButton(self.mafsGB)
        self.saveDeckPB.setGeometry(QtCore.QRect(450, 420, 51, 41))
        self.saveDeckPB.setStyleSheet("QPushButton{\n"
"background:  rgb(232, 232, 232);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 salmon);\n"
"border-width: 5px;\n"
"border-radius: 10px;\n"
"font: 75 bold 9pt \"Cambria\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(111, 111, 111);\n"
"    border-style: inset;\n"
"}")
        self.saveDeckPB.setObjectName("saveDeckPB")
        self.deviceTypeLabel_3 = QtWidgets.QLabel(self.mafsGB)
        self.deviceTypeLabel_3.setGeometry(QtCore.QRect(370, 30, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.deviceTypeLabel_3.setFont(font)
        self.deviceTypeLabel_3.setObjectName("deviceTypeLabel_3")
        self.genRolesPB = QtWidgets.QPushButton(self.mafsGB)
        self.genRolesPB.setGeometry(QtCore.QRect(550, 400, 131, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.genRolesPB.setFont(font)
        self.genRolesPB.setStyleSheet("QPushButton{\n"
"background:  rgb(232, 232, 232);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 orange);\n"
"border-width: 5px;\n"
"border-radius: 10px;\n"
"font: 75 bold 9pt \"Cambria\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(111, 111, 111);\n"
"    border-style: inset;\n"
"}")
        self.genRolesPB.setObjectName("genRolesPB")
        self.deviceTypeLabel_4 = QtWidgets.QLabel(self.mafsGB)
        self.deviceTypeLabel_4.setGeometry(QtCore.QRect(530, 30, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.deviceTypeLabel_4.setFont(font)
        self.deviceTypeLabel_4.setObjectName("deviceTypeLabel_4")
        self.deviceTypeLabel_5 = QtWidgets.QLabel(self.mafsGB)
        self.deviceTypeLabel_5.setGeometry(QtCore.QRect(190, 400, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.deviceTypeLabel_5.setFont(font)
        self.deviceTypeLabel_5.setObjectName("deviceTypeLabel_5")
        self.deviceTypeLabel_6 = QtWidgets.QLabel(self.mafsGB)
        self.deviceTypeLabel_6.setGeometry(QtCore.QRect(20, 395, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.deviceTypeLabel_6.setFont(font)
        self.deviceTypeLabel_6.setObjectName("deviceTypeLabel_6")
        self.newRoleTB = QtWidgets.QLineEdit(self.mafsGB)
        self.newRoleTB.setGeometry(QtCore.QRect(20, 420, 91, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.newRoleTB.setFont(font)
        self.newRoleTB.setStyleSheet("QLineEdit{\n"
"background: white;\n"
"border: 1px solid darkgray;\n"
"border-radius: 20px;\n"
"padding: 5px;\n"
"}")
        self.newRoleTB.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.newRoleTB.setObjectName("newRoleTB")
        self.addRolePB = QtWidgets.QPushButton(self.mafsGB)
        self.addRolePB.setGeometry(QtCore.QRect(120, 420, 51, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.addRolePB.setFont(font)
        self.addRolePB.setStyleSheet("QPushButton{\n"
"background:  rgb(232, 232, 232);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 coral);\n"
"border-width: 5px;\n"
"border-radius: 10px;\n"
"font: 75 bold 9pt \"Cambria\";\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(111, 111, 111);\n"
"    border-style: inset;\n"
"}")
        self.addRolePB.setObjectName("addRolePB")
        self.selectedRoleList = QtWidgets.QListWidget(self.mafsGB)
        self.selectedRoleList.setGeometry(QtCore.QRect(180, 60, 141, 331))
        self.selectedRoleList.setStyleSheet("QListWidget{\n"
"background: white;\n"
"border: 1px solid darkgray;\n"
"border-radius: 20px;\n"
"padding: 10px;\n"
"}")
        self.selectedRoleList.setObjectName("selectedRoleList")
        self.deckNameTB = QtWidgets.QLineEdit(self.mafsGB)
        self.deckNameTB.setGeometry(QtCore.QRect(340, 420, 91, 40))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.deckNameTB.setFont(font)
        self.deckNameTB.setStyleSheet("QLineEdit{\n"
"background: white;\n"
"border: 1px solid darkgray;\n"
"border-radius: 20px;\n"
"padding: 5px;\n"
"}")
        self.deckNameTB.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.deckNameTB.setObjectName("deckNameTB")
        self.deviceTypeLabel_7 = QtWidgets.QLabel(self.mafsGB)
        self.deviceTypeLabel_7.setGeometry(QtCore.QRect(340, 395, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.deviceTypeLabel_7.setFont(font)
        self.deviceTypeLabel_7.setObjectName("deviceTypeLabel_7")
        self.countLabel = QtWidgets.QLabel(self.mafsGB)
        self.countLabel.setGeometry(QtCore.QRect(240, 400, 71, 21))
        self.countLabel.setStyleSheet("QLabel{\n"
"border-style: outset;\n"
"border-width: 2px;\n"
"border-color: gray;\n"
"}")
        self.countLabel.setObjectName("countLabel")
        self.availableDecksList = QtWidgets.QListWidget(self.mafsGB)
        self.availableDecksList.setGeometry(QtCore.QRect(330, 60, 191, 331))
        self.availableDecksList.setStyleSheet("QListWidget{\n"
"background: white;\n"
"border: 1px solid darkgray;\n"
"border-radius: 20px;\n"
"padding: 10px;\n"
"}")
        self.availableDecksList.setObjectName("availableDecksList")
        self.deviceTypeLabel_8 = QtWidgets.QLabel(self.mafsGB)
        self.deviceTypeLabel_8.setGeometry(QtCore.QRect(630, 510, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(7)
        font.setItalic(True)
        self.deviceTypeLabel_8.setFont(font)
        self.deviceTypeLabel_8.setStyleSheet("")
        self.deviceTypeLabel_8.setObjectName("deviceTypeLabel_8")
        self.clearPB = QtWidgets.QPushButton(self.mafsGB)
        self.clearPB.setGeometry(QtCore.QRect(190, 440, 121, 20))
        self.clearPB.setStyleSheet("QPushButton{\n"
"background:  rgb(232, 232, 232);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 goldenrod);\n"
"border-width: 5px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(111, 111, 111);\n"
"    border-style: inset;\n"
"}")
        self.clearPB.setObjectName("clearPB")
        self.removeDeckPB = QtWidgets.QPushButton(self.mafsGB)
        self.removeDeckPB.setGeometry(QtCore.QRect(340, 470, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.removeDeckPB.setFont(font)
        self.removeDeckPB.setStyleSheet("QPushButton{\n"
"background:  rgb(232, 232, 232);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 firebrick);\n"
"border-width: 5px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(111, 111, 111);\n"
"    border-style: inset;\n"
"}")
        self.removeDeckPB.setObjectName("removeDeckPB")
        self.removeRolePB = QtWidgets.QPushButton(self.mafsGB)
        self.removeRolePB.setGeometry(QtCore.QRect(20, 500, 151, 21))
        self.removeRolePB.setStyleSheet("QPushButton{\n"
"background:  rgb(232, 232, 232);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 orangered);\n"
"border-width: 5px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(111, 111, 111);\n"
"    border-style: inset;\n"
"}")
        self.removeRolePB.setObjectName("removeRolePB")
        self.instantAddPB = QtWidgets.QPushButton(self.mafsGB)
        self.instantAddPB.setGeometry(QtCore.QRect(20, 470, 151, 21))
        self.instantAddPB.setToolTip("")
        self.instantAddPB.setToolTipDuration(3)
        self.instantAddPB.setStyleSheet("QPushButton{\n"
"background:  rgb(232, 232, 232);\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 white, stop: 1 gold);\n"
"border-width: 5px;\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: rgb(111, 111, 111);\n"
"    border-style: inset;\n"
"}")
        self.instantAddPB.setObjectName("instantAddPB")

        self.retranslateUi(Mafs)
        QtCore.QMetaObject.connectSlotsByName(Mafs)

    def retranslateUi(self, Mafs):
        _translate = QtCore.QCoreApplication.translate
        Mafs.setWindowTitle(_translate("Mafs", "Form"))
        __sortingEnabled = self.availableRolesList.isSortingEnabled()
        self.availableRolesList.setSortingEnabled(False)
        item = self.availableRolesList.item(0)
        item.setText(_translate("Mafs", "رییس مافیا"))
        item = self.availableRolesList.item(1)
        item.setText(_translate("Mafs", "مذاکره‌کننده"))
        item = self.availableRolesList.item(2)
        item.setText(_translate("Mafs", "مافیا ساده"))
        item = self.availableRolesList.item(3)
        item.setText(_translate("Mafs", "افسون‌گر"))
        item = self.availableRolesList.item(4)
        item.setText(_translate("Mafs", "ناتو"))
        item = self.availableRolesList.item(5)
        item.setText(_translate("Mafs", "ترور"))
        item = self.availableRolesList.item(6)
        item.setText(_translate("Mafs", "جادوگر"))
        item = self.availableRolesList.item(7)
        item.setText(_translate("Mafs", "ناتاشا"))
        item = self.availableRolesList.item(8)
        item.setText(_translate("Mafs", "وکیل"))
        item = self.availableRolesList.item(9)
        item.setText(_translate("Mafs", "دزد"))
        item = self.availableRolesList.item(10)
        item.setText(_translate("Mafs", "خرابکار"))
        item = self.availableRolesList.item(11)
        item.setText(_translate("Mafs", "شهر ساده"))
        item = self.availableRolesList.item(12)
        item.setText(_translate("Mafs", "دکتر"))
        item = self.availableRolesList.item(13)
        item.setText(_translate("Mafs", "کاراگاه"))
        item = self.availableRolesList.item(14)
        item.setText(_translate("Mafs", "اسنایپر"))
        item = self.availableRolesList.item(15)
        item.setText(_translate("Mafs", "خبرنگار"))
        item = self.availableRolesList.item(16)
        item.setText(_translate("Mafs", "زره‌پوش"))
        item = self.availableRolesList.item(17)
        item.setText(_translate("Mafs", "تفنگ‌دار"))
        item = self.availableRolesList.item(18)
        item.setText(_translate("Mafs", "تکاور"))
        item = self.availableRolesList.item(19)
        item.setText(_translate("Mafs", "نگهبان"))
        item = self.availableRolesList.item(20)
        item.setText(_translate("Mafs", "قاضی"))
        item = self.availableRolesList.item(21)
        item.setText(_translate("Mafs", "کابوی"))
        item = self.availableRolesList.item(22)
        item.setText(_translate("Mafs", "آهنگر"))
        item = self.availableRolesList.item(23)
        item.setText(_translate("Mafs", "ساقی"))
        item = self.availableRolesList.item(24)
        item.setText(_translate("Mafs", "گورکن"))
        item = self.availableRolesList.item(25)
        item.setText(_translate("Mafs", "کشیش"))
        item = self.availableRolesList.item(26)
        item.setText(_translate("Mafs", "مسیح"))
        item = self.availableRolesList.item(27)
        item.setText(_translate("Mafs", "ماسون"))
        item = self.availableRolesList.item(28)
        item.setText(_translate("Mafs", "تایلر"))
        item = self.availableRolesList.item(29)
        item.setText(_translate("Mafs", "پرستار"))
        item = self.availableRolesList.item(30)
        item.setText(_translate("Mafs", "انگل"))
        item = self.availableRolesList.item(31)
        item.setText(_translate("Mafs", "دلقک"))
        item = self.availableRolesList.item(32)
        item.setText(_translate("Mafs", "قلدر"))
        item = self.availableRolesList.item(33)
        item.setText(_translate("Mafs", "هفت‌تیرکش"))
        item = self.availableRolesList.item(34)
        item.setText(_translate("Mafs", "سایه"))
        self.availableRolesList.setSortingEnabled(__sortingEnabled)
        self.deviceTypeLabel.setText(_translate("Mafs", "نقش‌های موجود"))
        self.deviceTypeLabel_2.setText(_translate("Mafs", "نقش‌های دک جدید"))
        self.saveDeckPB.setText(_translate("Mafs", "ذخیره"))
        self.deviceTypeLabel_3.setText(_translate("Mafs", "دک‌های موجود"))
        self.genRolesPB.setText(_translate("Mafs", "نقش بده"))
        self.deviceTypeLabel_4.setText(_translate("Mafs", "نقش‌های داده شده برای بازی"))
        self.deviceTypeLabel_5.setText(_translate("Mafs", "Count:"))
        self.deviceTypeLabel_6.setText(_translate("Mafs", "نام نفش جدید"))
        self.addRolePB.setText(_translate("Mafs", "اضافه"))
        self.deviceTypeLabel_7.setText(_translate("Mafs", "نام دک جدید"))
        self.countLabel.setText(_translate("Mafs", "<html><head/><body><p><br/></p></body></html>"))
        self.deviceTypeLabel_8.setText(_translate("Mafs", "By: Mary Juana"))
        self.clearPB.setText(_translate("Mafs", "پاک کردن نقش‌های دک"))
        self.removeDeckPB.setText(_translate("Mafs", "حذف دک"))
        self.removeRolePB.setText(_translate("Mafs", "حذف نقش"))
        self.instantAddPB.setText(_translate("Mafs", "اضافه به نقش‌های بازی"))
