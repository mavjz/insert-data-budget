import openpyxl

def insert_raport(source_path: str):
    wb = openpyxl.load_workbook(source_path)
    sheet = wb['Arkusz1']

insert_raport('../../Wzór excel budżet/Zeszyt1.xlsx')
