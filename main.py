import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('gui.ui', self)

        self.predictButton.clicked.connect(self.predict)

    
    def predict(self):
        ''' TODO: Predict output from input arguments ''' 
        pm10 = self.pm10_input.text()
        so2 = self.so2_input.text()
        o3 = self.o3_input.text()
        no2 = self.no2_input.text()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    gui = GUI()
    gui.show()

    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("closing window...")