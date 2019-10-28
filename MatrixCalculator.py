# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MatrixCalculator.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import clipboard
from PyQt5.QtWidgets import QMessageBox

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 254)
        Form.setMaximumSize(QtCore.QSize(1200, 254))
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.MatrixLayout = QtWidgets.QVBoxLayout()
        self.MatrixLayout.setSpacing(6)
        self.MatrixLayout.setObjectName("MatrixLayout")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(298, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.MatrixLayout.addLayout(self.horizontalLayout_7)
        self.MatrixInputLayout = QtWidgets.QVBoxLayout()
        self.MatrixInputLayout.setObjectName("MatrixInputLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.A11 = QtWidgets.QLineEdit(Form)
        self.A11.setMinimumSize(QtCore.QSize(53, 35))
        self.A11.setStyleSheet("QLineEdit{\n"
"        border: 1px solid #F0F0F0;\n"
"        border-bottom: 2px solid #41CD52;\n"
"        font-size: 13px;\n"
"        padding: 5px 5px 5px 5px;\n"
" }\n"
" QLineEdit:hover{\n"
"    border: 1px solid #F0F0F0;\n"
"    border-bottom: 2px solid orange;\n"
" }\n"
"")
        self.A11.setText("")
        self.A11.setObjectName("A11")
        self.horizontalLayout_5.addWidget(self.A11)
        self.A12 = QtWidgets.QLineEdit(Form)
        self.A12.setMinimumSize(QtCore.QSize(53, 35))
        self.A12.setStyleSheet("QLineEdit{\n"
"        border: 1px solid #F0F0F0;\n"
"        border-bottom: 2px solid #41CD52;\n"
"        font-size: 13px;\n"
"padding: 5px 5px 5px 5px;\n"
" }\n"
" QLineEdit:hover{\n"
"    border: 1px solid #F0F0F0;\n"
"    border-bottom: 2px solid orange;\n"
" }\n"
"")
        self.A12.setText("")
        self.A12.setObjectName("A12")
        self.horizontalLayout_5.addWidget(self.A12)
        self.A13 = QtWidgets.QLineEdit(Form)
        self.A13.setMinimumSize(QtCore.QSize(53, 35))
        self.A13.setStyleSheet("QLineEdit{\n"
"        border: 1px solid #F0F0F0;\n"
"        border-bottom: 2px solid #41CD52;\n"
"        font-size: 13px;\n"
"padding: 5px 5px 5px 5px;\n"
" }\n"
" QLineEdit:hover{\n"
"    border: 1px solid #F0F0F0;\n"
"    border-bottom: 2px solid orange;\n"
" }\n"
"")
        self.A13.setText("")
        self.A13.setObjectName("A13")
        self.horizontalLayout_5.addWidget(self.A13)
        self.MatrixInputLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.A21 = QtWidgets.QLineEdit(Form)
        self.A21.setMinimumSize(QtCore.QSize(53, 35))
        self.A21.setStyleSheet("QLineEdit{\n"
"        border: 1px solid #F0F0F0;\n"
"        border-bottom: 2px solid #41CD52;\n"
"        font-size: 13px;\n"
"        padding: 5px 5px 5px 5px;\n"
" }\n"
" QLineEdit:hover{\n"
"    border: 1px solid #F0F0F0;\n"
"    border-bottom: 2px solid orange;\n"
" }\n"
"")
        self.A21.setText("")
        self.A21.setObjectName("A21")
        self.horizontalLayout.addWidget(self.A21)
        self.A22 = QtWidgets.QLineEdit(Form)
        self.A22.setMinimumSize(QtCore.QSize(53, 35))
        self.A22.setStyleSheet("QLineEdit{\n"
"        border: 1px solid #F0F0F0;\n"
"        border-bottom: 2px solid #41CD52;\n"
"        font-size: 13px;\n"
"padding: 5px 5px 5px 5px;\n"
" }\n"
" QLineEdit:hover{\n"
"    border: 1px solid #F0F0F0;\n"
"    border-bottom: 2px solid orange;\n"
" }\n"
"")
        self.A22.setText("")
        self.A22.setObjectName("A22")
        self.horizontalLayout.addWidget(self.A22)
        self.A23 = QtWidgets.QLineEdit(Form)
        self.A23.setMinimumSize(QtCore.QSize(53, 35))
        self.A23.setStyleSheet("QLineEdit{\n"
"        border: 1px solid #F0F0F0;\n"
"        border-bottom: 2px solid #41CD52;\n"
"        font-size: 13px;\n"
"padding: 5px 5px 5px 5px;\n"
" }\n"
" QLineEdit:hover{\n"
"    border: 1px solid #F0F0F0;\n"
"    border-bottom: 2px solid orange;\n"
" }\n"
"")
        self.A23.setText("")
        self.A23.setObjectName("A23")
        self.horizontalLayout.addWidget(self.A23)
        self.MatrixInputLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.A31 = QtWidgets.QLineEdit(Form)
        self.A31.setMinimumSize(QtCore.QSize(53, 35))
        self.A31.setStyleSheet("QLineEdit{\n"
"        border: 1px solid #F0F0F0;\n"
"        border-bottom: 2px solid #41CD52;\n"
"        font-size: 13px;\n"
"padding: 5px 5px 5px 5px;\n"
" }\n"
" QLineEdit:hover{\n"
"    border: 1px solid #F0F0F0;\n"
"    border-bottom: 2px solid orange;\n"
" }\n"
"")
        self.A31.setText("")
        self.A31.setObjectName("A31")
        self.horizontalLayout_4.addWidget(self.A31)
        self.A32 = QtWidgets.QLineEdit(Form)
        self.A32.setMinimumSize(QtCore.QSize(53, 35))
        self.A32.setStyleSheet("QLineEdit{\n"
"        border: 1px solid #F0F0F0;\n"
"        border-bottom: 2px solid #41CD52;\n"
"        font-size: 13px;\n"
"padding: 5px 5px 5px 5px;\n"
" }\n"
" QLineEdit:hover{\n"
"    border: 1px solid #F0F0F0;\n"
"    border-bottom: 2px solid orange;\n"
" }\n"
"")
        self.A32.setText("")
        self.A32.setObjectName("A32")
        self.horizontalLayout_4.addWidget(self.A32)
        self.A33 = QtWidgets.QLineEdit(Form)
        self.A33.setMinimumSize(QtCore.QSize(53, 35))
        self.A33.setStyleSheet("QLineEdit{\n"
"        border: 1px solid #F0F0F0;\n"
"        border-bottom: 2px solid #41CD52;\n"
"        font-size: 13px;\n"
"padding: 5px 5px 5px 5px;\n"
" }\n"
" QLineEdit:hover{\n"
"    border: 1px solid #F0F0F0;\n"
"    border-bottom: 2px solid orange;\n"
" }\n"
"")
        self.A33.setText("")
        self.A33.setObjectName("A33")

        self.horizontalLayout_4.addWidget(self.A33)
        self.MatrixInputLayout.addLayout(self.horizontalLayout_4)
        self.MatrixLayout.addLayout(self.MatrixInputLayout)
        self.ShortResultLayout = QtWidgets.QVBoxLayout()
        self.ShortResultLayout.setObjectName("ShortResultLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.ResultLabel = QtWidgets.QLabel(Form)
        self.ResultLabel.setObjectName("ResultLabel")
        self.horizontalLayout_6.addWidget(self.ResultLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.ShortResultLayout.addLayout(self.horizontalLayout_6)
        self.ShortResult = QtWidgets.QLineEdit(Form)

        self.ShortResult.setStyleSheet("QLineEdit{\n"
"        border: 1px solid #F0F0F0;\n"
"        border-bottom: 2px solid #404040;\n"
"        font-size: 13px;\n"
"        padding: 5px 5px 5px 5px;\n"
" }\n"
" QLineEdit:hover{\n"
"    border: 1px solid #F0F0F0;\n"
"    border-bottom: 2px solid orange;\n"
" }\n"
"")
        self.ShortResult.setText("")
        self.ShortResult.setObjectName("ShortResult")
        self.ShortResultLayout.addWidget(self.ShortResult)
        self.MatrixLayout.addLayout(self.ShortResultLayout)
        self.MatrixAreaButtonsLayout = QtWidgets.QHBoxLayout()
        self.MatrixAreaButtonsLayout.setObjectName("MatrixAreaButtonsLayout")
        self.Calculate = QtWidgets.QPushButton(Form)
        self.Calculate.setObjectName("Calculate")
        self.MatrixAreaButtonsLayout.addWidget(self.Calculate)
        self.ClearMatrix = QtWidgets.QPushButton(Form)
        self.ClearMatrix.setObjectName("ClearMatrix")
        self.MatrixAreaButtonsLayout.addWidget(self.ClearMatrix)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.MatrixAreaButtonsLayout.addItem(spacerItem2)
        self.MatrixLayout.addLayout(self.MatrixAreaButtonsLayout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.MatrixLayout.addItem(spacerItem3)
        self.horizontalLayout_8.addLayout(self.MatrixLayout)
        self.ExpandedResultLayout = QtWidgets.QVBoxLayout()
        self.ExpandedResultLayout.setObjectName("ExpandedResultLayout")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_9.addWidget(self.label_3)
        spacerItem4 = QtWidgets.QSpacerItem(298, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem4)
        self.ExpandedResultLayout.addLayout(self.horizontalLayout_9)
        self.ExpandedResult = QtWidgets.QTextBrowser(Form)
        self.ExpandedResult.setMinimumSize(QtCore.QSize(0, 180))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.ExpandedResult.setFont(font)
        self.ExpandedResult.setMouseTracking(False)
        self.ExpandedResult.setTabletTracking(False)
        self.ExpandedResult.setStatusTip("")
        self.ExpandedResult.setWhatsThis("")
        self.ExpandedResult.setAccessibleName("")
        self.ExpandedResult.setAccessibleDescription("")
        self.ExpandedResult.setStyleSheet("QTextBrowser{\n"
"        border: 1px solid #F0F0F0;\n"
"        border-bottom: 2px solid #404040;\n"
"        font-size: 13px;\n"
" }\n"
" QTextBrowser:hover{\n"
"    border: 1px solid #F0F0F0;\n"
"    border-bottom: 2px solid orange;\n"
" }\n"
"")
        self.ExpandedResult.setOpenLinks(True)
        self.ExpandedResult.setObjectName("ExpandedResult")
        self.ExpandedResultLayout.addWidget(self.ExpandedResult)
        self.ExpandedresultAreaButtonLayout = QtWidgets.QHBoxLayout()
        self.ExpandedresultAreaButtonLayout.setObjectName("ExpandedresultAreaButtonLayout")
        self.CopResult = QtWidgets.QPushButton(Form)
        self.CopResult.setObjectName("CopResult")
        self.ExpandedresultAreaButtonLayout.addWidget(self.CopResult)
        self.ClearExpandedResults = QtWidgets.QPushButton(Form)
        self.ClearExpandedResults.setText("Clear Results")
        self.ClearExpandedResults.setObjectName("ClearExpandedResults")
        self.ExpandedresultAreaButtonLayout.addWidget(self.ClearExpandedResults)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.ExpandedresultAreaButtonLayout.addItem(spacerItem5)
        self.ExpandedResultLayout.addLayout(self.ExpandedresultAreaButtonLayout)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ExpandedResultLayout.addItem(spacerItem6)
        self.horizontalLayout_8.addLayout(self.ExpandedResultLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Matrix Calculator [By Harvindar Singh]"))
        self.label_2.setText(_translate("Form", "Matrix"))
        self.ResultLabel.setText(_translate("Form", "Result"))
        self.Calculate.setText(_translate("Form", "Calculate"))
        self.ClearMatrix.setText(_translate("Form", "Clear Matrix"))
        self.label_3.setText(_translate("Form", "Expanded Result"))
        self.ExpandedResult.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:13px; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.CopResult.setText(_translate("Form", "Copy Result"))

class Calculation:
    def __init__(self, ui_form, form):
        self.ui = ui
        self.Form = form
        self.A11 = 0
        self.A12 = 0
        self.A13 = 0
        self.A21 = 0
        self.A22 = 0
        self.A23 = 0
        self.A31 = 0
        self.A32 = 0
        self.A33 = 0
        self.ExpandedResult = ""
        self.ExpandedResults = ""
        self.connect_ui_buttons()
        self.result_count = 0

    def connect_ui_buttons(self):
        self.ui.Calculate.clicked.connect(self.calculate)
        self.ui.ClearMatrix.clicked.connect(self.clear_matrix)
        self.ui.CopResult.clicked.connect(self.copy_result)
        self.ui.ClearExpandedResults.clicked.connect(self.clear_results)
        self.ui.ShortResult.setDisabled(True)
        self.ui.Calculate.setShortcut("c")
        self.ui.ClearMatrix.setShortcut("ctrl+c")

    def copy_result(self):
        clipboard.copy(self.ExpandedResult)

    def clear_matrix(self):
        self.ui.A11.clear()
        self.ui.A12.clear()
        self.ui.A13.clear()
        self.ui.A21.clear()
        self.ui.A22.clear()
        self.ui.A23.clear()
        self.ui.A31.clear()
        self.ui.A32.clear()
        self.ui.A33.clear()
        self.ui.ShortResult.clear()
        self.ShortResult = ""

    def clear_results(self):
        self.result_count = 0
        self.ui.ExpandedResult.clear()
        self.ExpandedResult = ""

    def error_msg(self, title, message, icon=QMessageBox.Critical):
        msg = QMessageBox()
        msg.setWindowIcon(QtGui.QIcon("Brightgoal.ico"))
        msg.setIcon(icon)
        msg.setWindowTitle(title)
        msg.setText(message)
        msg.exec_()

    def get_values_of_matrix_from_ui(self):
        Value = [self.ui.A11.text(), self.ui.A12.text(), self.ui.A13.text(),
                 self.ui.A21.text(), self.ui.A22.text(), self.ui.A23.text(),
                 self.ui.A31.text(), self.ui.A32.text(), self.ui.A33.text()]

        for e in Value:
            if len(e) == 0:
                self.error_msg("Empty Matrix", "Please Fill Complete Matrix", QMessageBox.Information)
                return False
            if not e.isnumeric():
                if not (e[0] == "-" and e[1::].isnumeric()):
                    self.error_msg("Invalid Values", "Please Fill Valid Values")
                    return False

        self.A11 = int(Value[0])
        self.A12 = int(Value[1])
        self.A13 = int(Value[2])
        self.A21 = int(Value[3])
        self.A22 = int(Value[4])
        self.A23 = int(Value[5])
        self.A31 = int(Value[6])
        self.A32 = int(Value[7])
        self.A33 = int(Value[8])
        return True

    def calculate(self):
        if self.get_values_of_matrix_from_ui():
            self.result_count += 1
            self.ExpandedResult = self.ExpandedResult + "Question "+str(self.result_count)+"\n-------------------------\n"

            self.ExpandedResult = self.ExpandedResult + "[1]: " +str(self.A11)+"(("+str(self.A22)+"*"+str(self.A33)+")-("\
                                  +str(self.A32)+"*"+str(self.A23)+"))"
            if self.A12 < 0:
                self.ExpandedResult = self.ExpandedResult+"+"+str(-self.A12)+"(("+str(self.A21)+"*"+str(self.A33)+")-("\
                                      +str(self.A31)+"*"+str(self.A23)+"))"
            else:
                self.ExpandedResult = self.ExpandedResult + " -" + str(self.A12) + "((" + str(self.A21) + "*" + \
                                      str(self.A33) + ")-(" + str(self.A31) + "*" + str(self.A23) + "))"

            if self.A13 < 0:
                self.ExpandedResult = self.ExpandedResult + " " + str(self.A13) + "((" + str(self.A21) + "*" + \
                                      str(self.A32) + ")-(" + str(self.A31) + "*" + str(self.A22) + "))"
            else:
                self.ExpandedResult = self.ExpandedResult + " +" + str(self.A13) + "((" + str(self.A21) + "*" + \
                                      str(self.A32) + ")-(" + str(self.A31) + "*" + str(self.A22) + "))"
            self.ExpandedResult += "\n\n[2]: "
            #Second Step

            self.ExpandedResult = self.ExpandedResult + str(self.A11) + "(" + str(self.A22 * self.A33)
            result = (self.A32 * self.A23)
            if result < 0:
                self.ExpandedResult = self.ExpandedResult + "+" + str(-result) + ")"
            else:
                self.ExpandedResult = self.ExpandedResult + "-" + str(result) + ")"

            if self.A12 < 0:
                self.ExpandedResult = self.ExpandedResult + " +" + str(-self.A12) + "(" + str(self.A21 * self.A33)
            else:
                self.ExpandedResult = self.ExpandedResult + " -" + str(self.A12) + "(" + str(self.A21 * self.A33)

            result = (self.A31 * self.A23)
            if result < 0:
                self.ExpandedResult = self.ExpandedResult + "+" + str(-result) + ")"
            else:
                self.ExpandedResult = self.ExpandedResult + "-" + str(result) + ")"

            if self.A13 < 0:
                self.ExpandedResult = self.ExpandedResult + " " + str(self.A13) + "(" + str(self.A21 * self.A32)
            else:
                self.ExpandedResult = self.ExpandedResult + " +" + str(self.A13) + "(" + str(self.A21 * self.A32)

            result = (self.A31 * self.A22)
            if result < 0:
                self.ExpandedResult = self.ExpandedResult + "+" + str(-result) + ")"
            else:
                self.ExpandedResult = self.ExpandedResult + "-" + str(result) + ")"

            self.ExpandedResult += "\n\n[3]: "
            # Third Step

            self.ExpandedResult = self.ExpandedResult + str(self.A11) + "(" + str((self.A22 * self.A33)-(self.A32 * self.A23)) + ")"

            if self.A12 < 0:
                self.ExpandedResult = self.ExpandedResult + " +" + str(-self.A12) + "(" + str((self.A21 * self.A33)-(self.A31 * self.A23)) + ")"
            else:
                self.ExpandedResult = self.ExpandedResult + " -" + str(self.A12) + "(" + str((self.A21 * self.A33)-(self.A31 * self.A23)) + ")"

            if self.A13 < 0:
                self.ExpandedResult = self.ExpandedResult + " " + str(self.A13) + "(" + str((self.A21 * self.A32) - (self.A31 * self.A22)) + ")"
            else:
                self.ExpandedResult = self.ExpandedResult + " +" + str(self.A13) + "(" + str((self.A21 * self.A32) - (self.A31 * self.A22)) + ")"

            self.ExpandedResult += "\n\n[4]: "
            # 4th Step

            result1 = (self.A11 * ((self.A22 * self.A33) - (self.A32 * self.A23)))
            self.ExpandedResult += str(result1)

            result2 = ((-self.A12) * ((self.A21 * self.A33) - (self.A31 * self.A23)))
            if result2 < 0:
                self.ExpandedResult += str(result2)
            else:
                self.ExpandedResult = self.ExpandedResult + " +" + str(result2)

            result3 = (self.A13 * ((self.A21 * self.A32) - (self.A31 * self.A22)))
            if result3 < 0:
                self.ExpandedResult += str(result3)
            else:
                self.ExpandedResult = self.ExpandedResult + " +" + str(result3)

            # 5th Step
            self.ExpandedResult += "\n\nFinal Result: "

            result = result1 + result2 + result3
            self.ExpandedResult += str(result)
            self.ExpandedResult += "\n\n"
            self.ShortResult = str(result)

            self.ui.ShortResult.setText(self.ShortResult)
            self.ui.ExpandedResult.setText(self.ExpandedResult)



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    Form.setWindowIcon(QtGui.QIcon("Brightgoal.ico"))
    ui = Ui_Form()
    ui.setupUi(Form)
    Calculate = Calculation(ui, Form)
    Form.show()
    sys.exit(app.exec_())