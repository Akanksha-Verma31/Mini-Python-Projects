# find your vaccination slot using python program
# pip install PyQt5
# pip install PyQtWebEngine
import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Window(QMainWindow):
    def __init__(self):
        super(window,self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        
        # navigation tools
        navigation_bar = QToolBar()
        self.addToolBar(navigation_bar)
        
        back_button = QAction('Backward',self)
        back_button.triggered.connect(self.browser.back)
        navigation_bar.addAction(back_button)
        
        forward_button = QAction('Forward',self)
        forward_button.triggered.connect(self.browser.forward)
        navigation_bar.addAction(forward_button)
        
        refresh_button = QAction('Refresh',self)
        refresh_button.triggered.connect(self.browser.refresh)
        navigation_bar.addAction(refresh_button)
        
        home_button = QAction('Home',self)
        home_button.triggered.connect(self.navigate_home)
        navigation_bar.addAction(home_button)
        
        self.url_bar = QLineEdit
        self.url_bar.returnPressed.connect(self.navigate_url)
        navigation_bar.addWidget(self.url_bar)
        
        self.browser.urlChanged.connect(self.update_url)
        
    def navigate_home(self):
        self.browser.setUrl(QUrl("http://google.com"))
    def update_url(self,q):
        self.url_bar.setText(q.toString())
    def navigate_url(self):
        url= self.url_bar.text()
        self.browser.setUrl(QUrl(url))
        
        
app = QApplication(sys.argv)
QApplication.setApplicationName('Doogle')
main = Window()
app.exec_()
