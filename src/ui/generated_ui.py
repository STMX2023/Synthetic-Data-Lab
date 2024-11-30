from PySide6.QtWidgets import (
    QMainWindow, QDialog, QWidget, QVBoxLayout, QHBoxLayout,
    QFormLayout, QLabel, QLineEdit, QPushButton, QSpinBox,
    QComboBox, QGroupBox, QTableView, QDialogButtonBox,
    QTabWidget, QSplitter, QMenuBar, QStatusBar, QToolBar,
    QMenu, QTextEdit, QPlainTextEdit, QFrame
)
from PySide6.QtCore import Qt, QRect, QMetaObject, QCoreApplication, QSize
from PySide6.QtGui import QAction, QFont

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1200, 800)
        MainWindow.setWindowTitle("Synthetic Data Lab")
        
        # Central Widget
        self.centralwidget = QWidget(MainWindow)
        self.main_layout = QVBoxLayout(self.centralwidget)
        
        # Main Horizontal Splitter
        self.main_splitter = QSplitter(Qt.Horizontal)
        
        # Left Panel (Control Panel)
        self.left_panel = QWidget()
        self.left_layout = QVBoxLayout(self.left_panel)
        
        # Data Controls Group
        self.data_group = QGroupBox("Data Controls")
        self.data_layout = QVBoxLayout(self.data_group)
        
        self.load_data_btn = QPushButton("Load Data")
        self.generate_data_btn = QPushButton("Generate Data")
        self.data_layout.addWidget(self.load_data_btn)
        self.data_layout.addWidget(self.generate_data_btn)
        
        # Visualization Controls Group
        self.viz_group = QGroupBox("Visualization")
        self.viz_layout = QVBoxLayout(self.viz_group)
        
        self.plot_type_label = QLabel("Plot Type:")
        self.plot_type_combo = QComboBox()
        self.plot_type_combo.addItems(["Candlestick", "Line", "OHLC"])
        self.update_plot_btn = QPushButton("Update Plot")
        
        self.viz_layout.addWidget(self.plot_type_label)
        self.viz_layout.addWidget(self.plot_type_combo)
        self.viz_layout.addWidget(self.update_plot_btn)
        
        # Backtesting Controls Group
        self.backtest_group = QGroupBox("Backtesting")
        self.backtest_layout = QVBoxLayout(self.backtest_group)
        
        self.period_label = QLabel("Period:")
        self.period_combo = QComboBox()
        self.period_combo.addItems(["1D", "1W", "1M", "3M", "6M", "1Y"])
        self.run_backtest_btn = QPushButton("Run Backtest")
        
        self.backtest_layout.addWidget(self.period_label)
        self.backtest_layout.addWidget(self.period_combo)
        self.backtest_layout.addWidget(self.run_backtest_btn)
        
        # Add groups to left panel
        self.left_layout.addWidget(self.data_group)
        self.left_layout.addWidget(self.viz_group)
        self.left_layout.addWidget(self.backtest_group)
        self.left_layout.addStretch()
        
        # Center Panel (Main Display)
        self.center_panel = QWidget()
        self.center_layout = QVBoxLayout(self.center_panel)
        
        # Plot Area
        self.plot_area = QFrame()
        self.plot_area.setFrameStyle(QFrame.StyledPanel)
        self.plot_area.setMinimumSize(QSize(400, 300))
        
        # Add plot area to center panel
        self.center_layout.addWidget(self.plot_area)
        
        # Right Panel (Control Buttons)
        self.right_panel = QWidget()
        self.right_layout = QVBoxLayout(self.right_panel)
        
        # Control Buttons Group
        self.control_group = QGroupBox("Controls")
        self.control_layout = QVBoxLayout(self.control_group)
        
        # Control Buttons
        self.start_btn = QPushButton("Start")
        self.pause_btn = QPushButton("Pause")
        self.stop_btn = QPushButton("Stop")
        self.reset_btn = QPushButton("Reset")
        
        # Add buttons to control layout
        self.control_layout.addWidget(self.start_btn)
        self.control_layout.addWidget(self.pause_btn)
        self.control_layout.addWidget(self.stop_btn)
        self.control_layout.addWidget(self.reset_btn)
        self.control_layout.addStretch()
        
        # Add control group to right panel
        self.right_layout.addWidget(self.control_group)
        
        # Add panels to main splitter
        self.main_splitter.addWidget(self.left_panel)
        self.main_splitter.addWidget(self.center_panel)
        self.main_splitter.addWidget(self.right_panel)
        
        # Set initial sizes for main splitter (20% left, 60% center, 20% right)
        total_width = MainWindow.width()
        self.main_splitter.setSizes([
            int(total_width * 0.2),
            int(total_width * 0.6),
            int(total_width * 0.2)
        ])
        
        # Bottom Panel (Code Editor and Console)
        self.bottom_panel = QWidget()
        self.bottom_layout = QVBoxLayout(self.bottom_panel)
        
        # Editor Tab Widget
        self.editor_tab_widget = QTabWidget()
        
        # Strategy Editor Tab
        self.strategy_editor_tab = QWidget()
        self.strategy_editor_layout = QVBoxLayout(self.strategy_editor_tab)
        
        # Strategy Controls
        self.strategy_controls = QWidget()
        self.strategy_controls_layout = QHBoxLayout(self.strategy_controls)
        self.strategy_controls_layout.setContentsMargins(0, 0, 0, 0)
        
        # Strategy Buttons
        self.new_strategy_btn = QPushButton("New Strategy")
        self.load_strategy_btn = QPushButton("Load Strategy")
        self.save_strategy_btn = QPushButton("Save Strategy")
        self.run_strategy_btn = QPushButton("Run Strategy")
        
        self.strategy_controls_layout.addWidget(self.new_strategy_btn)
        self.strategy_controls_layout.addWidget(self.load_strategy_btn)
        self.strategy_controls_layout.addWidget(self.save_strategy_btn)
        self.strategy_controls_layout.addWidget(self.run_strategy_btn)
        self.strategy_controls_layout.addStretch()
        
        # Code Editor
        self.code_editor = QPlainTextEdit()
        font = QFont("Monospace")
        font.setFixedPitch(True)
        self.code_editor.setFont(font)
        
        self.strategy_editor_layout.addWidget(self.strategy_controls)
        self.strategy_editor_layout.addWidget(self.code_editor)
        
        # Console Tab
        self.console_tab = QWidget()
        self.console_layout = QVBoxLayout(self.console_tab)
        self.console_output = QPlainTextEdit()
        self.console_output.setReadOnly(True)
        self.console_layout.addWidget(self.console_output)
        
        # Visualization Tab
        self.visualization_tab = QWidget()
        self.visualization_layout = QVBoxLayout(self.visualization_tab)
        self.visualization_output = QPlainTextEdit()
        self.visualization_output.setReadOnly(True)
        self.visualization_output.setPlaceholderText("Visualization output will appear here...")
        self.visualization_layout.addWidget(self.visualization_output)
        
        # Backtesting Tab
        self.backtest_tab = QWidget()
        self.backtest_layout = QVBoxLayout(self.backtest_tab)
        self.backtest_output = QPlainTextEdit()
        self.backtest_output.setReadOnly(True)
        self.backtest_output.setPlaceholderText("Backtesting results will appear here...")
        self.backtest_layout.addWidget(self.backtest_output)
        
        # Add tabs to editor widget
        self.editor_tab_widget.addTab(self.strategy_editor_tab, "Strategy Editor")
        self.editor_tab_widget.addTab(self.console_tab, "Console")
        self.editor_tab_widget.addTab(self.visualization_tab, "Visualization")
        self.editor_tab_widget.addTab(self.backtest_tab, "Backtesting")
        
        # Add editor widget to bottom layout
        self.bottom_layout.addWidget(self.editor_tab_widget)
        
        # Vertical Splitter (Main + Bottom)
        self.vertical_splitter = QSplitter(Qt.Vertical)
        self.vertical_splitter.addWidget(self.main_splitter)
        self.vertical_splitter.addWidget(self.bottom_panel)
        
        # Set initial sizes for vertical splitter (60% top, 40% bottom)
        total_height = MainWindow.height()
        self.vertical_splitter.setSizes([
            int(total_height * 0.6),
            int(total_height * 0.4)
        ])
        
        # Add vertical splitter to main layout
        self.main_layout.addWidget(self.vertical_splitter)
        
        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)
        
        # Menu Bar
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 1200, 24))
        
        self.menu_file = QMenu("File", self.menubar)
        self.menu_view = QMenu("View", self.menubar)
        self.menu_tools = QMenu("Tools", self.menubar)
        
        MainWindow.setMenuBar(self.menubar)
        
        # Status Bar
        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)
        
        # Tool Bar
        self.toolBar = QToolBar(MainWindow)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        
        # Actions
        self.action_open = QAction("Open", MainWindow)
        self.action_save = QAction("Save", MainWindow)
        self.action_exit = QAction("Exit", MainWindow)
        self.action_toggle_console = QAction("Toggle Console", MainWindow)
        self.action_settings = QAction("Settings", MainWindow)
        
        # Add actions to menus
        self.menu_file.addAction(self.action_open)
        self.menu_file.addAction(self.action_save)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.action_exit)
        
        self.menu_view.addAction(self.action_toggle_console)
        self.menu_tools.addAction(self.action_settings)
        
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_view.menuAction())
        self.menubar.addAction(self.menu_tools.menuAction())

class Ui_LoadDataDialog(object):
    def setupUi(self, LoadDataDialog):
        if not LoadDataDialog.objectName():
            LoadDataDialog.setObjectName(u"LoadDataDialog")
        LoadDataDialog.resize(600, 400)
        LoadDataDialog.setWindowTitle("Load Data")
        
        self.verticalLayout = QVBoxLayout(LoadDataDialog)
        
        # File Selection
        self.file_group = QGroupBox("File Selection")
        self.horizontalLayout = QHBoxLayout(self.file_group)
        
        self.file_path = QLineEdit()
        self.browse_btn = QPushButton("Browse")
        
        self.horizontalLayout.addWidget(self.file_path)
        self.horizontalLayout.addWidget(self.browse_btn)
        
        # Import Options
        self.options_group = QGroupBox("Import Options")
        self.formLayout = QFormLayout(self.options_group)
        
        self.delimiter_label = QLabel("Delimiter:")
        self.delimiter_combo = QComboBox()
        self.delimiter_combo.addItems(["Comma (,)", "Tab (\\t)", "Semicolon (;)"])
        
        self.header_label = QLabel("Header Row:")
        self.header_spin = QSpinBox()
        self.header_spin.setValue(0)
        
        self.formLayout.addRow(self.delimiter_label, self.delimiter_combo)
        self.formLayout.addRow(self.header_label, self.header_spin)
        
        # Preview
        self.preview_group = QGroupBox("Data Preview")
        self.preview_layout = QVBoxLayout(self.preview_group)
        self.preview_table = QTableView()
        self.preview_layout.addWidget(self.preview_table)
        
        # Button Box
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        
        # Add widgets to main layout
        self.verticalLayout.addWidget(self.file_group)
        self.verticalLayout.addWidget(self.options_group)
        self.verticalLayout.addWidget(self.preview_group)
        self.verticalLayout.addWidget(self.button_box)
        
        # Connect signals
        self.button_box.accepted.connect(LoadDataDialog.accept)
        self.button_box.rejected.connect(LoadDataDialog.reject)

class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        if not SettingsDialog.objectName():
            SettingsDialog.setObjectName(u"SettingsDialog")
        SettingsDialog.resize(500, 400)
        SettingsDialog.setWindowTitle("Settings")
        
        self.verticalLayout = QVBoxLayout(SettingsDialog)
        
        # Settings Tabs
        self.settings_tabs = QTabWidget()
        self.settings_tabs.setCurrentIndex(0)
        
        # General Tab
        self.general_tab = QWidget()
        self.general_layout = QFormLayout(self.general_tab)
        
        self.theme_label = QLabel("Theme:")
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Light", "Dark"])
        
        self.autosave_label = QLabel("Autosave (minutes):")
        self.autosave_spin = QSpinBox()
        self.autosave_spin.setMinimum(1)
        self.autosave_spin.setMaximum(60)
        self.autosave_spin.setValue(5)
        
        self.general_layout.addRow(self.theme_label, self.theme_combo)
        self.general_layout.addRow(self.autosave_label, self.autosave_spin)
        
        # Data Tab
        self.data_tab = QWidget()
        self.data_layout = QFormLayout(self.data_tab)
        
        self.cache_label = QLabel("Cache Size (MB):")
        self.cache_spin = QSpinBox()
        self.cache_spin.setMaximum(10000)
        self.cache_spin.setValue(1000)
        
        self.precision_label = QLabel("Decimal Precision:")
        self.precision_spin = QSpinBox()
        self.precision_spin.setMinimum(2)
        self.precision_spin.setMaximum(10)
        self.precision_spin.setValue(4)
        
        self.data_layout.addRow(self.cache_label, self.cache_spin)
        self.data_layout.addRow(self.precision_label, self.precision_spin)
        
        # Visualization Tab
        self.visualization_tab = QWidget()
        self.visualization_layout = QFormLayout(self.visualization_tab)
        
        self.chart_theme_label = QLabel("Chart Theme:")
        self.chart_theme_combo = QComboBox()
        self.chart_theme_combo.addItems(["Default", "Dark", "Light"])
        
        self.default_chart_label = QLabel("Default Chart Type:")
        self.default_chart_combo = QComboBox()
        self.default_chart_combo.addItems(["Candlestick", "Line", "OHLC"])
        
        self.visualization_layout.addRow(self.chart_theme_label, self.chart_theme_combo)
        self.visualization_layout.addRow(self.default_chart_label, self.default_chart_combo)
        
        # Add tabs to tab widget
        self.settings_tabs.addTab(self.general_tab, "General")
        self.settings_tabs.addTab(self.data_tab, "Data")
        self.settings_tabs.addTab(self.visualization_tab, "Visualization")
        
        # Button Box
        self.button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        
        # Add widgets to main layout
        self.verticalLayout.addWidget(self.settings_tabs)
        self.verticalLayout.addWidget(self.button_box)
        
        # Connect signals
        self.button_box.accepted.connect(SettingsDialog.accept)
        self.button_box.rejected.connect(SettingsDialog.reject)
