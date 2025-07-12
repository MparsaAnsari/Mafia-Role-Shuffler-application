from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
import sys
import mafiaUI
import random
import os
import pickle

class guiControl:
    def __init__(self, ui, app):
        self.ui = ui
        self.app = app
        self.defineConnections()
        self.selectedRoles = []
        self.allDecks = {}

        if os.path.exists("mafiSettings.pk"):
            pkl = open("mafiSettings.pk", 'rb')
            loaded = pickle.load(pkl)
            pkl.close()


            self.allDecks = loaded["allDecks"]
            availableRoles = loaded["roles"]

            self.ui.availableRolesList.clear()
            for item in availableRoles:
                self.ui.availableRolesList.addItem(item)

            for item in self.allDecks:
                self.ui.availableDecksList.addItem(item)

    def saveBeforeExit(self):
        try:
            dic = {}
            dic["allDecks"] = self.allDecks
            roles = []
            for index in range(self.ui.availableRolesList.count()):
                roles.append(self.ui.availableRolesList.item(index).text())
            dic["roles"] = roles
            pkl = open("mafiSettings.pk", 'wb')
            pickle.dump(dic, pkl)
            pkl.close()
        except:
            pass

    def defineConnections(self):
        self.ui.saveDeckPB.clicked.connect(self.saveDeck)
        self.ui.availableRolesList.doubleClicked.connect(self.addToSelected)
        self.ui.selectedRoleList.doubleClicked.connect(self.removeSelected)
        self.ui.generatedRoleList.doubleClicked.connect(self.removeFromGenRole)

        self.ui.genRolesPB.clicked.connect(self.genRoles)
        self.ui.addRolePB.clicked.connect(self.addRole)
        self.ui.availableDecksList.clicked.connect(self.updateDeck)
        self.ui.clearPB.clicked.connect(self.clearSelected)
        self.ui.removeDeckPB.clicked.connect(self.removeDeck)
        self.ui.removeRolePB.clicked.connect(self.removeRole)
        self.ui.instantAddPB.clicked.connect(self.instantAdd)


    def instantAdd(self):
        try:
            role = self.ui.availableRolesList.currentItem().text()
            self.generatedRoles.append(role)
            self.ui.generatedRoleList.addItem(role)
        except:
            pass

    def removeFromGenRole(self):
        try:
            role = self.ui.generatedRoleList.currentItem().text()
            self.ui.generatedRoleList.takeItem(self.ui.generatedRoleList.currentRow())
            self.generatedRoles.remove(role)
        except:
            pass

    def clearSelected(self):
        self.ui.selectedRoleList.clear()
        self.selectedRoles.clear()
        self.ui.countLabel.setText(str(self.ui.selectedRoleList.count()))

    def removeDeck(self):
        try:
            deckName = self.ui.availableDecksList.currentItem().text()
            self.ui.availableDecksList.takeItem(self.ui.availableDecksList.currentRow())
            self.allDecks.pop(deckName)
        except:
            pass

    def removeRole(self):
        try:
            self.ui.availableRolesList.takeItem(self.ui.availableRolesList.currentRow())
        except:
            pass

    def saveDeck(self):
        try:
            roles = []
            for index in range(self.ui.selectedRoleList.count()):
                roles.append(self.ui.selectedRoleList.item(index).text())

            deckName = self.ui.deckNameTB.text() + " ( " + str(self.ui.selectedRoleList.count()) + " ) "

            self.allDecks[deckName] = roles
            self.ui.availableDecksList.addItem(deckName)
            self.ui.deckNameTB.clear()
        except:
            pass

    def removeSelected(self):
        try:
            role = self.ui.selectedRoleList.currentItem().text()
            self.ui.selectedRoleList.takeItem(self.ui.selectedRoleList.currentRow())
            self.selectedRoles.remove(role)
            self.ui.countLabel.setText(str(self.ui.selectedRoleList.count()))
        except:
            pass

    def addToSelected(self):
        try:
            role = self.ui.availableRolesList.currentItem().text()
            newItem =QtWidgets.QListWidgetItem(role)
            if role in self.selectedRoles:
                newItem.setBackground(Qt.cyan)
            self.ui.selectedRoleList.addItem(newItem)
            self.selectedRoles.append(role)
            self.ui.countLabel.setText(str(self.ui.selectedRoleList.count()))
        except:
            pass

    def updateDeck(self):
        try:
            self.ui.generatedRoleList.clear()
            deck = self.ui.availableDecksList.currentItem().text()
            self.generatedRoles = []

            for item in self.allDecks[deck]:
                self.ui.generatedRoleList.addItem(item)
                self.generatedRoles.append(item)
        except:
            pass


    def genRoles(self):
        try:
            deck = self.generatedRoles
            random.shuffle(deck)
            self.ui.generatedRoleList.clear()
            for i in range(len(deck)):
                self.ui.generatedRoleList.addItem(str(i+1) + " - " + deck[i])
        except:
            pass

    def addRole(self):
        try:
            newRole = self.ui.newRoleTB.text()
            self.ui.availableRolesList.addItem(newRole)
            self.ui.newRoleTB.clear()
        except:
            pass


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = mafiaUI.Ui_Mafs()
ui.setupUi(MainWindow)

gui = guiControl(ui, app)
MainWindow.setWindowTitle("Mafia")
MainWindow.show()
ret = app.exec_()

gui.saveBeforeExit()
