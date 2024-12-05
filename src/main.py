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
        self.app = QApplication.instance()
        
        # Apply spinbox styling
        self.setup_spinbox_styling()
        
        # Set up theme selector
        self.setup_theme_selector()
        
        # Connect data buttons
        self.ui.load_data_btn.clicked.connect(self.show_load_dialog)
        self.ui.save_data_btn.clicked.connect(self.show_save_dialog)
        
        # Apply initial theme after UI setup
        self.apply_theme(self.settings.get_theme() == 'dark')

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
        self.apply_theme(index == 1)
        
    def apply_theme(self, is_dark_theme=False):
        """Apply dark or light theme to the application"""
        if is_dark_theme:
            # Dark theme colors
            palette = QPalette()
            palette.setColor(QPalette.Window, QColor(45, 45, 45))
            palette.setColor(QPalette.WindowText, QColor(255, 255, 255))
            palette.setColor(QPalette.Base, QColor(30, 30, 30))
            palette.setColor(QPalette.AlternateBase, QColor(35, 35, 35))
            palette.setColor(QPalette.Text, QColor(255, 255, 255))
            palette.setColor(QPalette.Button, QColor(53, 53, 53))
            palette.setColor(QPalette.ButtonText, QColor(255, 255, 255))
            palette.setColor(QPalette.Link, QColor(100, 149, 237))
            palette.setColor(QPalette.Highlight, QColor(100, 149, 237))
            palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))
            
            # Dark theme styles
            groupbox_style = """
                QLabel, QLabel * {
                    border: none;
                    background: transparent;
                }
                *[class="QLabel"] {
                    border: none;
                    background: transparent;
                }
                QFormLayout QLabel {
                    border: none;
                    background: transparent;
                }
                QGroupBox { 
                    font-weight: bold;
                    margin-top: 10px;
                    background-color: #2d2d2d;
                    border: 1px solid #3d3d3d;
                    border-radius: 6px;
                    padding: 15px;
                }
                QGroupBox::title { 
                    subcontrol-origin: margin;
                    subcontrol-position: top left;
                    background-color: transparent;
                    padding-left: 10px;
                    padding-right: 10px;
                    padding-top: 0px;
                    padding-bottom: 0px;
                    margin-top: px;
                    color: #CCCCCC;
                }
                QFrame, QScrollArea {
                    border: 1px solid #3d3d3d;
                    border-radius: 6px;
                    background: transparent;
                }
                QScrollArea > QWidget > QWidget {
                    background: transparent;
                    border: none;
                }
                QScrollBar:vertical {
                    border: none;
                    background: transparent;
                    width: 4px;
                }
                QScrollBar::handle:vertical {
                    background: #66666600;
                    border-radius: 2px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #666666;
                }
                QScrollBar::handle:vertical:pressed {
                    background: #666666;
                }
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    height: 0px;
                }
                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    background: none;
                }
                QTabWidget::pane {
                    border: 1px solid #3d3d3d;
                    border-radius: 6px;
                    background: transparent;
                }
                QTabWidget::tab-pane {
                    border: none;
                    border-radius: 6px;
                    background: transparent;
                }
                QWidget#leftWidget, QWidget#right_panel {
                    background: transparent;
                    border: none;
                }
            """
        else:
            # Light theme colors
            palette = QPalette()
            palette.setColor(QPalette.Window, QColor(240, 240, 240))
            palette.setColor(QPalette.WindowText, QColor(0, 0, 0))
            palette.setColor(QPalette.Base, QColor(255, 255, 255))
            palette.setColor(QPalette.AlternateBase, QColor(245, 245, 245))
            palette.setColor(QPalette.Text, QColor(0, 0, 0))
            palette.setColor(QPalette.Button, QColor(240, 240, 240))
            palette.setColor(QPalette.ButtonText, QColor(0, 0, 0))
            palette.setColor(QPalette.Link, QColor(0, 102, 204))  # Soft blue for links
            palette.setColor(QPalette.Highlight, QColor(51, 153, 255))  # Light blue
            palette.setColor(QPalette.HighlightedText, QColor(255, 255, 255))  # White text on highlight
            
            # Light theme styles
            groupbox_style = """
                QLabel, QLabel * {
                    border: none;
                    background: transparent;
                }
                *[class="QLabel"] {
                    border: none;
                    background: transparent;
                }
                QFormLayout QLabel {
                    border: none;
                    background: transparent;
                }
                QGroupBox { 
                    font-weight: bold;
                    margin-top: 10px;
                    background-color: #f0f0f0;
                    border: 1px solid #e0e0e0;
                    border-radius: 6px;
                    padding: 15px;
                }
                QGroupBox::title { 
                    subcontrol-origin: margin;
                    subcontrol-position: top left;
                    background-color: transparent;
                    padding-left: 10px;
                    padding-right: 10px;
                    padding-top: 0px;
                    padding-bottom: 0px;
                    margin-top: 0px;
                    margin-bottom: 0px;
                    color: #000000;
                }
                QFrame, QScrollArea {
                    border: 1px solid #CCCCCC;
                    border-radius: 6px;
                    background: transparent;
                }
                QScrollArea > QWidget > QWidget {
                    background: transparent;
                    border: none;
                }
                QScrollBar:vertical {
                    border: none;
                    background: transparent;
                    width: 4px;
                }
                QScrollBar::handle:vertical {
                    background: #CCCCCC00;
                    border-radius: 2px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #CCCCCC;
                }
                QScrollBar::handle:vertical:pressed {
                    background: #CCCCCC;
                }
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    height: 0px;
                }
                QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                    background: none;
                }
                QTabWidget::pane {
                    border: 1px solid #CCCCCC;
                    border-radius: 6px;
                    background: transparent;
                }
                QTabWidget::tab-pane {
                    border: none;
                    border-radius: 6px;
                    background: transparent;
                }
                QWidget#leftWidget, QWidget#right_panel {
                    background: transparent;
                    border: none;
                }
            """

        # Apply palette and styles
        self.app.setPalette(palette)
        
        # Apply styles to group boxes
        group_boxes = [
            self.ui.infinite_data_group,
            self.ui.live_streaming_group,
            self.ui.data_group,
            self.ui.price_settings_group,
            self.ui.volume_settings_group,
            self.ui.viz_controls_group
        ]
        for group_box in group_boxes:
            group_box.setPalette(palette)
            group_box.setStyleSheet(groupbox_style)

        # Apply styles to containers
        self.ui.plot_area.setStyleSheet(groupbox_style)
        self.ui.left_scroll.setStyleSheet(groupbox_style)
        self.ui.right_scroll.setStyleSheet(groupbox_style)
        self.ui.editor_tab_widget.setStyleSheet(groupbox_style)
        
        # Apply styles to spinboxes
        spinboxes = [
            self.ui.initial_price,
            self.ui.volatility,
            self.ui.drift,
            self.ui.mean_reversion,
            self.ui.gap_probability,
            self.ui.gap_size,
            self.ui.base_volume,
            self.ui.volume_volatility,
            self.ui.volume_trend,
            self.ui.spike_probability,
            self.ui.spike_multiplier,
            self.ui.initial_amount,
            self.ui.infinite_initial_amount
        ]
        for spinbox in spinboxes:
            spinbox.setStyleSheet(groupbox_style)   
    # Apply left alignment with offset to numbers inside Spinbox
    def setup_spinbox_styling(self):
        spinboxes = [
            # Price settings spinboxes
            self.ui.initial_price,
            self.ui.volatility,
            self.ui.drift,
            self.ui.mean_reversion,
            self.ui.gap_probability,
            self.ui.gap_size,
            # Volume settings spinboxes
            self.ui.base_volume,
            self.ui.volume_volatility,
            self.ui.volume_trend,
            self.ui.spike_probability,
            self.ui.spike_multiplier,
            # Data amount spinboxes
            self.ui.initial_amount,
            self.ui.infinite_initial_amount
        ]

        spinbox_style = """
            QSpinBox, QDoubleSpinBox {
                padding-left: 5px;
                height: 24px;
            }
        """

        for spinbox in spinboxes:
            # Set text alignment and margins
            spinbox.lineEdit().setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            spinbox.lineEdit().setTextMargins(5, 0, 0, 0)
            # Set fixed height
            spinbox.setMinimumHeight(24)
            spinbox.setMaximumHeight(24)
            spinbox.setStyleSheet(spinbox_style)

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