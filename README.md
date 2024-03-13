# Certificate Generator

## Description
This Python script automates the generation of certificates for students based on data provided in an Excel spreadsheet.

## Setup Instructions
1. Ensure Python is installed on your system (developed on Linux Mint).
2. Create a virtual environment using `virtualenv`:
    ```bash
    virtualenv venv
    source venv/bin/activate
    ```
3. Install required libraries:
    ```bash
    pip install pillow openpyxl
    ```

## Usage
- Place `planilha_alunos.xlsx` and `certificadoDefault.png` in the project directory.
- Run the script:
    ```
      python main.py
    ```

## Example
```bash
python main.py
```

## Note
Assumes specific layout/format for input data and certificate template.
Ensure required font files (AlexBrush-Regular.ttf) are available.
Credits
Developed by [Your Name/Team Name]
