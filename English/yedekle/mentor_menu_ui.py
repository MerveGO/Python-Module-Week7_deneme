# Form implementation generated from reading ui file '/Users/yhtyyarannayev/Documents/GitHub/Python-Module-Week7/mentor_menu.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(800, 600)
        MainWindow.setStyleSheet("background-image: url(./assets/zemin-buyuk.jpg);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(parent=self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 240, 771, 341))
        self.tableView.setStyleSheet("QTableView{\n"
"color:black;\n"
"background:white;\n"
"font-weight:bold;\n"
"border-radius:5px\n"
"}")
        self.tableView.setObjectName("tableView")
        self.comboBox = QtWidgets.QComboBox(parent=self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(340, 190, 441, 31))
        self.comboBox.setStyleSheet("QComboBox{\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"background:white;\n"
"color:black\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(260, 80, 291, 31))
        self.label.setStyleSheet("QLabel{\n"
"color:white;\n"
"font-size:36px;\n"
"font-weight:bold;\n"
"background:none\n"
"}\n"
"")
        self.label.setObjectName("label")
        self.pushButton_5 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(10, 190, 91, 31))
        self.pushButton_5.setStyleSheet("QPushButton{\n"
"color:black;\n"
"background:white;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"}\n"
"QPushButton::hover{\n"
"color:white;\n"
"background:#47545a;\n"
"border-radius:10px;\n"
"font-weight:bold\n"
"}")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_4 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(120, 190, 91, 31))
        self.pushButton_4.setStyleSheet("QPushButton{\n"
"color:white;\n"
"background:#47545a;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"color:#47545a;\n"
"background:white;\n"
"border-radius:10px;\n"
"font-weight:bold\n"
"}")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(10, 140, 201, 31))
        self.pushButton_3.setStyleSheet("QPushButton{\n"
"color:black;\n"
"background:white;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"}\n"
"QPushButton::hover{\n"
"color:white;\n"
"background:#47545a;\n"
"border-radius:10px;\n"
"font-weight:bold\n"
"}")
        self.pushButton_3.setObjectName("pushButton_3")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(340, 140, 351, 31))
        self.lineEdit.setStyleSheet("QLineEdit{\n"
"color:black;\n"
"background:white;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"padding:5px;\n"
"}")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(700, 140, 75, 31))
        self.pushButton_2.setStyleSheet("QPushButton{\n"
"color:black;\n"
"background:white;\n"
"border-radius:10px;\n"
"font-weight:bold;\n"
"}\n"
"QPushButton::hover{\n"
"color:white;\n"
"background:#47545a;\n"
"border-radius:10px;\n"
"font-weight:bold\n"
"}")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Vıt Projesinin Tamamına Katılması Uygun Olur"))
        self.comboBox.setItemText(1, _translate("MainWindow", "VIT Projesi ilk IT Eğtimi Al... ya Yönlendirilmesi Uygun Olur"))
        self.comboBox.setItemText(2, _translate("MainWindow", "VIT Projesi İngilizce Eğtimi Al... ya Yönlendirilmesi Uygun Olur"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Vit Pojesi Kapsamında Dir.. Yönlendirilmesi Uygun Olur"))
        self.comboBox.setItemText(4, _translate("MainWindow", "Direkt Bireysel Koçluk İle İşe Yönlendirilmesi Uygun Olur"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Bir Sonraki VIT Projesine Katılması Daha Uygun Olur"))
        self.comboBox.setItemText(6, _translate("MainWindow", "Başka Bir Sektöre Yönlendirilmesi"))
        self.comboBox.setItemText(7, _translate("MainWindow", "Diğer"))
        self.label.setText(_translate("MainWindow", "Mentor Interview"))
        self.pushButton_5.setText(_translate("MainWindow", "TERCİHLER"))
        self.pushButton_4.setText(_translate("MainWindow", "KAPAT"))
        self.pushButton_3.setText(_translate("MainWindow", "TÜM GÖRÜŞMELER"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "ARANACAK METNİ GİRİNİZ"))
        self.pushButton_2.setText(_translate("MainWindow", "BUL"))
