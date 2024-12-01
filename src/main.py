import sys
from pathlib import Path
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from PySide6.QtGui import QIcon, QPalette, QColor
from PySide6.QtCore import Qt
from ui.generated_ui import Ui_MainWindow
from ui.settings import Settings

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.settings = Settings()
        
        # Set up theme selector
        self.setup_theme_selector()
        
        # Connect data buttons
        self.ui.load_data_btn.clicked.connect(self.show_load_dialog)
        self.ui.save_data_btn.clicked.connect(self.show_save_dialog)
        
        # Apply initial theme after UI setup
        self.apply_theme(self.settings.get_theme())
        
    def setup_theme_selector(self):
        """
        Initializes the theme selector combobox, sets its initial state,
        and connects its signal to the change_theme method.
        """
        # Set initial theme in the combobox
        current_theme = self.settings.get_theme()
        theme_index = 0 if current_theme == 'light' else 1
        self.ui.theme_selector.setCurrentIndex(theme_index)
        
        # Connect theme selector to theme change method
        self.ui.theme_selector.currentIndexChanged.connect(self.change_theme)
        
    def change_theme(self, index):
        """
        Slot to handle theme changes when the user selects a different theme.
        """
        new_theme = 'light' if index == 0 else 'dark'
        self.settings.set_theme(new_theme)
        self.apply_theme(new_theme)
        
    def apply_theme(self, theme):
        """
        Applies the selected theme to the entire application by setting
        a custom palette based on the theme.
        """
        app = QApplication.instance()
        palette = QPalette()
        groupbox_style = ""

        if theme == 'dark':
            # -------------------
            # Dark Theme Palette
            # -------------------
            palette.setColor(QPalette.Window, QColor(45, 45, 45))
            palette.setColor(QPalette.WindowText, QColor(200, 200, 200))
            palette.setColor(QPalette.Base, QColor(30, 30, 30))
            palette.setColor(QPalette.AlternateBase, QColor(45, 45, 45))
            palette.setColor(QPalette.ToolTipBase, QColor(75, 75, 75))
            palette.setColor(QPalette.ToolTipText, QColor(200, 200, 200))
            palette.setColor(QPalette.Text, QColor(200, 200, 200))
            palette.setColor(QPalette.Button, QColor(55, 55, 55))
            palette.setColor(QPalette.ButtonText, QColor(200, 200, 200))
            palette.setColor(QPalette.BrightText, Qt.red)
            palette.setColor(QPalette.Link, QColor(100, 149, 237))
            palette.setColor(QPalette.Highlight, QColor(100, 149, 237))
            palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
            
            # Dark theme groupbox style
            groupbox_style = """
                QGroupBox {
                    color: #CCCCCC; /* Light gray text for dark mode */
                    margin-top: 2em;
                    padding-top: 0.5em;
                }
                QGroupBox::title {
                    subcontrol-origin: margin;
                    subcontrol-position: top center;
                    margin-top: 0.5em;
                }
            """
        else:
            # -------------------
            # Light Theme Palette
            # -------------------
            palette.setColor(QPalette.Window, QColor(250, 250, 250))  # Softer white
            palette.setColor(QPalette.WindowText, QColor(30, 30, 30))  # Darker gray for better contrast
            palette.setColor(QPalette.Base, QColor(255, 255, 255))  # Pure white
            palette.setColor(QPalette.AlternateBase, QColor(245, 245, 245))  # Very light gray
            palette.setColor(QPalette.ToolTipBase, QColor(255, 255, 220))  # Soft yellow
            palette.setColor(QPalette.ToolTipText, QColor(0, 0, 0))  # Black text
            palette.setColor(QPalette.Text, QColor(50, 50, 50))  # Medium gray for inputs
            palette.setColor(QPalette.Button, QColor(235, 235, 235))  # Light gray for buttons
            palette.setColor(QPalette.ButtonText, QColor(30, 30, 30))  # Darker gray for button text
            palette.setColor(QPalette.BrightText, Qt.red)  # Keep red for alerts
            palette.setColor(QPalette.Link, QColor(0, 102, 204))  # Soft blue for links
            palette.setColor(QPalette.Highlight, QColor(51, 153, 255))  # Light blue
            palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))  # White text on highlight
            
            # Light theme groupbox style
            groupbox_style = """
                QGroupBox {
                    color: #000000; /* Black text for light mode */
                    margin-top: 2em;
                    padding-top: 0.5em;
                }
                QGroupBox::title {
                    subcontrol-origin: margin;
                    subcontrol-position: top center;
                    margin-top: 0.5em;
                }
            """
        
        # Apply the customized palette to the application
        app.setPalette(palette)

        # Apply the palette to price settings
        self.ui.initial_price.setPalette(palette)
        self.ui.volatility.setPalette(palette)
        self.ui.drift.setPalette(palette)
        self.ui.mean_reversion.setPalette(palette)
        self.ui.gap_probability.setPalette(palette)
        self.ui.gap_size.setPalette(palette)

        # Apply the palette to volume settings
        self.ui.base_volume.setPalette(palette)
        self.ui.volume_volatility.setPalette(palette)
        self.ui.volume_trend.setPalette(palette)
        self.ui.spike_probability.setPalette(palette)
        self.ui.spike_multiplier.setPalette(palette)
        
        # Apply the palette to right-hand panel widgets
        self.ui.data_group.setPalette(palette)
        self.ui.exec_group.setPalette(palette)
        self.ui.live_streaming_group.setPalette(palette)
        self.ui.right_scroll.setPalette(palette)

        # Apply the stylesheet to groupbox titles
        self.ui.price_settings_group.setStyleSheet(groupbox_style)
        self.ui.volume_settings_group.setStyleSheet(groupbox_style)
        self.ui.viz_controls_group.setStyleSheet(groupbox_style)
        self.ui.data_group.setStyleSheet(groupbox_style)
        self.ui.exec_group.setStyleSheet(groupbox_style)
        self.ui.live_streaming_group.setStyleSheet(groupbox_style)

    def show_load_dialog(self):
        """Opens a file dialog for loading data files"""
        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Load Data File",
            "",
            "CSV Files (*.csv);;Excel Files (*.xlsx *.xls);;All Files (*.*)"
        )
        if file_name:
            # TODO: Add code to load the selected file
            print(f"Selected file: {file_name}")

    def show_save_dialog(self):
        """Opens a file dialog for saving data files"""
        file_name, _ = QFileDialog.getSaveFileName(
            self,
            "Save Data File",
            "",
            "CSV Files (*.csv);;Excel Files (*.xlsx);;All Files (*.*)"
        )
        if file_name:
            # TODO: Add code to save data to the selected file
            print(f"Saving to file: {file_name}")

    def closeEvent(self, event):
        """
        Handle the close event to perform any necessary cleanup.
        """
        reply = QMessageBox.question(
            self,
            'Quit',
            'Are you sure you want to quit?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())