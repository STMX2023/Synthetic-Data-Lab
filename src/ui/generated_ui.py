from PySide6.QtWidgets import (
    QMainWindow, QDialog, QWidget, QVBoxLayout, QHBoxLayout,
    QFormLayout, QLabel, QLineEdit, QPushButton, QSpinBox,
    QComboBox, QGroupBox, QTableView, QDialogButtonBox,
    QTabWidget, QSplitter, QMenuBar, QStatusBar, QToolBar,
    QMenu, QTextEdit, QPlainTextEdit, QFrame, QScrollArea,
    QDoubleSpinBox, QMessageBox
)
from PySide6.QtCore import Qt, QRect, QMetaObject, QCoreApplication, QSize, QPoint, QTimer
from PySide6.QtGui import QAction, QFont, QColor, QPalette, QScreen


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        # Get the primary screen and its geometry
        screen = MainWindow.screen()
        screen_geometry = screen.availableGeometry()
        # Set window size to 100% of screen size
        window_width = int(screen_geometry.width() * 1)
        window_height = int(screen_geometry.height() * 1)
        MainWindow.resize(window_width, window_height)
        # Center the window on screen
        center_point = screen_geometry.center()
        MainWindow.setGeometry(
            center_point.x() - window_width // 2,
            center_point.y() - window_height // 2,
            window_width,
            window_height
        )
        MainWindow.setWindowTitle("Synthetic Data Lab")
        
        # Store MainWindow reference
        self.main_window = MainWindow
        
        # Central Widget
        self.centralwidget = QWidget(MainWindow)
        MainWindow.setCentralWidget(self.centralwidget)  # Set central widget immediately
        self.main_layout = QVBoxLayout(self.centralwidget)
        self.main_layout.setContentsMargins(14, 14, 14, 14)  # Add margins around the entire content
        self.main_layout.setSpacing(14)  # Add spacing between main elements
        
        # Main Horizontal Splitter
        self.main_splitter = QSplitter(Qt.Horizontal)
        
        # Left Panel with Scroll Area
        self.left_scroll = QScrollArea()
        self.left_scroll.setWidgetResizable(True)
        self.left_scroll.setObjectName("leftPanel")
        self.left_scroll.setMinimumWidth(270)  # Reduced from default

        # Create widget for scroll area first
        self.left_widget = QWidget()
        self.left_widget.setObjectName("leftWidget")
        self.left_layout = QVBoxLayout(self.left_widget)
        self.left_layout.setContentsMargins(10, 10, 10, 10)  # Reduced margins
        self.left_layout.setSpacing(10)  # Reduced spacing

        # Set the widget before setting scroll bar policies
        self.left_scroll.setWidget(self.left_widget)
        
        # Now set scroll bar policies
        self.left_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.left_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Timer to hide scrollbars after scrolling stops on the left
        self.scroll_timer_left = QTimer()
        self.scroll_timer_left.setInterval(2000)  # 2 seconds
        self.scroll_timer_left.timeout.connect(self.on_scroll_stop_left)

        # Connect scroll events to timer for the left scroll
        self.left_scroll.verticalScrollBar().valueChanged.connect(lambda: (self.on_scroll_left(), self.scroll_timer_left.start()))
        self.left_scroll.horizontalScrollBar().valueChanged.connect(lambda: (self.on_scroll_left(), self.scroll_timer_left.start()))

        # Theme Selector
        self.theme_selector = QComboBox()
            
        self.theme_selector.addItems(["Light", "Dark"])
        self.theme_selector.setMinimumWidth(80)
        self.theme_selector.setMaximumWidth(80)        
        self.theme_selector.setCurrentIndex(0)
        self.left_layout.addWidget(self.theme_selector)

        # Visualization Controls Group
        self.viz_controls_group = QGroupBox("Visualization Controls")
        self.viz_controls_layout = QVBoxLayout(self.viz_controls_group)
        self.viz_controls_layout.setSpacing(8)
        self.viz_controls_layout.setContentsMargins(10, 12, 10, 12)
        
        # Plot Type Section
        self.plot_form_layout = QFormLayout()
        self.plot_type_label = QLabel("Plot Type:")
        self.plot_type_combo = QComboBox()
        self.plot_type_combo.addItems([
            "Candlestick",
            "Line",
            "OHLC",
            "Area",
            "Scatter",
            "Dollar bar",
            "Volume bar"
        ])
        self.plot_type_combo.setMinimumWidth(120)
        self.plot_form_layout.addRow(self.plot_type_label, self.plot_type_combo)
        
        # Period Selection
        self.period_label = QLabel("Period:")
        self.period_combo = QComboBox()
        self.period_combo.addItems([
            "Tick",
            "1 Second",
            "5 Seconds",
            "30 Seconds",
            "1 Minute",
            "5 Minutes",
            "15 Minutes",
            "1 Hour",
            "4 Hours",
            "1 Day"
        ])
        self.period_combo.setMinimumWidth(120)
        self.plot_form_layout.addRow(self.period_label, self.period_combo)
      
        # Add all sections to main layout
        self.viz_controls_layout.addLayout(self.plot_form_layout)
        
        # Add visualization controls to left panel
        self.left_layout.addWidget(self.viz_controls_group)
        self.left_layout.addStretch(0)  # Adjusted stretch factor
        
        # Price Settings Group
        self.price_settings_group = QGroupBox("Price Settings")
        self.price_settings_layout = QFormLayout(self.price_settings_group)
        self.price_settings_layout.setSpacing(8)  # Spacing between elements within groups
        self.price_settings_layout.setContentsMargins(10, 12, 10, 12)  # Increased internal padding
        self.price_settings_layout.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        
        # Price Presets
        self.price_preset_combo = QComboBox()
        self.price_preset_combo.addItems([
            "Custom",
            "Stable Large Cap",
            "Volatile Small Cap",
            "Crypto Bull Market",
            "Crypto Bear Market",
            "Range Bound",
            "Strong Uptrend",
            "Strong Downtrend",
            "High Volatility",
            "Low Volatility",
            "Mean Reverting",
            "Flash Crash",
            "Bubble Formation"
        ])
        self.price_preset_combo.setMinimumWidth(80)
        self.price_preset_combo.setMaximumWidth(150)
        
        # Price parameters with more realistic ranges
        self.initial_price = QDoubleSpinBox()
        self.initial_price.setRange(0.0001, 1000000.00)  # Support crypto to blue chips
        self.initial_price.setValue(100.00)
        self.initial_price.setDecimals(4)
        self.initial_price.setSingleStep(0.1)
        self.initial_price.setMinimumWidth(80)
        self.initial_price.setMaximumWidth(120)
        
        self.volatility = QDoubleSpinBox()
        self.volatility.setRange(0.01, 500.00)  # Support high volatility assets
        self.volatility.setValue(15.00)  # More typical market volatility
        self.volatility.setDecimals(2)
        self.volatility.setSingleStep(0.5)
        self.volatility.setMinimumWidth(80)
        self.volatility.setMaximumWidth(120)
        
        self.drift = QDoubleSpinBox()
        self.drift.setRange(-200.00, 200.00)  # Extended for extreme trends
        self.drift.setValue(0.00)
        self.drift.setDecimals(2)
        self.drift.setSingleStep(0.1)
        self.drift.setMinimumWidth(80)
        self.drift.setMaximumWidth(120)
        
        self.mean_reversion = QDoubleSpinBox()
        self.mean_reversion.setRange(0.00, 1.00)
        self.mean_reversion.setValue(0.15)  # Typical mean reversion strength
        self.mean_reversion.setDecimals(3)
        self.mean_reversion.setSingleStep(0.01)
        self.mean_reversion.setMinimumWidth(80)
        self.mean_reversion.setMaximumWidth(120)
        
        # New: Market Regime
        self.market_regime = QComboBox()
        self.market_regime.addItems([
            "Normal",
            "Bull Market",
            "Bear Market",
            "High Volatility",
            "Low Volatility",
            "Crisis"
        ])
        self.market_regime.setMinimumWidth(80)
        self.market_regime.setMaximumWidth(150)
        
        # New: Price Distribution
        self.price_distribution = QComboBox()
        self.price_distribution.addItems([
            "Normal",
            "Student-t",
            "Skewed Normal",
            "Jump Diffusion",
            "GARCH"
        ])
        self.price_distribution.setMinimumWidth(80)
        self.price_distribution.setMaximumWidth(150)
        
        # New: Gap Settings
        self.gap_probability = QDoubleSpinBox()
        self.gap_probability.setRange(0.00, 1.00)
        self.gap_probability.setValue(0.02)  # 2% chance of gaps
        self.gap_probability.setDecimals(3)
        self.gap_probability.setMinimumWidth(80)
        self.gap_probability.setMaximumWidth(120)
        
        self.gap_size = QDoubleSpinBox()
        self.gap_size.setRange(0.00, 50.00)
        self.gap_size.setValue(2.00)  # 2% average gap size
        self.gap_size.setDecimals(2)
        self.gap_size.setMinimumWidth(80)
        self.gap_size.setMaximumWidth(120)
        
        # Add price parameters to layout
        self.price_settings_layout.addRow("Preset:", self.price_preset_combo)
        self.price_settings_layout.addRow("Initial Price:", self.initial_price)
        self.price_settings_layout.addRow("Volatility (%):", self.volatility)
        self.price_settings_layout.addRow("Drift (%):", self.drift)
        self.price_settings_layout.addRow("Mean Reversion:", self.mean_reversion)
        self.price_settings_layout.addRow("Market Regime:", self.market_regime)
        self.price_settings_layout.addRow("Distribution:", self.price_distribution)
        self.price_settings_layout.addRow("Gap Probability:", self.gap_probability)
        self.price_settings_layout.addRow("Gap Size (%):", self.gap_size)
        
        # Volume Settings Group
        self.volume_settings_group = QGroupBox("Volume Settings")
        self.volume_settings_layout = QFormLayout(self.volume_settings_group)
        self.volume_settings_layout.setSpacing(12)
        self.volume_settings_layout.setContentsMargins(1, 12, 1, 12)

        # Volume Presets
        self.volume_preset_combo = QComboBox()
        self.volume_preset_combo.addItems([
            "Custom",
            "U-Shape Pattern",
            "Institutional Trading",
            "Retail Trading",
            "Opening Hour",
            "Closing Hour",
            "Low Liquidity",
            "High Liquidity",
            "News Impact",
            "Earnings Release",
            "Market Maker"
        ])
        self.volume_preset_combo.setMinimumWidth(80)
        self.volume_preset_combo.setMaximumWidth(150)
        
        # Volume parameters with enhanced ranges
        self.base_volume = QSpinBox()
        self.base_volume.setRange(100, 100000000)  # Support higher volume assets
        self.base_volume.setValue(100000)  # More typical volume
        self.base_volume.setSingleStep(1000)
        self.base_volume.setMinimumWidth(80)
        self.base_volume.setMaximumWidth(120)
        
        self.volume_volatility = QDoubleSpinBox()
        self.volume_volatility.setRange(0.01, 300.00)
        self.volume_volatility.setValue(40.00)  # Typical volume volatility
        self.volume_volatility.setDecimals(2)
        self.volume_volatility.setMinimumWidth(80)
        self.volume_volatility.setMaximumWidth(120)
        
        self.volume_trend = QDoubleSpinBox()
        self.volume_trend.setRange(-200.00, 200.00)
        self.volume_trend.setValue(0.00)
        self.volume_trend.setDecimals(2)
        self.volume_trend.setMinimumWidth(80)
        self.volume_trend.setMaximumWidth(120)
        
        # Enhanced Volume Patterns
        self.volume_pattern = QComboBox()
        self.volume_pattern.addItems([
            "Normal",
            "U-Shape (Day)",
            "W-Shape (Week)",
            "Monthly Cycle",
            "Earnings Season",
            "Custom"
        ])
        self.volume_pattern.setMinimumWidth(80)
        self.volume_pattern.setMaximumWidth(150)
        
        # New: Volume Profile
        self.volume_profile = QComboBox()
        self.volume_profile.addItems([
            "Balanced",
            "Bottom Heavy",
            "Top Heavy",
            "Multi-Modal",
            "Random"
        ])
        self.volume_profile.setMinimumWidth(80)
        self.volume_profile.setMaximumWidth(150)
        
        # New: Volume Spike Settings
        self.spike_probability = QDoubleSpinBox()
        self.spike_probability.setRange(0.00, 1.00)
        self.spike_probability.setValue(0.05)  # 5% chance of volume spikes
        self.spike_probability.setDecimals(3)
        self.spike_probability.setMinimumWidth(80)
        self.spike_probability.setMaximumWidth(120)
        
        self.spike_multiplier = QDoubleSpinBox()
        self.spike_multiplier.setRange(1.00, 100.00)
        self.spike_multiplier.setValue(3.00)  # 3x normal volume
        self.spike_multiplier.setDecimals(2)
        self.spike_multiplier.setMinimumWidth(80)
        self.spike_multiplier.setMaximumWidth(120)
        
        # Add volume parameters to layout
        self.volume_settings_layout.addRow("Preset:", self.volume_preset_combo)
        self.volume_settings_layout.addRow("Base Volume:", self.base_volume)
        self.volume_settings_layout.addRow("Volatility (%):", self.volume_volatility)
        self.volume_settings_layout.addRow("Trend (%):", self.volume_trend)
        self.volume_settings_layout.addRow("Pattern:", self.volume_pattern)
        self.volume_settings_layout.addRow("Profile:", self.volume_profile)
        self.volume_settings_layout.addRow("Spike Probability:", self.spike_probability)
        self.volume_settings_layout.addRow("Spike Multiplier:", self.spike_multiplier)
        
        
        self.left_layout.addWidget(self.price_settings_group)
        
        self.left_layout.addWidget(self.volume_settings_group)
        self.left_layout.addStretch()
        
        # Add scroll area to main splitter
        self.main_splitter.addWidget(self.left_scroll)
        
        # Center Panel (Main Display)
        self.center_panel = QWidget()
        self.center_panel.setObjectName("centerPanel")
        self.center_layout = QVBoxLayout(self.center_panel)
        
        # Plot Area
        self.plot_area = QFrame()
        self.plot_area.setFrameStyle(QFrame.StyledPanel)
        self.plot_area.setMinimumSize(QSize(300, 300))
        
        # Add plot area to center panel
        self.center_layout.addWidget(self.plot_area)
        
        # Add center panel to main splitter
        self.main_splitter.addWidget(self.center_panel)
        
        # Right Panel with Scroll Area
        self.right_scroll = QScrollArea()
        self.right_scroll.setWidgetResizable(True)
        self.right_scroll.setObjectName("rightPanel")
        self.right_scroll.setMinimumWidth(200)
        self.right_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.right_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        # Right Panel widget with scroll area
        self.right_panel = QWidget()
        self.right_panel.setObjectName("right_panel")
        self.right_layout = QVBoxLayout(self.right_panel)
        self.right_layout.setContentsMargins(10, 10, 10, 10)
        self.right_layout.setSpacing(10)  # Increased spacing between groups

        # Infinite Data Run Group
        self.infinite_data_group = QGroupBox("Infinite Data Run")
        self.infinite_data_layout = QVBoxLayout(self.infinite_data_group)
        self.infinite_data_layout.setSpacing(12)  # Spacing between elements within groups
        self.infinite_data_layout.setContentsMargins(1, 10, 1, 10)  # Increased internal padding
        
        self.initial_data_points_label = QLabel("Initial Data Points")
        self.initial_data_points_label.setAlignment(Qt.AlignCenter)
        self.infinite_initial_amount = QDoubleSpinBox()
        self.infinite_initial_amount.setDecimals(0)
        self.infinite_initial_amount.setValue(100000)
        self.infinite_initial_amount.setRange(1000, 1000000000) 
        self.start_btn = QPushButton("Start")
        self.start_btn.setMaximumWidth(120)
        self.pause_btn = QPushButton("Pause")
        self.pause_btn.setMaximumWidth(120)
        self.stop_btn = QPushButton("Stop")
        self.stop_btn.setMaximumWidth(120)
        self.reset_btn = QPushButton("Reset")
        self.reset_btn.setMaximumWidth(120)
        
        self.infinite_data_layout.setAlignment(Qt.AlignCenter)  
        
        self.infinite_data_layout.addWidget(self.initial_data_points_label)
        self.infinite_data_layout.addWidget(self.infinite_initial_amount)
        self.infinite_data_layout.addWidget(self.start_btn)
        self.infinite_data_layout.addWidget(self.pause_btn)
        self.infinite_data_layout.addWidget(self.stop_btn)
        self.infinite_data_layout.addWidget(self.reset_btn)

        # Live streaming Group
        self.live_streaming_group = QGroupBox("Live Streaming")
        
        self.live_streaming_group_layout = QVBoxLayout(self.live_streaming_group)
        self.live_streaming_group_layout.setSpacing(12)  # Spacing between elements within groups
        self.live_streaming_group_layout.setContentsMargins(1, 12, 1, 12)  # Increased internal padding
        
        self.start_data_stream_btn = QPushButton("Start Data Stream")
        self.start_data_stream_btn.setMaximumWidth(150)
        self.start_data_stream_btn.clicked.connect(self.show_stream_connection_dialog)
        self.start_data_stream_btn.setObjectName("startDataStreamBtn")
        self.stop_data_stream_btn = QPushButton("Stop Data Stream")
        self.stop_data_stream_btn.setMaximumWidth(150)
        self.stop_data_stream_btn.setEnabled(False)
        self.live_streaming_group_layout.addWidget(self.start_data_stream_btn)
        self.live_streaming_group_layout.addWidget(self.stop_data_stream_btn)

        # Center button alignment
        self.live_streaming_group_layout.setAlignment(Qt.AlignCenter)

        # Static Data Group
        self.data_group = QGroupBox("Static Data")

        self.data_layout = QVBoxLayout(self.data_group)
        self.data_layout.setSpacing(12)  # Spacing between elements within groups
        self.data_layout.setContentsMargins(1, 12, 1, 12 )  # Increased internal padding
        
        self.load_data_btn = QPushButton("Load Data")
        self.load_data_btn.setMaximumWidth(150)
        self.generate_data_btn = QPushButton("Generate Data")
        self.generate_data_btn.setMaximumWidth(150)
        self.data_points_label = QLabel("Data Points")
        self.data_points_label.setAlignment(Qt.AlignCenter)
        self.initial_amount = QDoubleSpinBox()
        self.initial_amount.setDecimals(0)
        self.initial_amount.setValue(100000)
        self.initial_amount.setRange(10000, 1000000000) 
        self.save_data_btn = QPushButton("Save Data")
        self.save_data_btn.setMaximumWidth(150)

        self.data_layout.addWidget(self.load_data_btn)
        self.data_layout.addWidget(self.generate_data_btn)
        self.data_layout.addWidget(self.data_points_label)
        self.data_layout.addWidget(self.initial_amount)
        self.data_layout.addWidget(self.save_data_btn)

        self.data_layout.setAlignment(Qt.AlignCenter)

        # Add all groups to right panel
        self.right_layout.addWidget(self.infinite_data_group)
        self.right_layout.addWidget(self.live_streaming_group)
        self.right_layout.addWidget(self.data_group)
        self.right_layout.addStretch()
        
        # Set the widget for scroll area
        self.right_scroll.setWidget(self.right_panel)
        
        # Add right scroll box to the main splitter
        self.main_splitter.addWidget(self.right_scroll)

        # Timer to hide scrollbars after scrolling stops on the right
        self.scroll_timer_right = QTimer()
        self.scroll_timer_right.setInterval(2000)  # 2 seconds
        self.scroll_timer_right.timeout.connect(self.on_scroll_stop_right)

        # Connect scroll events to timer for the right scroll
        self.right_scroll.verticalScrollBar().valueChanged.connect(lambda: (self.on_scroll_right(), self.scroll_timer_right.start()))
        self.right_scroll.horizontalScrollBar().valueChanged.connect(lambda: (self.on_scroll_right(), self.scroll_timer_right.start()))

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
        
        # Stats Tab
        self.stats_tab = QWidget()
        self.stats_layout = QVBoxLayout(self.stats_tab)
        
        # Results Window
        self.stats_results = QPlainTextEdit()
        self.stats_results.setReadOnly(True)
        self.stats_results.setPlaceholderText("Strategy statistics and performance metrics will appear here...")
        self.stats_layout.addWidget(self.stats_results)
        
        # Add tabs to editor widget
        self.editor_tab_widget.addTab(self.strategy_editor_tab, "Strategy Editor")
        self.editor_tab_widget.addTab(self.console_tab, "Console")
        self.editor_tab_widget.addTab(self.visualization_tab, "Visualization")
        self.editor_tab_widget.addTab(self.stats_tab, "Stats")
        
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

        # Menu Bar
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setGeometry(QRect(0, 0, 1200, 30))
        
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

        # Connect preset signals
        self.price_preset_combo.currentTextChanged.connect(self.apply_price_preset)
        self.volume_preset_combo.currentTextChanged.connect(self.apply_volume_preset)

    def apply_price_preset(self, preset):
        """Apply predefined price settings based on selected preset"""
        presets = {
            # Market Behavior Presets
            "Strong Uptrend": {
                "initial_price": 25000.0,
                "volatility": 35.0,        # Moderate volatility for trending market
                "drift": 85.0,             # Strong positive drift
                "mean_reversion": 0.05,     # Low mean reversion in trend
                "market_regime": "Bull Market",
                "distribution": "Skewed Normal",
                "gap_probability": 0.03,    # Occasional gaps
                "gap_size": 2.0            # Moderate gaps
            },
            "Strong Downtrend": {
                "initial_price": 25000.0,
                "volatility": 45.0,        # Higher volatility in downtrends
                "drift": -75.0,            # Strong negative drift
                "mean_reversion": 0.05,     # Low mean reversion in trend
                "market_regime": "Bear Market",
                "distribution": "Skewed Normal",
                "gap_probability": 0.05,    # More frequent gaps in downtrends
                "gap_size": 2.5            # Slightly larger gaps
            },
            "High Volatility": {
                "initial_price": 25000.0,
                "volatility": 75.0,        # High volatility
                "drift": 0.0,              # No directional bias
                "mean_reversion": 0.08,     # Low mean reversion
                "market_regime": "High Volatility",
                "distribution": "Student-t",
                "gap_probability": 0.08,    # Frequent gaps
                "gap_size": 3.5            # Large gaps
            },
            "Low Volatility": {
                "initial_price": 25000.0,
                "volatility": 8.0,         # Very low volatility
                "drift": 4.0,              # Slight upward drift
                "mean_reversion": 0.20,     # Higher mean reversion
                "market_regime": "Low Volatility",
                "distribution": "Normal",
                "gap_probability": 0.01,    # Very rare gaps
                "gap_size": 0.5            # Small gaps
            },
            "Mean Reverting": {
                "initial_price": 25000.0,
                "volatility": 25.0,        # Moderate volatility
                "drift": 0.0,              # No drift
                "mean_reversion": 0.40,     # Strong mean reversion
                "market_regime": "Normal",
                "distribution": "Normal",
                "gap_probability": 0.02,    # Rare gaps
                "gap_size": 1.0            # Small gaps
            },
            "Flash Crash": {
                "initial_price": 25000.0,
                "volatility": 150.0,       # Extreme volatility
                "drift": -200.0,           # Severe downward drift
                "mean_reversion": 0.02,     # Almost no mean reversion
                "market_regime": "Crisis",
                "distribution": "Jump Diffusion",
                "gap_probability": 0.25,    # Very frequent gaps
                "gap_size": 8.0            # Very large gaps
            },
            "Bubble Formation": {
                "initial_price": 25000.0,
                "volatility": 65.0,        # High volatility
                "drift": 150.0,            # Extreme upward drift
                "mean_reversion": 0.03,     # Very low mean reversion
                "market_regime": "Bull Market",
                "distribution": "Student-t",
                "gap_probability": 0.10,    # Frequent gaps
                "gap_size": 4.0            # Large gaps
            },
            "Range Bound": {
                "initial_price": 25000.0,
                "volatility": 15.0,        # Low volatility
                "drift": 0.0,              # No drift
                "mean_reversion": 0.35,     # Strong mean reversion
                "market_regime": "Normal",
                "distribution": "Normal",
                "gap_probability": 0.02,    # Rare gaps
                "gap_size": 1.0            # Small gaps
            },
            "News Event": {
                "initial_price": 25000.0,
                "volatility": 55.0,        # High volatility
                "drift": 0.0,              # No directional bias
                "mean_reversion": 0.10,     # Low mean reversion
                "market_regime": "High Volatility",
                "distribution": "Jump Diffusion",
                "gap_probability": 0.15,    # Frequent gaps
                "gap_size": 5.0            # Large gaps
            },
            # Asset Type Presets
            "Stable Large Cap": {
                "initial_price": 150.0,
                "volatility": 12.0,        # Low volatility
                "drift": 8.0,              # Moderate upward drift
                "mean_reversion": 0.15,     # Moderate mean reversion
                "market_regime": "Normal",
                "distribution": "Normal",
                "gap_probability": 0.01,    # Very rare gaps
                "gap_size": 0.8            # Small gaps
            },
            "Volatile Small Cap": {
                "initial_price": 25.0,
                "volatility": 45.0,        # High volatility
                "drift": 15.0,             # Strong growth potential
                "mean_reversion": 0.08,     # Low mean reversion
                "market_regime": "High Volatility",
                "distribution": "Student-t",
                "gap_probability": 0.05,    # Moderate gap frequency
                "gap_size": 3.5            # Large gaps
            }
        }
        
        if preset != "Custom" and preset in presets:
            settings = presets[preset]
            # Block signals to prevent feedback loops
            self.initial_price.blockSignals(True)
            self.volatility.blockSignals(True)
            self.drift.blockSignals(True)
            self.mean_reversion.blockSignals(True)
            self.market_regime.blockSignals(True)
            self.price_distribution.blockSignals(True)
            self.gap_probability.blockSignals(True)
            self.gap_size.blockSignals(True)
            
            try:
                # Apply settings
                self.initial_price.setValue(settings["initial_price"])
                self.volatility.setValue(settings["volatility"])
                self.drift.setValue(settings["drift"])
                self.mean_reversion.setValue(settings["mean_reversion"])
                self.market_regime.setCurrentText(settings["market_regime"])
                self.price_distribution.setCurrentText(settings["distribution"])
                self.gap_probability.setValue(settings["gap_probability"])
                self.gap_size.setValue(settings["gap_size"])
            finally:
                # Always unblock signals
                self.initial_price.blockSignals(False)
                self.volatility.blockSignals(False)
                self.drift.blockSignals(False)
                self.mean_reversion.blockSignals(False)
                self.market_regime.blockSignals(False)
                self.price_distribution.blockSignals(False)
                self.gap_probability.blockSignals(False)
                self.gap_size.blockSignals(False)

    def apply_volume_preset(self, preset):
        """Apply predefined volume settings based on selected preset"""
        presets = {
            # Standard Market Patterns
            "U-Shape Pattern": {
                "base_volume": 1500000,     # Moderate base volume
                "volatility": 35.0,         # Moderate volatility
                "trend": 0.0,               # No trend
                "pattern": "U-Shape (Day)",  # Classic U-shaped pattern
                "profile": "Balanced",       # Even buy/sell distribution
                "spike_probability": 0.03,   # Occasional spikes
                "spike_multiplier": 2.0      # Moderate spike size
            },
            "Institutional Trading": {
                "base_volume": 3500000,     # High base volume
                "volatility": 45.0,         # Moderate-high volatility
                "trend": 10.0,              # Slight upward trend
                "pattern": "Block Trading",  # Large block trades
                "profile": "Top Heavy",      # More buying pressure
                "spike_probability": 0.08,   # Regular block trades
                "spike_multiplier": 4.0      # Large blocks
            },
            "Retail Trading": {
                "base_volume": 800000,      # Lower base volume
                "volatility": 55.0,         # Higher volatility
                "trend": 0.0,               # No clear trend
                "pattern": "Random",         # Random retail flow
                "profile": "Multi-Modal",    # Multiple trading waves
                "spike_probability": 0.05,   # Moderate spikes
                "spike_multiplier": 2.5      # Smaller spikes
            },
            "Opening Hour": {
                "base_volume": 2500000,     # High opening volume
                "volatility": 65.0,         # High volatility
                "trend": 25.0,              # Strong initial surge
                "pattern": "Front Loaded",   # Heavy opening volume
                "profile": "Multi-Modal",    # Multiple opening waves
                "spike_probability": 0.15,   # Frequent spikes
                "spike_multiplier": 3.0      # Significant spikes
            },
            "Closing Hour": {
                "base_volume": 2800000,     # High closing volume
                "volatility": 60.0,         # High volatility
                "trend": 35.0,              # Increasing into close
                "pattern": "Back Loaded",    # Heavy closing volume
                "profile": "Multi-Modal",    # Multiple closing waves
                "spike_probability": 0.12,   # Regular spikes
                "spike_multiplier": 3.5      # Large spikes
            },
            "Low Liquidity": {
                "base_volume": 150000,      # Very low base volume
                "volatility": 85.0,         # Very high volatility
                "trend": -15.0,             # Declining trend
                "pattern": "Random",         # Sporadic trading
                "profile": "Bottom Heavy",   # More selling pressure
                "spike_probability": 0.04,   # Rare but impactful spikes
                "spike_multiplier": 5.0      # Very large spikes when they occur
            },
            "High Liquidity": {
                "base_volume": 5000000,     # Very high base volume
                "volatility": 25.0,         # Lower volatility
                "trend": 5.0,               # Slight upward trend
                "pattern": "U-Shape (Day)",  # Classic pattern
                "profile": "Balanced",       # Even distribution
                "spike_probability": 0.10,   # Regular small spikes
                "spike_multiplier": 1.8      # Small spikes
            },
            "News Impact": {
                "base_volume": 4000000,     # High news-driven volume
                "volatility": 95.0,         # Very high volatility
                "trend": 50.0,              # Strong volume surge
                "pattern": "Random",         # Unpredictable flow
                "profile": "Multi-Modal",    # Multiple volume waves
                "spike_probability": 0.20,   # Very frequent spikes
                "spike_multiplier": 4.5      # Large spikes
            },
            "Earnings Release": {
                "base_volume": 4500000,     # Very high event volume
                "volatility": 100.0,        # Extreme volatility
                "trend": 65.0,              # Strong volume increase
                "pattern": "Front Loaded",   # Heavy initial volume
                "profile": "Multi-Modal",    # Multiple waves
                "spike_probability": 0.25,   # Very frequent spikes
                "spike_multiplier": 5.0      # Very large spikes
            },
            "Market Maker": {
                "base_volume": 2000000,     # Steady base volume
                "volatility": 20.0,         # Low volatility
                "trend": 0.0,               # No trend
                "pattern": "U-Shape (Day)",  # Standard pattern
                "profile": "Balanced",       # Market making balance
                "spike_probability": 0.06,   # Regular small spikes
                "spike_multiplier": 1.5      # Small, controlled spikes
            }
        }
        
        if preset != "Custom" and preset in presets:
            settings = presets[preset]
            # Block signals to prevent feedback loops
            self.base_volume.blockSignals(True)
            self.volume_volatility.blockSignals(True)
            self.volume_trend.blockSignals(True)
            self.volume_pattern.blockSignals(True)
            self.volume_profile.blockSignals(True)
            self.spike_probability.blockSignals(True)
            self.spike_multiplier.blockSignals(True)
            
            try:
                # Apply settings
                self.base_volume.setValue(settings["base_volume"])
                self.volume_volatility.setValue(settings["volatility"])
                self.volume_trend.setValue(settings["trend"])
                self.volume_pattern.setCurrentText(settings["pattern"])
                self.volume_profile.setCurrentText(settings["profile"])
                self.spike_probability.setValue(settings["spike_probability"])
                self.spike_multiplier.setValue(settings["spike_multiplier"])
            finally:
                # Always unblock signals
                self.base_volume.blockSignals(False)
                self.volume_volatility.blockSignals(False)
                self.volume_trend.blockSignals(False)
                self.volume_pattern.blockSignals(False)
                self.volume_profile.blockSignals(False)
                self.spike_probability.blockSignals(False)
                self.spike_multiplier.blockSignals(False)

    def show_stream_connection_dialog(self):
        dialog = StreamConnectionDialog(self.main_window)
        if dialog.exec_() == QDialog.Accepted:
            # Connection was successful
            self.start_data_stream_btn.setEnabled(False)
            self.start_data_stream_btn.setText("Connected")
            # Enable the stop button
            self.stop_data_stream_btn.setEnabled(True)

    def on_scroll_right(self):
        self.right_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.right_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def on_scroll_stop_right(self):
        self.right_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.right_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def on_scroll_left(self):
        self.left_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.left_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def on_scroll_stop_left(self):
        self.left_scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.left_scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


class StreamConnectionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Stream Connection Settings")
        self.setModal(True)
        self.resize(400, 300)

        # Create layout
        layout = QVBoxLayout(self)
        form_layout = QFormLayout()

        # Create input fields
        self.exchange_combo = QComboBox()
        self.exchange_combo.addItems(["Binance", "Coinbase", "Kraken", "Bitfinex"])
        
        self.api_key = QLineEdit()
        self.api_key.setEchoMode(QLineEdit.Password)
        self.api_secret = QLineEdit()
        self.api_secret.setEchoMode(QLineEdit.Password)
        
        self.symbol_input = QLineEdit()
        self.symbol_input.setPlaceholderText("e.g., BTC/USD")
        
        # Add fields to form layout
        form_layout.addRow("Exchange:", self.exchange_combo)
        form_layout.addRow("API Key:", self.api_key)
        form_layout.addRow("API Secret:", self.api_secret)
        form_layout.addRow("Trading Pair:", self.symbol_input)
        
        # Add form to main layout
        layout.addLayout(form_layout)
        
        # Status label
        self.status_label = QLabel("")
        self.status_label.setStyleSheet("QLabel { color: red; }")
        layout.addWidget(self.status_label)
        
        # Buttons
        button_layout = QHBoxLayout()
        self.connect_button = QPushButton("Connect")
        self.connect_button.clicked.connect(self.try_connect)
        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(self.connect_button)
        button_layout.addWidget(self.cancel_button)
        layout.addLayout(button_layout)

    def try_connect(self):
        # Validate inputs
        if not self.api_key.text() or not self.api_secret.text() or not self.symbol_input.text():
            self.status_label.setText("Please fill in all fields")
            return
            
        # Here you would implement the actual connection logic
        # For now, we'll just show a success message
        self.status_label.setStyleSheet("QLabel { color: green; }")
        self.status_label.setText("Connected successfully!")
        self.accept()


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
