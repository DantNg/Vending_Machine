import sys
# pip install pyqt5
from PyQt5.QtWidgets import QApplication
from MainWindow import MainWindow
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())