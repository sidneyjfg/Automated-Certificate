Project Title: Certificate Generator
Description:
This Python script automates the generation of certificates for students based on data provided in an Excel spreadsheet. It extracts information such as student name, course, participation type, dates, and load schedule from the spreadsheet and overlays it onto a certificate template image.

Setup Instructions:
Ensure you have Python installed on your system. This script was developed on Linux Mint.
Create a virtual environment using virtualenv:
virtualenv [your name]
source [your name]/bin/activate
Install required libraries using: pip install pillow openpyxl, which includes the following dependencies:
openpyxl: For reading data from Excel spreadsheets.
Pillow (Python Imaging Library): For image manipulation and drawing text onto images.
Place the Excel spreadsheet containing student data (planilha_alunos.xlsx) and the certificate template image (certificadoDefault.png) in the project directory.
Adjust the font paths in the script if necessary.
Remove all archives located in directiorie 'certificados' before running this program.
Run the script using python main.py.
Usage:
Ensure the Excel spreadsheet (planilha_alunos.xlsx) follows the specified format with columns for course, student name, participation type, dates, and load schedule.
Modify the certificate template image (certificadoDefault.png) as desired.
The generated certificates will be saved in the certificados directory with filenames based on the student name.
Example:

python main.py

Note:
This script assumes a specific layout and format for the input data and the certificate template image. Modify the script accordingly if changes are made to these aspects.
Make sure to have the required font files (AlexBrush-Regular.ttf) available in the project directory.
Credits:
Developed by Sidney
Certificate Template: Automated-Certificate/certificadoDefault . 
By:Sidney Junio.
Feel free to customize this README to fit your project's specifics and add any additional information deemed necessary.