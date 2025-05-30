from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QMovie
import sys

form_class = uic.loadUiType("main.ui")[0]



app = QApplication(sys.argv)

label = QLabel()

happy = QMovie("./static/기쁨.gif")
scary = QMovie("./static/두려움.gif")
sad = QMovie("./static/슬픔.gif")
exhausted = QMovie("./static/지침.gif")
angry = QMovie("./static/짜증.gif")
hate = QMovie("./static/혐오.gif")

# QLabel에 QMovie 연결
label.setMovie(movie)

# 애니메이션 시작
movie.start()

label.show()
sys.exit(app.exec_())





class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.feelings = []

        self.set_label_functions = []
        for i in range (1, 43) :
            self.set_label_functions.append(f"self.label{i}.setMovie({self.feelings[i]})")


        def set_label (self) :
            for code_str in self.set_label_functions :
                exec(code_str)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()

