# Form implementation generated from reading ui file '/Users/yhtyyarannayev/Documents/GitHub/Python-Module-Week7/admin_menu.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("padding:0;\n"
"background-image: url(:/assets/assets/zemin-buyuk.jpg);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Basvurular_2 = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Basvurular_2.setGeometry(QtCore.QRect(320, 350, 141, 31))
        self.Basvurular_2.setAutoFillBackground(False)
        self.Basvurular_2.setStyleSheet("QPushButton{\n"
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
        self.Basvurular_2.setObjectName("Basvurular_2")
        self.Mentor = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Mentor.setGeometry(QtCore.QRect(520, 350, 181, 31))
        self.Mentor.setAutoFillBackground(False)
        self.Mentor.setStyleSheet("QPushButton{\n"
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
        self.Mentor.setObjectName("Mentor")
        self.Adminmenu = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Adminmenu.setGeometry(QtCore.QRect(440, 280, 141, 31))
        self.Adminmenu.setAutoFillBackground(False)
        self.Adminmenu.setStyleSheet("QPushButton{\n"
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
        self.Adminmenu.setObjectName("Adminmenu")
        self.Anamenu = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Anamenu.setGeometry(QtCore.QRect(220, 280, 141, 31))
        self.Anamenu.setAutoFillBackground(False)
        self.Anamenu.setStyleSheet("QPushButton{\n"
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
        self.Anamenu.setObjectName("Anamenu")
        self.Basvurular = QtWidgets.QPushButton(parent=self.centralwidget)
        self.Basvurular.setGeometry(QtCore.QRect(100, 350, 141, 31))
        self.Basvurular.setAutoFillBackground(False)
        self.Basvurular.setStyleSheet("QPushButton{\n"
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
        self.Basvurular.setObjectName("Basvurular")
        self.pushButton = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(610, 500, 91, 31))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton{\n"
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
        self.pushButton.setObjectName("pushButton")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 70, 451, 41))
        self.label_2.setStyleSheet("color:white;\n"
"font-size:36px;\n"
"font-weight:bold;\n"
"background:none")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Basvurular_2.setText(_translate("MainWindow", "MÜLAKATLAR"))
        self.Mentor.setText(_translate("MainWindow", "MENTÖR GÖRÜŞMESİ"))
        self.Adminmenu.setText(_translate("MainWindow", "ADMIN MENÜ"))
        self.Anamenu.setText(_translate("MainWindow", "ANA MENÜ"))
        self.Basvurular.setText(_translate("MainWindow", "BAŞVURULAR"))
        self.pushButton.setText(_translate("MainWindow", "KAPAT"))
        self.label_2.setText(_translate("MainWindow", "ADMIN TERCİHLER MENU"))
