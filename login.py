from PyQt5.QtWidgets import QApplication,QLabel,QPushButton,QMainWindow,QWidget,QGridLayout,QVBoxLayout,QLineEdit,QGraphicsDropShadowEffect
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Form")
        self.resize(300,200)
        self.GUI()
        self.componets()
        self.funtionIn()
        
    def GUI(self):
        self.setStyleSheet("""
                           QLabel{
                               font-size:15px;
                               font-family:'Times New Roman';
                           }
                           QLabel#topic{
                               font-size:30px;
                               font-family:'Ink Free';
                           }
                           QPushButton{
                               border:solid 5px solid;
                               border-radius:8px;
                               padding:5px;
                               font-size:10px;
                           }
                           QPushButton#Login{
                               background-color:#71eb34;
                               color:white;
                           }
                           QPushButton#Sign{
                               background-color:#eb8934;
                               color:white;
                           }
                           """)       
    
    def componets(self):
        
        self.topic = QLabel("Login")
        self.topic.setObjectName("topic")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(5)
        shadow.setOffset(2,2)
        shadow.setColor(QColor("red"))
        self.topic.setGraphicsEffect(shadow)
        
        self.name = QLabel("User Name : ")
        self.nameIn = QLineEdit()
        
        self.password = QLabel("Password : ")
        self.passwordIn = QLineEdit()
        
        self.loginBtn = QPushButton("Login")
        self.loginBtn.setObjectName("Login")
        self.signBtn = QPushButton("Sign In")
        self.signBtn.setObjectName("Sign")
        
    def funtionIn(self):
        self.MainBlock = QWidget()
        self.setCentralWidget(self.MainBlock)
        
        vBox = QVBoxLayout()
        vBox2 = QVBoxLayout()
        vBox3 = QVBoxLayout()
        
        grid = QGridLayout()
        grid2 = QGridLayout()
        
        grid.addWidget(self.topic,0,0,1,2,Qt.AlignHCenter)
        
        grid.addWidget(self.name,1,0)
        grid.addWidget(self.nameIn,1,1)
        
        grid.addWidget(self.password,2,0)
        grid.addWidget(self.passwordIn,2,1)

        grid2.addWidget(self.loginBtn,0,0)
        grid2.addWidget(self.signBtn,0,1)
        
        vBox.addLayout(grid)
        vBox2.addLayout(grid2)
        
        vBox3.addLayout(vBox)
        vBox3.addLayout(vBox2)
        
        self.MainBlock.setLayout(vBox3)
    
def main():
    app = QApplication(sys.argv)
    Windows = MainWindow()
    Windows.show()
    sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()