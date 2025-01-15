from PyQt5 import QtCore, QtGui, QtWidgets
from ImageHoverWidget import ImageHoverWidget  # Import the ImageHoverWidget class


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Replacing QLabel with ImageHoverWidget
        self.photo = ImageHoverWidget()  # Use ImageHoverWidget here
        self.photo.setGeometry(QtCore.QRect(0, 0, 801, 411))
        self.photo.image_label.setPixmap(QtGui.QPixmap("band_for_band.jpg"))  # Set initial image
        self.photo.image_label.setScaledContents(True) # I don't know if this is necessary because of setContentsMargins in ImageHoverWidget.py
        self.photo.setObjectName("photo")
        self.photo.setParent(self.centralwidget)  # Add it to the central widget
        
        # Adding buttons
        self.cat = QtWidgets.QPushButton(self.centralwidget)
        self.cat.setGeometry(QtCore.QRect(0, 450, 391, 61))
        self.cat.setObjectName("cat")
        self.dog = QtWidgets.QPushButton(self.centralwidget)
        self.dog.setGeometry(QtCore.QRect(400, 450, 391, 61))
        self.dog.setObjectName("dog")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # Button actions
        self.dog.clicked.connect(self.show_dog)
        self.cat.clicked.connect(self.show_cat)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.cat.setText(_translate("MainWindow", "CAT"))
        self.dog.setText(_translate("MainWindow", "DOG"))

    def show_dog(self):
        self.photo.image_label.setPixmap(QtGui.QPixmap("band_for_band.jpg"))

    def show_cat(self):
        self.photo.image_label.setPixmap(QtGui.QPixmap("freakycat.png"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
