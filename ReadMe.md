# Synthetic Data Lab

A modular platform for algorithmic trading strategy development, featuring synthetic data generation, strategy backtesting, and data visualization. The application provides an embedded Python console and code editor for interactive strategy coding and testing within the app.

---

## Introduction

**Synthetic Data Lab** is a desktop application designed to help traders and developers generate synthetic cryptocurrency market data, develop and test trading algorithms, and visualize results in real-time. Built with a focus on modularity and extensibility, the application leverages powerful Python libraries to provide high performance and a user-friendly interface.

---

## Features

- **Synthetic Data Generation**: Simulate realistic market conditions using statistical models.
- **Embedded Python Console/Code Editor**: Write and execute trading strategies within the application.
- **Efficient Data Handling**: Manage large datasets efficiently using Polars.
- **Real-Time Data Visualization**: Visualize market data and backtesting results with PyQtGraph.
- **Numerical Computation and Machine Learning**: Utilize JAX for high-performance computations and model training.
- **Modular Architecture**: Easily extend and customize the application to suit your needs.
- **User-Friendly Interface**: Design a modern and intuitive interfaces with PySide6 and Qt Designer.

---

## Technology Stack

- **Programming Language**: Python 3.9+
- **Frontend (UI)**: PySide6, Qt Designer
- **Data Handling**: Polars
- **Visualization**: PyQtGraph
- **Numerical Computation**: JAX
- **Trading Logic Execution**: Custom Python modules
- **Embedded Code Editor**: QTextEdit
- **IDE**: Visual Studio Code or PyCharm

---

## File System Structure

The application is structured as follows:

synthetic-data-lab/
├── README.md
├── requirements.txt
├── main.py
├── src/
│   ├── __init**.py
│   ├── ui/
│   │   ├──__init**.py
│   │   ├── main_window.ui
│   │   ├── generated_ui.py
│   │   ├── dialogs/
│   │   │   ├── __init**.py
│   │   │   ├── settings_dialog.ui
│   │   │   ├── load_data_dialog.ui
│   ├── data/
│   │   ├──__init**.py
│   │   ├── data_loader.py
│   │   ├── data_processor.py
│   │   ├── data_generator.py
│   ├── visualization/
│   │   ├── __init**.py
│   │   ├── plot_manager.py
│   │   ├── plot_widgets.py
│   ├── computation/
│   │   ├──__init**.py
│   │   ├── numerical_methods.py
│   │   ├── machine_learning.py
│   ├── trading/
│   │   ├── __init**.py
│   │   ├── strategy_base.py
│   │   ├── strategies/
│   │   │   ├──__init**.py
│   │   │   ├── sample_strategy.py
│   │   ├── backtester.py
│   ├── console/
│   │   ├── __init**.py
│   │   ├── code_editor.py
│   │   ├── console_widget.py
│   ├── utils/
│   │   ├──__init**.py
│   │   ├── helpers.py
│   │   ├── logger.py
│   └── resources/
│       ├── __init**.py
│       ├── icons/
│       │   ├── icon.png
│       ├── styles/
│           ├── style.qss
├── tests/
│   ├──__init**.py
│   ├── test_data_handling.py
│   ├── test_visualization.py
│   ├── test_trading_logic.py
│   ├── test_console.py
└── data/
    ├── sample_data.csv
    └── synthetic_data.csv
