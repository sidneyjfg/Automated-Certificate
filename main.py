import openpyxl as xl
from PIL import Image, ImageDraw, ImageFont


workbook = xl.load_workbook('planilha_alunos.xlsx')
sheet_alunos = workbook['Sheet1']

for index, row in enumerate(sheet_alunos.iter_rows(min_row=2, max_row=2)):

    course = row[0].value #curso
    student = row[1].value #aluno
    type_participation = row[2].value #tipo de participação
    start_date = row[3].value #data inicio
    final_date = row[4].value #data final
    load_schedule = row[5].value #carga horária
    emission_date = row[6].value #data de emissão

    #transfer images for sheet
    font_name = ImageFont.truetype('./AlexBrush-Regular.ttf',90)
    font_course = ImageFont.truetype('./AlexBrush-Regular.ttf',50)
    font_schedule_and_Date = ImageFont.truetype('./AlexBrush-Regular.ttf',40)
    image = Image.open('./certificadoDefault.png')
    draw = ImageDraw.Draw(image)
    draw.text((650,300), student, fill='blue', font=font_name)
    draw.text((475,500), course, fill='blue', font=font_course)
    draw.text((610,590), str(load_schedule) + ' Horas', fill='blue', font=font_schedule_and_Date)
    draw.text((640,690), str(emission_date), fill='blue', font=font_schedule_and_Date)
    draw.text((460,1033), str(start_date), fill='blue', font=font_schedule_and_Date)
    draw.text((450,1135), str(final_date), fill='blue', font=font_schedule_and_Date)
    
    
    image.save(f'./certificados/{index+1} {student}.png')