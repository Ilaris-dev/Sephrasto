# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DatenbankEditAbgeleiteterWert.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QSpinBox, QTabWidget, QTextBrowser, QVBoxLayout,
    QWidget)

class Ui_dialog(object):
    def setupUi(self, dialog):
        if not dialog.objectName():
            dialog.setObjectName(u"dialog")
        dialog.resize(526, 617)
        self.verticalLayout_3 = QVBoxLayout(dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.scrollArea = QScrollArea(dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 506, 597))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.teFinalscript = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.teFinalscript.setObjectName(u"teFinalscript")

        self.horizontalLayout_2.addWidget(self.teFinalscript)

        self.buttonPickFinalscript = QPushButton(self.scrollAreaWidgetContents)
        self.buttonPickFinalscript.setObjectName(u"buttonPickFinalscript")

        self.horizontalLayout_2.addWidget(self.buttonPickFinalscript)


        self.gridLayout.addLayout(self.horizontalLayout_2, 8, 2, 1, 1)

        self.leFormel = QLineEdit(self.scrollAreaWidgetContents)
        self.leFormel.setObjectName(u"leFormel")

        self.gridLayout.addWidget(self.leFormel, 6, 2, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.teScript = QPlainTextEdit(self.scrollAreaWidgetContents)
        self.teScript.setObjectName(u"teScript")

        self.horizontalLayout_3.addWidget(self.teScript)

        self.buttonPickScript = QPushButton(self.scrollAreaWidgetContents)
        self.buttonPickScript.setObjectName(u"buttonPickScript")

        self.horizontalLayout_3.addWidget(self.buttonPickScript)


        self.gridLayout.addLayout(self.horizontalLayout_3, 7, 2, 1, 1)

        self.labelBeschreibung = QLabel(self.scrollAreaWidgetContents)
        self.labelBeschreibung.setObjectName(u"labelBeschreibung")

        self.gridLayout.addWidget(self.labelBeschreibung, 5, 1, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.spinSortOrder = QSpinBox(self.scrollAreaWidgetContents)
        self.spinSortOrder.setObjectName(u"spinSortOrder")
        self.spinSortOrder.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spinSortOrder.setMinimum(-999)
        self.spinSortOrder.setMaximum(999)

        self.horizontalLayout.addWidget(self.spinSortOrder)


        self.gridLayout.addLayout(self.horizontalLayout, 4, 2, 1, 1)

        self.leName = QLineEdit(self.scrollAreaWidgetContents)
        self.leName.setObjectName(u"leName")

        self.gridLayout.addWidget(self.leName, 1, 2, 1, 1)

        self.labelShow = QLabel(self.scrollAreaWidgetContents)
        self.labelShow.setObjectName(u"labelShow")

        self.gridLayout.addWidget(self.labelShow, 3, 1, 1, 1)

        self.labelAnzeigeName = QLabel(self.scrollAreaWidgetContents)
        self.labelAnzeigeName.setObjectName(u"labelAnzeigeName")

        self.gridLayout.addWidget(self.labelAnzeigeName, 2, 1, 1, 1)

        self.labelFinalscript = QLabel(self.scrollAreaWidgetContents)
        self.labelFinalscript.setObjectName(u"labelFinalscript")

        self.gridLayout.addWidget(self.labelFinalscript, 8, 1, 1, 1)

        self.labelScript = QLabel(self.scrollAreaWidgetContents)
        self.labelScript.setObjectName(u"labelScript")
        self.labelScript.setMinimumSize(QSize(110, 0))

        self.gridLayout.addWidget(self.labelScript, 7, 1, 1, 1)

        self.leAnzeigeName = QLineEdit(self.scrollAreaWidgetContents)
        self.leAnzeigeName.setObjectName(u"leAnzeigeName")

        self.gridLayout.addWidget(self.leAnzeigeName, 2, 2, 1, 1)

        self.checkShow = QCheckBox(self.scrollAreaWidgetContents)
        self.checkShow.setObjectName(u"checkShow")

        self.gridLayout.addWidget(self.checkShow, 3, 2, 1, 1)

        self.tabWidget = QTabWidget(self.scrollAreaWidgetContents)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_2 = QVBoxLayout(self.tab)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.teBeschreibung = QPlainTextEdit(self.tab)
        self.teBeschreibung.setObjectName(u"teBeschreibung")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teBeschreibung.sizePolicy().hasHeightForWidth())
        self.teBeschreibung.setSizePolicy(sizePolicy)

        self.verticalLayout_2.addWidget(self.teBeschreibung)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout = QVBoxLayout(self.tab_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tbBeschreibung = QTextBrowser(self.tab_2)
        self.tbBeschreibung.setObjectName(u"tbBeschreibung")

        self.verticalLayout.addWidget(self.tbBeschreibung)

        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout.addWidget(self.tabWidget, 5, 2, 1, 1)

        self.labelName = QLabel(self.scrollAreaWidgetContents)
        self.labelName.setObjectName(u"labelName")

        self.gridLayout.addWidget(self.labelName, 1, 1, 1, 1)

        self.labelSortOrder = QLabel(self.scrollAreaWidgetContents)
        self.labelSortOrder.setObjectName(u"labelSortOrder")

        self.gridLayout.addWidget(self.labelSortOrder, 4, 1, 1, 1)

        self.labelFormel = QLabel(self.scrollAreaWidgetContents)
        self.labelFormel.setObjectName(u"labelFormel")

        self.gridLayout.addWidget(self.labelFormel, 6, 1, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_3.addWidget(self.scrollArea)

        QWidget.setTabOrder(self.leName, self.leAnzeigeName)
        QWidget.setTabOrder(self.leAnzeigeName, self.checkShow)
        QWidget.setTabOrder(self.checkShow, self.spinSortOrder)
        QWidget.setTabOrder(self.spinSortOrder, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.teBeschreibung)
        QWidget.setTabOrder(self.teBeschreibung, self.leFormel)
        QWidget.setTabOrder(self.leFormel, self.teScript)
        QWidget.setTabOrder(self.teScript, self.buttonPickScript)
        QWidget.setTabOrder(self.buttonPickScript, self.teFinalscript)
        QWidget.setTabOrder(self.teFinalscript, self.buttonPickFinalscript)
        QWidget.setTabOrder(self.buttonPickFinalscript, self.tbBeschreibung)

        self.retranslateUi(dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(dialog)
    # setupUi

    def retranslateUi(self, dialog):
        dialog.setWindowTitle(QCoreApplication.translate("dialog", u"Sephrasto - Abgeleiteten Wert bearbeiten...", None))
#if QT_CONFIG(tooltip)
        self.teFinalscript.setToolTip(QCoreApplication.translate("dialog", u"<html><head/><body><p>Manche abgeleitete Werte werden nach allen Berechnungen (erneut) modifiziert, beispielsweise indem die BE noch abgezogen wird. In diesem Feld kannst du ein Python-Skript einf\u00fcgen, das den finalen Wert berechnet.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.buttonPickFinalscript.setToolTip(QCoreApplication.translate("dialog", u"Scripteditor \u00f6ffnen", None))
#endif // QT_CONFIG(tooltip)
        self.buttonPickFinalscript.setText(QCoreApplication.translate("dialog", u"+", None))
        self.buttonPickFinalscript.setProperty("class", QCoreApplication.translate("dialog", u"iconSmall", None))
#if QT_CONFIG(tooltip)
        self.leFormel.setToolTip(QCoreApplication.translate("dialog", u"Die Berechnungsformel, die im Charaktereditor neben dem Namen angezeigt werden soll.", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.teScript.setToolTip(QCoreApplication.translate("dialog", u"<html><head/><body><p>In diesem Feld kannst du ein Python-Skript einf\u00fcgen, das den Basiswert berechnet.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.buttonPickScript.setToolTip(QCoreApplication.translate("dialog", u"Scripteditor \u00f6ffnen", None))
#endif // QT_CONFIG(tooltip)
        self.buttonPickScript.setText(QCoreApplication.translate("dialog", u"+", None))
        self.buttonPickScript.setProperty("class", QCoreApplication.translate("dialog", u"iconSmall", None))
        self.labelBeschreibung.setText(QCoreApplication.translate("dialog", u"Beschreibung", None))
#if QT_CONFIG(tooltip)
        self.spinSortOrder.setToolTip(QCoreApplication.translate("dialog", u"<html><head/><body><p>Die Reihenfolge, in der der Wert im Charaktereditor aufgef\u00fchrt werden soll.</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.labelShow.setText(QCoreApplication.translate("dialog", u"Anzeigen", None))
        self.labelAnzeigeName.setText(QCoreApplication.translate("dialog", u"Voller Name", None))
        self.labelFinalscript.setText(QCoreApplication.translate("dialog", u"Finalwert Script", None))
        self.labelScript.setText(QCoreApplication.translate("dialog", u"Script", None))
        self.checkShow.setText(QCoreApplication.translate("dialog", u"Im Attribute-Tab des Charaktereditors zeigen", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("dialog", u"HTML", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("dialog", u"Vorschau", None))
        self.labelName.setText(QCoreApplication.translate("dialog", u"Name", None))
        self.labelSortOrder.setText(QCoreApplication.translate("dialog", u"Sortierreihenfolge", None))
        self.labelFormel.setText(QCoreApplication.translate("dialog", u"Formel", None))
    # retranslateUi

