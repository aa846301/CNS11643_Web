import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CNS11643_web.settings')
django.setup()
from word_crud.models import WordModels

# with open('Open_Data/MapingTables/Unicode/CNS2UNICODE_Unicode BMP.txt', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f, delimiter='\t')
#     for row in reader:
#         cns, unicode = row
#         character = WordModels(cns_code=cns, unicode_code=unicode)
#         character.save()

def update_char_code_uni(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter='\t')
        for row in reader:
            cns, unicode = row
            character = WordModels(cns_code=cns, unicode_code=unicode)
            character.save()

update_char_code_uni('Open_Data/MapingTables/Unicode/CNS2UNICODE_Unicode 2.txt')          
update_char_code_uni('Open_Data/MapingTables/Unicode/CNS2UNICODE_Unicode 15.txt')
update_char_code_uni('Open_Data/MapingTables/Unicode/CNS2UNICODE_Unicode BMP.txt')
            