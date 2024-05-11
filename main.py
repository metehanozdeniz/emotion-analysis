from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from PySide2.QtWidgets import QApplication, QMainWindow
import sys

# Add the path of the ui folder to the system path
sys.path.append('ui') 

# GUI File
from ui_main import Ui_MainWindow

# Prediction Function
from prediction import Prediction

# Application Window
class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # initialize the prediction object for load model and tokenizer and predict text
        self.Predict = Prediction('emotions_detect_model.h5', 'tokenizer.pkl')

        # Load model and tokenizer
        self.Predict.load_model()

        # Button clicked and call the predict function
        self.ui.pushButton.clicked.connect(self.predictText)
    
    # set progress bar value
    def progressBarValue(self, value, widget, color):

        # Progress Bar Stylesheet Template
        styleSheet = """
        QFrame{
        	border-radius: 110px;
        	background-color: qconicalgradient(cx:0.5, cy:0.5, angle:90, stop:{STOP_1} rgba(255, 0, 127, 0), stop:{STOP_2} {COLOR});
        }
        """

        # GET PROGRESS BAR VALUE, CONVERT TO FLOAT AND INVERT VALUES
        # stop works of 1.000 to 0.000
        progress = (100 - value) / 100.0

        # Get new values for stop_1 and stop_2
        stop_1 = str(progress - 0.001)
        stop_2 = str(progress)

        # Fix max value
        if value == 100:
            stop_1 = "1.000"
            stop_2 = "1.000"

        # Set new values to stylesheet
        newStylesheet = styleSheet.replace("{STOP_1}", stop_1).replace("{STOP_2}", stop_2).replace("{COLOR}", color)

        # Apply stylesheet with new values
        widget.setStyleSheet(newStylesheet)
    
    # Set label percentage value
    def labelPercentageValue(self, value, label):

        # Fix value
        if value < 0:
            value = 0
        elif value > 100:
            value = 100
        
        value = int(value)

        htmlText = """<p align="center"><span style=" font-size:50pt;">{VALUE}</span><span style=" font-size:40pt; vertical-align:super;">%</span></p>"""
        label.setText(htmlText.replace("{VALUE}", str(value))) 

    # Predict Text Function
    def predictText(self):

        # Get text from text edit
        text = self.ui.textEdit.toPlainText()

        # Call the predict function
        result, emotions_rates = self.Predict.predict(text)

        # Set result to label
        self.ui.label_13.setVisible(True)
        self.ui.label_13.setText(result)
        
        # Set values to progress bar
        self.progressBarValue(emotions_rates[0][2]*100, self.ui.circularProgressAngry, "rgba(255, 0, 127, 255)")
        self.progressBarValue(emotions_rates[0][0]*100, self.ui.circularProgressFear, "rgba(255, 243, 53, 255)")
        self.progressBarValue(emotions_rates[0][1]*100, self.ui.circularProgressHappy, "rgba(85, 255, 127, 255)")
        self.progressBarValue(emotions_rates[0][3]*100, self.ui.circularProgressSad, "rgba(85, 170, 255, 255)")

        # Set values to label percentage  
        self.labelPercentageValue(emotions_rates[0][2]*100, self.ui.labelPercentageAngry)
        self.labelPercentageValue(emotions_rates[0][0]*100, self.ui.labelPercentageFear)
        self.labelPercentageValue(emotions_rates[0][1]*100, self.ui.labelPercentageHappy)
        self.labelPercentageValue(emotions_rates[0][3]*100, self.ui.labelPercentageSad)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())