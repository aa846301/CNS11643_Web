import csv
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CNS11643_web.settings')
django.setup()
from word_crud.models import WordModels

# with open('CNS2UNICODE_Unicode BMP.txt', 'r', encoding='utf-8') as f:
#     reader = csv.reader(f, delimiter='\t')
#     for row in reader:
#         cns, unicode = row
#         character = CharMap(cns_code=cns, unicode_code=unicode)

with open('Open_Data/MapingTables/Big5/CNS2BIG5.txt', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        cns, big5 = row
        WordModels.objects.filter(cns_code=cns).update(big5_code=big5)

with open('Open_Data/MapingTables/Big5/CNS2BIG5_Big5E.txt', 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        cns, big5 = row
        qureyset = WordModels.objects.filter(cns_code=cns)
        
        if qureyset.count() > 0:
            qureyset.update(big5_code=big5)
        else:
            character = WordModels(cns_code=cns, big5_code=big5)
            character.save()
    