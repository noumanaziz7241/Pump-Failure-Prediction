#  Pump Failure Prediction Project Setup Guide

This guide provides the necessary steps to set up and run the Pump Failure Prediction project. Follow the instructions below to ensure a smooth setup process.

## Prerequisites

- Python installed on your system
- `virtualenv` installed
- `VS Code` Installed

## Installation Steps

### Step 1: clone the repository and Install `virtualenv`
To clone repository use the give command:

`git clone https://github.com/noumanaziz7241/Pump-Failure-Prediction.git`

To create a virtual environment for the project, you need to install `virtualenv`:

`pip install virtualenv`

### Step 2: Create a Virtual Environment

Create a virtual environment for your project.


`python -m venv detection_env`

### Step 3: Activate the Virtual Environment
Activate the virtual environment to isolate your project dependencies from your global Python environment.

Windows:

`detection_env\Scripts\activate`

Linux:

`source detection_env/bin/activate`

### Step 4: Install Required Libraries

With the virtual environment activated, install all necessary libraries specified in the requirements.txt file:

`pip install -r requirements.txt`



### Step 5: Run the Project

- It's recommended to use VS Code to run the project.

    To open VS Code in the current folder, open the Command Prompt or Terminal in the project directory and type: `code .`

- Install Jupyter Extension in VS Code (if not already installed):

    If you're using VS Code and haven’t installed the Jupyter extension, search for `Jupyter` in the Extensions view and install it.

- Open the `pump_failure_detection.ipynb.ipynb` file in VS Code.


- Select the Virtual Environment Kernel:

    In Notebook file i.e. `pump_failure_detection.ipynb.ipynb`, their will be an option `Select Kernal` on right side. 
    Choose the interpreter associated with your virtual environment i.e. `detection_env`.

- Run the Notebook:


    Execute each cell sequentially to run the project.

- To Run the predictions on new data you can run the `predictions.py` file using command `python predictions.py` in terminal in linux or cmd in windows. provdie value of each feature as floating point numbers and you will have predictons at the end.

- Alternatively I have created a streamlit app as well to run the project. you can run the app on streamlit using `streamlit run streamlit_app.py`.




