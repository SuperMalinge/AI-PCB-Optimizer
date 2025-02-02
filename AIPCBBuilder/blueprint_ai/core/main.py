import sys
from PyQt6.QtWidgets import QApplication
from blueprint_ai.gui.main_window import MainWindow
from PyQt6.QtCore import QFile, QTextStream

def load_stylesheet(file_path):
    style_file = QFile(file_path)
    style_file.open(QFile.OpenModeFlag.ReadOnly | QFile.OpenModeFlag.Text)
    stream = QTextStream(style_file)
    return stream.readAll()

def main():
    app = QApplication(sys.argv)
    
    # Load and apply stylesheet
    style = load_stylesheet('blueprint_ai/gui/style.qss')
    app.setStyleSheet(style)
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
