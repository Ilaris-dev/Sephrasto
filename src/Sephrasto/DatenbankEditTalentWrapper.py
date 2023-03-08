# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 11:04:21 2017

@author: Aeolitus
"""
import Fertigkeiten
from Hilfsmethoden import Hilfsmethoden, VoraussetzungException
import UI.DatenbankEditTalent
from PySide6 import QtWidgets, QtCore
from TextTagCompleter import TextTagCompleter
from Wolke import Wolke
import re

class DatenbankEditTalentWrapper(object):
    def __init__(self, datenbank, talent=None, readonly=False):
        super().__init__()
        self.datenbank = datenbank
        if talent is None:
            talent = Fertigkeiten.Talent()
        self.talentPicked = talent
        self.nameValid = True
        self.voraussetzungenValid = True
        self.fertigkeitenValid = True
        self.readonly = readonly
        self.talentDialog = QtWidgets.QDialog()
        self.talentDialog.accept = lambda: self.accept()
        self.ui = UI.DatenbankEditTalent.Ui_talentDialog()
        self.ui.setupUi(self.talentDialog)

        if not talent.isUserAdded:
            if readonly:
                self.ui.warning.setText("Gelöschte Elemente können nicht verändert werden.")
            self.ui.warning.setVisible(True)

        self.talentDialog.setWindowFlags(
                QtCore.Qt.Window |
                QtCore.Qt.CustomizeWindowHint |
                QtCore.Qt.WindowTitleHint |
                QtCore.Qt.WindowCloseButtonHint |
                QtCore.Qt.WindowMaximizeButtonHint |
                QtCore.Qt.WindowMinimizeButtonHint)

        self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Save).setText("Speichern")
        self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel).setText("Abbrechen")
        
        windowSize = Wolke.Settings["WindowSize-DBTalent"]
        self.talentDialog.resize(windowSize[0], windowSize[1])

        self.ui.nameEdit.setText(talent.name)
        self.ui.nameEdit.textChanged.connect(self.nameChanged)
        self.nameChanged()
        if talent.verbilligt:
            self.ui.buttonVerbilligt.setChecked(True)
        elif talent.kosten != -1:
            self.ui.buttonSpezial.setChecked(True)
            self.ui.spinKosten.setValue(talent.kosten)
            self.ui.checkCheatsheet.setChecked(talent.cheatsheetAuflisten)
        else:
            self.ui.buttonRegulaer.setChecked(True)
        if talent.variableKosten:
            self.ui.checkVariable.setChecked(True)
        else:
            self.ui.checkVariable.setChecked(False)

        if talent.kommentarErlauben:
            self.ui.checkKommentar.setChecked(True)
        else:
            self.ui.checkKommentar.setChecked(False)

        self.fertigkeitenCompleter = TextTagCompleter(self.ui.fertigkeitenEdit, [])
        self.ui.fertigkeitenEdit.setText(Hilfsmethoden.FertArray2Str(talent.fertigkeiten, None))
        self.ui.fertigkeitenEdit.textChanged.connect(self.fertigkeitenTextChanged)
        
        self.ui.buttonRegulaer.clicked.connect(self.kostenChanged)
        self.ui.buttonVerbilligt.clicked.connect(self.kostenChanged)
        self.ui.buttonSpezial.clicked.connect(self.kostenChanged)
        self.kostenChanged()

        self.ui.checkVariable.clicked.connect(self.variableKostenCheckChanged)
        self.variableKostenCheckChanged()

        self.ui.voraussetzungenEdit.setPlainText(Hilfsmethoden.VorArray2Str(talent.voraussetzungen, None))
        self.ui.voraussetzungenEdit.textChanged.connect(self.voraussetzungenTextChanged)

        self.ui.textEdit.setPlainText(talent.text)

        bücher = datenbank.einstellungen["Referenzbücher"].toTextList()
        if (len(bücher) > 0):
            self.ui.comboSeite.addItems(bücher)
            self.ui.comboSeite.setCurrentIndex(self.talentPicked.referenzBuch)
        self.ui.spinSeite.setValue(self.talentPicked.referenzSeite)

        self.talentDialog.show()
        ret = self.talentDialog.exec()

        Wolke.Settings["WindowSize-DBTalent"] = [self.talentDialog.size().width(), self.talentDialog.size().height()]

        if ret == QtWidgets.QDialog.Accepted:
            self.talent = Fertigkeiten.Talent()
            self.talent.name = self.ui.nameEdit.text()
            self.talent.fertigkeiten = Hilfsmethoden.FertStr2Array(self.ui.fertigkeitenEdit.text(),None)
            self.talent.voraussetzungen = Hilfsmethoden.VorStr2Array(self.ui.voraussetzungenEdit.toPlainText(), datenbank)
            self.talent.text = self.ui.textEdit.toPlainText()
            self.talent.kosten = -1

            self.talent.kommentarErlauben = self.ui.checkKommentar.isChecked()
            self.talent.variableKosten = self.ui.checkVariable.isChecked()

            if self.ui.buttonSpezial.isChecked():
                self.talent.kosten = self.ui.spinKosten.value()
            elif self.ui.buttonVerbilligt.isChecked():
                self.talent.verbilligt = 1
            self.talent.cheatsheetAuflisten = self.ui.checkCheatsheet.isChecked()

            self.talent.referenzBuch = self.ui.comboSeite.currentIndex()
            self.talent.referenzSeite = self.ui.spinSeite.value()

            self.talent.isUserAdded = False
            if self.talent == self.talentPicked:
                self.talent = None
            else:
                self.talent.isUserAdded = True
        else:
            self.talent = None

    def kostenChanged(self):
        self.ui.spinKosten.setEnabled(self.ui.buttonSpezial.isChecked())
        self.ui.checkCheatsheet.setEnabled(self.ui.buttonSpezial.isChecked())
        self.ui.comboSeite.setEnabled(self.ui.buttonSpezial.isChecked())
        self.ui.spinSeite.setEnabled(self.ui.buttonSpezial.isChecked())

        if self.ui.buttonSpezial.isChecked():
            self.fertigkeitenCompleter.setTags([f for f in self.datenbank.übernatürlicheFertigkeiten.keys()])
        else:
            self.fertigkeitenCompleter.setTags([f for f in self.datenbank.fertigkeiten.keys()])
        self.fertigkeitenTextChanged()

    def variableKostenCheckChanged(self):
        if self.ui.checkVariable.isChecked():
            self.ui.checkKommentar.setChecked(self.ui.checkVariable.isChecked())
        self.ui.checkKommentar.setEnabled(not self.ui.checkVariable.isChecked())

    def nameChanged(self):
        name = self.ui.nameEdit.text()
        fertigkeiten = Hilfsmethoden.FertStr2Array(self.ui.fertigkeitenEdit.text(),None)
        if name == "":
            self.ui.nameEdit.setToolTip("Name darf nicht leer sein.")
            self.ui.nameEdit.setStyleSheet("border: 1px solid red;")
            self.nameValid = False
        elif name != self.talentPicked.name and name in self.datenbank.talente:
            self.ui.nameEdit.setToolTip("Name existiert bereits.")
            self.ui.nameEdit.setStyleSheet("border: 1px solid red;")
            self.nameValid = False
        elif "Gebräuche" in fertigkeiten and not name.startswith("Gebräuche: "):
            self.ui.nameEdit.setToolTip("Talentnamen für die Fertigkeit Gebräuche müssen mit 'Gebräuche: ' anfangen.")
            self.ui.nameEdit.setStyleSheet("border: 1px solid red;")
            self.nameValid = False
        else:
            self.ui.nameEdit.setToolTip("")
            self.ui.nameEdit.setStyleSheet("")
            self.nameValid = True
        self.updateSaveButtonState()

    def voraussetzungenTextChanged(self):
        try:
            Hilfsmethoden.VorStr2Array(self.ui.voraussetzungenEdit.toPlainText(), self.datenbank)
            self.ui.voraussetzungenEdit.setStyleSheet("")
            self.ui.voraussetzungenEdit.setToolTip("")
            self.voraussetzungenValid = True
        except VoraussetzungException as e:
            self.ui.voraussetzungenEdit.setStyleSheet("border: 1px solid red;")
            self.ui.voraussetzungenEdit.setToolTip(str(e))
            self.voraussetzungenValid = False
        self.updateSaveButtonState()

    def fertigkeitenTextChanged(self):
        fertigkeiten = Hilfsmethoden.FertStr2Array(self.ui.fertigkeitenEdit.text(),None)
        self.fertigkeitenValid = True
        for fertigkeit in fertigkeiten:
            if self.ui.buttonSpezial.isChecked():
                if not fertigkeit in self.datenbank.übernatürlicheFertigkeiten:
                    self.ui.fertigkeitenEdit.setStyleSheet("border: 1px solid red;")
                    self.ui.fertigkeitenEdit.setToolTip("Unbekannte übernatürliche Fertigkeit '" + fertigkeit + "'. Spezialtalente müssen übernatürlichen Fertigkeiten zugewiesen werden.")
                    self.fertigkeitenValid = False
                    break
            else:
                if not fertigkeit in self.datenbank.fertigkeiten:
                    self.ui.fertigkeitenEdit.setStyleSheet("border: 1px solid red;")
                    self.ui.fertigkeitenEdit.setToolTip("Unbekannte profane Fertigkeit '" + fertigkeit + "'. Reguläre Talente müssen profanen Fertigkeiten zugewiesen werden.")
                    self.fertigkeitenValid = False
                    break

        if self.fertigkeitenValid:
            self.ui.fertigkeitenEdit.setStyleSheet("")
            self.ui.fertigkeitenEdit.setToolTip("")
        self.nameChanged()

    def updateSaveButtonState(self):
        self.ui.buttonBox.button(QtWidgets.QDialogButtonBox.Save).setEnabled(not self.readonly and self.nameValid and self.voraussetzungenValid and self.fertigkeitenValid)

    def accept(self):
        text = self.ui.textEdit.toPlainText()
        example = ""
        bold = ["Mächtige Magie:", "Mächtige Liturgie:", "Mächtige Anrufung:", "Probenschwierigkeit:", "Modifikationen:", "Vorbereitungszeit:",
                "Ziel:", "Reichweite:", "Wirkungsdauer:", "Kosten:", "Fertigkeiten:", "Erlernen:", "Anmerkung:", "Sephrasto:", "Fertigkeit Eis:",
                "Fertigkeit Erz:", "Fertigkeit Feuer:", "Fertigkeit Humus:", "Fertigkeit Luft:", "Fertigkeit Wasser:"]
        boldPattern = re.compile("(?<!<b>)(" + "|".join(bold) + ")(?!</b>)")
        italic = ["Konterprobe", "Aufrechterhalten", "Ballistischer", "Ballistische", "Erfrieren", "Niederschmettern", "Nachbrennen", "Fesseln", "Zurückstoßen", "Ertränken", "Konzentration", "Objektritual", "Objektrituale"]
        italicPattern = re.compile("(?<!<i>)(" + "|".join(italic) + ")(?!</i>)")
        illusionPattern = re.compile("(?<!<i>)Illusion \((Sicht|Gehör|Geruch|Geschmack|Tast)")

        match = boldPattern.search(text)
        if match:
            example = "\"" + match.group(0)[:-1] + "\", normalerweise fett"
        if not match:
            match = italicPattern.search(text)
            if match:
                example = "\"" + match.group(0) + "\", normalerweise kursiv"
        if not match:
            match = illusionPattern.search(text)
            if match:
                example = "Illusion, normalerweise kursiv"

        if match:
            messageBox = QtWidgets.QMessageBox()
            messageBox.setIcon(QtWidgets.QMessageBox.Warning)
            messageBox.setWindowTitle("Formatierung der Beschreibung anpassen?")
            messageBox.setText("Die Beschreibung enthält Schlüsselwörter (z. B. " + example + "), die nicht wie üblich formatiert sind. Soll Sephrasto den Text automatisch anpassen?")
            messageBox.addButton("Ja", QtWidgets.QMessageBox.YesRole)
            messageBox.addButton("Nein", QtWidgets.QMessageBox.RejectRole)
            messageBox.setEscapeButton(QtWidgets.QMessageBox.Close)  
            result = messageBox.exec()
            if result == 0:
                text = boldPattern.sub(lambda m: "<b>" + m.group(0) + "</b>", text)
                text = italicPattern.sub(lambda m: "<i>" + m.group(0) + "</i>", text)
                text = illusionPattern.sub(lambda m: m.group(0).replace("Illusion", "<i>Illusion</i>"), text)
                self.ui.textEdit.setPlainText(text)
                return

        self.talentDialog.done(QtWidgets.QDialog.Accepted)