# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Einstellungen.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        SettingsWindow.resize(431, 618)
        self.verticalLayout = QtWidgets.QVBoxLayout(SettingsWindow)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_3 = QtWidgets.QGroupBox(SettingsWindow)
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.groupBox_3)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.comboRegelbasis = QtWidgets.QComboBox(self.groupBox_3)
        self.comboRegelbasis.setObjectName("comboRegelbasis")
        self.comboRegelbasis.addItem("")
        self.verticalLayout_5.addWidget(self.comboRegelbasis)
        self.verticalLayout_2.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(SettingsWindow)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setItalic(False)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.comboBogen = QtWidgets.QComboBox(self.groupBox)
        self.comboBogen.setObjectName("comboBogen")
        self.comboBogen.addItem("")
        self.comboBogen.addItem("")
        self.comboBogen.addItem("")
        self.verticalLayout_3.addWidget(self.comboBogen)
        self.checkCheatsheet = QtWidgets.QCheckBox(self.groupBox)
        self.checkCheatsheet.setObjectName("checkCheatsheet")
        self.verticalLayout_3.addWidget(self.checkCheatsheet)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setItalic(False)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.comboFontSize = QtWidgets.QComboBox(self.groupBox)
        self.comboFontSize.setObjectName("comboFontSize")
        self.comboFontSize.addItem("")
        self.comboFontSize.addItem("")
        self.comboFontSize.addItem("")
        self.verticalLayout_3.addWidget(self.comboFontSize)
        self.checkPDFOpen = QtWidgets.QCheckBox(self.groupBox)
        self.checkPDFOpen.setObjectName("checkPDFOpen")
        self.verticalLayout_3.addWidget(self.checkPDFOpen)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(SettingsWindow)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_4.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.editChar = QtWidgets.QLineEdit(self.groupBox_2)
        self.editChar.setReadOnly(False)
        self.editChar.setClearButtonEnabled(False)
        self.editChar.setObjectName("editChar")
        self.horizontalLayout_2.addWidget(self.editChar)
        self.buttonChar = QtWidgets.QPushButton(self.groupBox_2)
        self.buttonChar.setObjectName("buttonChar")
        self.horizontalLayout_2.addWidget(self.buttonChar)
        self.resetChar = QtWidgets.QPushButton(self.groupBox_2)
        self.resetChar.setObjectName("resetChar")
        self.horizontalLayout_2.addWidget(self.resetChar)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.editRegeln = QtWidgets.QLineEdit(self.groupBox_2)
        self.editRegeln.setObjectName("editRegeln")
        self.horizontalLayout_3.addWidget(self.editRegeln)
        self.buttonRegeln = QtWidgets.QPushButton(self.groupBox_2)
        self.buttonRegeln.setObjectName("buttonRegeln")
        self.horizontalLayout_3.addWidget(self.buttonRegeln)
        self.resetRegeln = QtWidgets.QPushButton(self.groupBox_2)
        self.resetRegeln.setObjectName("resetRegeln")
        self.horizontalLayout_3.addWidget(self.resetRegeln)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.editPlugins = QtWidgets.QLineEdit(self.groupBox_2)
        self.editPlugins.setObjectName("editPlugins")
        self.horizontalLayout_4.addWidget(self.editPlugins)
        self.buttonPlugins = QtWidgets.QPushButton(self.groupBox_2)
        self.buttonPlugins.setObjectName("buttonPlugins")
        self.horizontalLayout_4.addWidget(self.buttonPlugins)
        self.resetPlugins = QtWidgets.QPushButton(self.groupBox_2)
        self.resetPlugins.setObjectName("resetPlugins")
        self.horizontalLayout_4.addWidget(self.resetPlugins)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.vlPlugins = QtWidgets.QVBoxLayout()
        self.vlPlugins.setObjectName("vlPlugins")
        self.verticalLayout_4.addLayout(self.vlPlugins)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_5 = QtWidgets.QLabel(self.groupBox_4)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_6.addWidget(self.label_5)
        self.comboLogging = QtWidgets.QComboBox(self.groupBox_4)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboLogging.sizePolicy().hasHeightForWidth())
        self.comboLogging.setSizePolicy(sizePolicy)
        self.comboLogging.setObjectName("comboLogging")
        self.comboLogging.addItem("")
        self.comboLogging.addItem("")
        self.comboLogging.addItem("")
        self.verticalLayout_6.addWidget(self.comboLogging)
        self.verticalLayout_4.addWidget(self.groupBox_4)
        self.verticalLayout_2.addWidget(self.groupBox_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(SettingsWindow)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(SettingsWindow)
        self.comboLogging.setCurrentIndex(1)
        self.buttonBox.accepted.connect(SettingsWindow.accept)
        self.buttonBox.rejected.connect(SettingsWindow.reject)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)
        SettingsWindow.setTabOrder(self.comboRegelbasis, self.comboBogen)
        SettingsWindow.setTabOrder(self.comboBogen, self.checkCheatsheet)
        SettingsWindow.setTabOrder(self.checkCheatsheet, self.comboFontSize)
        SettingsWindow.setTabOrder(self.comboFontSize, self.checkPDFOpen)
        SettingsWindow.setTabOrder(self.checkPDFOpen, self.editChar)
        SettingsWindow.setTabOrder(self.editChar, self.buttonChar)
        SettingsWindow.setTabOrder(self.buttonChar, self.resetChar)
        SettingsWindow.setTabOrder(self.resetChar, self.editRegeln)
        SettingsWindow.setTabOrder(self.editRegeln, self.buttonRegeln)
        SettingsWindow.setTabOrder(self.buttonRegeln, self.resetRegeln)
        SettingsWindow.setTabOrder(self.resetRegeln, self.editPlugins)
        SettingsWindow.setTabOrder(self.editPlugins, self.buttonPlugins)
        SettingsWindow.setTabOrder(self.buttonPlugins, self.resetPlugins)
        SettingsWindow.setTabOrder(self.resetPlugins, self.comboLogging)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Sephrasto - Einstellungen"))
        self.groupBox_3.setTitle(_translate("SettingsWindow", "Regelbasis"))
        self.label_4.setText(_translate("SettingsWindow", "Aktuelle Nutzer-Regelbasis:"))
        self.comboRegelbasis.setItemText(0, _translate("SettingsWindow", "Keine"))
        self.groupBox.setTitle(_translate("SettingsWindow", "Charakterbogen"))
        self.label.setText(_translate("SettingsWindow", "Welcher Charakterbogen soll verwendet werden?"))
        self.comboBogen.setItemText(0, _translate("SettingsWindow", "Frag immer nach"))
        self.comboBogen.setItemText(1, _translate("SettingsWindow", "Standard Ilaris-Charakterbogen"))
        self.comboBogen.setItemText(2, _translate("SettingsWindow", "Die lange Version von Gatsu"))
        self.checkCheatsheet.setText(_translate("SettingsWindow", "Cheatsheet mit den Regeln anhängen"))
        self.label_6.setText(_translate("SettingsWindow", "Cheatsheet Schriftgröße:"))
        self.comboFontSize.setItemText(0, _translate("SettingsWindow", "Klein"))
        self.comboFontSize.setItemText(1, _translate("SettingsWindow", "Mittel"))
        self.comboFontSize.setItemText(2, _translate("SettingsWindow", "Groß"))
        self.checkPDFOpen.setText(_translate("SettingsWindow", "PDF nach dem Erstellen öffnen"))
        self.groupBox_2.setTitle(_translate("SettingsWindow", "Speicherpfade"))
        self.label_2.setText(_translate("SettingsWindow", "Speicherpfad für Charaktere:"))
        self.buttonChar.setText(_translate("SettingsWindow", "Durchsuchen"))
        self.resetChar.setText(_translate("SettingsWindow", "Zurücksetzen"))
        self.label_3.setText(_translate("SettingsWindow", "Speicherpfad für Regeln:"))
        self.buttonRegeln.setText(_translate("SettingsWindow", "Durchsuchen"))
        self.resetRegeln.setText(_translate("SettingsWindow", "Zurücksetzen"))
        self.label_7.setText(_translate("SettingsWindow", "Speicherpfad für Plugins:"))
        self.buttonPlugins.setText(_translate("SettingsWindow", "Durchsuchen"))
        self.resetPlugins.setText(_translate("SettingsWindow", "Zurücksetzen"))
        self.groupBox_4.setTitle(_translate("SettingsWindow", "Sonstiges"))
        self.label_5.setText(_translate("SettingsWindow", "Logging-Level:"))
        self.comboLogging.setItemText(0, _translate("SettingsWindow", "Protokolliere nur Fehler"))
        self.comboLogging.setItemText(1, _translate("SettingsWindow", "Protokolliere Warnungen und Fehler"))
        self.comboLogging.setItemText(2, _translate("SettingsWindow", "Protokolliere auch Debugging-Informationen"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SettingsWindow = QtWidgets.QDialog()
    ui = Ui_SettingsWindow()
    ui.setupUi(SettingsWindow)
    SettingsWindow.show()
    sys.exit(app.exec_())
