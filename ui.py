from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtGui import QMovie
import sys
from utils.functions import return_label_nums, load_feeling
form_class = uic.loadUiType("main.ui")[0]



class MyWindow(QMainWindow, form_class):
    def set_label (self, set_label_functions) :
        for code_str in set_label_functions :
            exec(code_str)
        for gif in self.feeling_list: gif.start()

    def modify_page (self) :
        year = self.calendarWidget.yearShown()
        month = self.calendarWidget.monthShown()
        start_date = return_label_nums (year, month)
        response = load_feeling(year, month)
        
        for i in range(42):
            getattr(self, f"label_{i+1}").clear()
            
        
        feelings = [None for _ in range (42)]
        for k in response.keys():
            feelings[int(k)+start_date-2] = response[k] # 시작이 수요일이라면 4에서 시작, label_4부터 계산 시작, 1일이라면 4에 들어가야함.
        
        set_label_functions = []
        for i in range(42) :
            if feelings[i] != None:
                set_label_functions.append(f"self.label_{i+1}.setMovie({self.feeling_str_list[int(feelings[i])]})")
                set_label_functions.append(f"self.label_{i+1}.setScaledContents(True)")
            else:
                set_label_functions.append(f"self.label_{i+1}.setMovie(self.empty)")
                set_label_functions.append(f"self.label_{i+1}.setScaledContents(True)")


        self.set_label(set_label_functions)
            
    def __init__(self):
        super().__init__()
        self.setupUi(self)
            
        self.calendarWidget.currentPageChanged.connect(self.modify_page)

        self.happy = QMovie("./static/기쁨.gif")
        self.scary = QMovie("./static/두려움.gif")
        self.sad = QMovie("./static/슬픔.gif")
        self.exhausted = QMovie("./static/지침.gif")
        self.angry = QMovie("./static/짜증.gif")
        self.hate = QMovie("./static/혐오.gif")
        self.empty = QMovie("./static/empty.gif")
        self.feeling_list = [self.happy, self.scary, self.sad, self.exhausted, self.angry, self.hate, self.empty]
        self.feeling_str_list = ["self.happy", "self.scary", "self.sad", "self.exhausted", "self.angry", "self.hate"]
        self.modify_page()

        

        for gif in self.feeling_list: 
            gif.start()


        
        
def start_App ():
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    app.exec_()

