import sys
import random
from PIL import Image, ImageDraw
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(632, 650)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(210, 580, 221, 41))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 40, 500, 500))
        self.label.setObjectName("label")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "Create"))
        self.label.setText(_translate("Form", "TextLabel"))


class MainWindow(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Генерация')
        self.pushButton.clicked.connect(self.draw)

    def draw(self):
        image = Image.new("RGBA", (500, 500), (0,0,0,0))
        draw = ImageDraw.Draw(image)
        n = random.randint(1,500)
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        draw.ellipse((10, 10, n, n), fill=(0,0,0,0), outline=(r,g,b))
        image.save("test.png", "PNG")
        self.pixmap = QPixmap("test.png")
        self.image = QLabel(self)
        self.label.setPixmap(self.pixmap)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())