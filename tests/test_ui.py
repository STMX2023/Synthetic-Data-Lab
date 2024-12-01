#!/usr/bin/env python3

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from src.ui.generated_ui import Ui_MainWindow, Ui_LoadDataDialog, Ui_SettingsDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Connect signals
        # self.ui.load_data_btn.clicked.connect(self.show_load_dialog)
        # self.ui.action_settings.triggered.connect(self.show_settings_dialog)
        # self.ui.action_exit.triggered.connect(self.close)
    
    def show_load_dialog(self):
        dialog = QDialog(self)
        ui = Ui_LoadDataDialog()
        ui.setupUi(dialog)
        dialog.exec()
    
    def show_settings_dialog(self):
        dialog = QDialog(self)
        ui = Ui_SettingsDialog()
        ui.setupUi(dialog)
        dialog.exec()

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
