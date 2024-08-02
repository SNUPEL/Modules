# 📊 JSSP Simulator

|                  **Main Developer**                  |       
|:----------------------------------------------------:| 
| Baek Jiwon [(Github)](https://github.com/Jiwon-Baek) | 
|                  🧑‍💻 AI-Developer                  | 

## 💁‍♂️ How does it work?

- permutation encoding recommended

# 💡 Execution
1. config.py에서 여러가지 시뮬레이션 관련 변수 설정
2. main.py 실행

# 📂 Executable Files

1. main.py

# 📂 Module Descriptions

## Root Directory

### `.gitignore`
Specifies files and directories that should be ignored by Git version control.

### `main.py`
The main entry point for the application. This script is responsible for initializing the environment and executing the core logic of the project.

### `Readme.md`
This file. Provides an overview and documentation for the project.

### `requirements.yaml`
Contains a list of dependencies and configurations required for the project, typically used for environment setup.

### `showdirectory.py`
A script for displaying the directory structure of the project.

### `utils.py`
Utility functions and helpers used throughout the project. This module may include functions for common tasks like data manipulation and file operations.

## Config Directory

### `Run_Config.py`
Contains configuration settings for running the project. This script defines various parameters and settings needed for execution.

## Environment Directory

### `monitor.py`
Defines the `Monitor` class, which is responsible for recording and saving events and statuses throughout the simulation process.

### `part.py`
Defines the `Job` class, which represents a job or part within the simulation. It includes details about the job's type, ID, and operations.

### `process.py`
Defines the `Process` class, which simulates a processing unit within the system. This class handles the processing of jobs and scheduling.

### `resource.py`
Defines resources used in the simulation, such as machines or other equipment. It may include classes and methods for managing resource availability and utilization.

### `sink.py`
Defines the `Sink` class, which collects and records completed jobs or parts. It tracks the number of parts processed and records their completion.

### `source.py`
Defines the `Source` class, which generates new jobs or parts and routes them to the appropriate processes. It manages the creation and distribution of jobs based on defined inter-arrival times.

## Postprocessing Directory

### `postprocessing.py`
Contains functions and classes for post-processing the results of the simulation. This may include data analysis, result aggregation, and report generation.

## Visualization Directory

### `Gantt.py`
Provides functionality for generating Gantt charts to visualize the scheduling and processing of jobs within the simulation.

### `GUI.py`
Contains code for graphical user interface elements related to the simulation. This may include tools for user interaction and visualization.

## Result Directory

This directory is intended to store the results of the simulation, such as output files, logs, or analysis results. It may be populated dynamically during or after the execution of the simulation.

# Project Directory Structure

```plaintext
JSSP
│  .gitignore
│  main.py
│  Readme.md
│  requirements.yaml
│  showdirectory.py
│  utils.py
│  
├─Config
│  └─ Run_Config.py
│
├─Data
│  │  DataGenerator.py
│  │  Inspection.ipynb
│  │  statistics.py
│  │
│  ├─Adams
│  │  ├─abz5
│  │  │      abz5.py
│  │  │      abz5.txt
│  │  │      abz5_solutions.txt
│  │  │      MIO.ipynb
│  │  │
│  │  ├─abz6
│  │  │  │  abz6.py
│  │  │  │  abz6.txt
│  │  │  └─ abz6_solutions.txt
│  │  │
│  │  ├─abz7
│  │  │      abz7.py
│  │  │      abz7.txt
│  │  │      abz7_test.py
│  │  │
│  │  ├─abz8
│  │  │      abz8.py
│  │  │      abz8.txt
│  │  │      abz8_test.py
│  │  │
│  │  └─abz9
│  │          abz9.py
│  │          abz9.txt
│  │          abz9_test.py
│  │
│  ├─Dataset
│  │      Dataset.py
│  │      test_10015.txt
│  │      test_1515.txt
│  │      test_2020.txt
│  │      test_3030.txt
│  │      test_4040.txt
│  │      test_43.txt
│  │      test_44.txt
│  │      test_5020.txt
│  │
│  ├─FT
│  │  ├─ft06
│  │  │      ft06.py
│  │  │      ft06.txt
│  │  │      ft06_solutions.txt
│  │  │
│  │  ├─ft10
│  │  │      ft10.py
│  │  │      ft10.txt
│  │  │      ft10_solutions.txt
│  │  │
│  │  └─ft20
│  │          ft20.py
│  │          ft20.txt
│  │          ft20_solutions.txt
│  │
│  └─Taillard
│      └─ta01
│              ta01.py
│              ta01.txt
│              ta01_solutions.txt
│
├─environment
│  │  monitor.py
│  │  part.py
│  │  process.py
│  │  resource.py
│  │  sink.py
│  └─ source.py
│
├─postprocessing
│  └─ postprocessing.py
│
├─result
└─visualization
   │  Gantt.py
   └─ GUI.py
