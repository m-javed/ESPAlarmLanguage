import csv
import re

import openpyxl


def clean_textkeys():
    fields = ("$Textkey", "$Subkey", "$English", "$Chinese")
    out_array = []

    try:
        with open('Alarm Tags/emosWeb.AlarmTexts.Plc.DS_LamTexts_TAB.csv', 'r', encoding='UTF-8') as file:
            dt = csv.DictReader(file, delimiter=';', fieldnames=fields)
            for row in dt:
                key = row[fields[0]].split('_')[-1]
                en_text = re.sub("\d{4}", key, row[fields[2]])
                zh_text = re.sub("\d{4}", key, row[fields[3]])
                out_array.append({fields[0]: f'"{row[fields[0]]}"', fields[1]: f'"{row[fields[1]]}"',
                                  fields[2]: f'"{en_text}"', fields[3]: f'"{zh_text}"'})
    except FileNotFoundError:
        print('file not found')

    try:
        with open('Alarm Tags/out.csv', 'w', newline="", encoding='UTF-8') as file:
            headers = fields
            filters = csv.DictWriter(file, delimiter=';', fieldnames=headers)
            filters.writerow(dict((heads, heads) for heads in headers))
            filters.writerows(out_array)
    except FileNotFoundError:
        print('save file not found')


def extract_tags_and_texts(filename):
    tags_fields = ("$IoNode", "$IoItem", "$Textkey", "$Class", "$Groupkey", "$Location", "$Active", "$Priority",
                   "$LogEnabled", "$PlantID", "$PlantType", "$EquipmentID", "$Devicename", "Cfg_Inst_Structure")
    texts_fields = ("$Textkey", "$Subkey", "$English", "$German", "$French", "$Spanish", "$Portuguese", "$Chinese",
                    "$Local1", "$Local2", "$Unicode1", "$Unicode2")
    tags_out_array = []
    texts_out_array = []
    ptag = ''
    io_node = "ESP-Core"
    tag_class = '01'        # 01=equipment fault, 02=equipment warning 03=emergency stop
    group_key = 'ESP-Core'
    plant_id = 'ESP-Core'
    tag_count = 0

    esalarms_sheet = openpyxl.load_workbook(filename)['Sheet1']
    rows_count = esalarms_sheet.max_row
    for row in range(2, rows_count):
        datatype = esalarms_sheet[f'B{row}'].value
        if datatype.startswith('Str'):
            ptag = esalarms_sheet[f'A{row}'].value      # parent tag
        elif datatype == 'Bool':
            ctag = esalarms_sheet[f'A{row}'].value      # child tag
            comment = esalarms_sheet[f'K{row}'].value  # alarm comment
            if ctag:
                tag_count += 1
            tag = f'.ESAlarms.{ptag}.{ctag}'
            text_key = f'T02_PLCALS_{tag_count:04d}'
            if ptag.startswith('PS') or ptag.startswith('SL'):
                comment = f'{ptag} {comment}'
            if ctag.startswith('Flt'):
                tag_class = "01"
                comment = f'HW: {comment}'
            elif ctag.startswith('EStop'):
                tag_class = "03"
                comment = f'SAFETY: {comment}'

            en_text = f'ID_{tag_count:04d} {comment}'
            tags_out_array.append({"$IoNode": io_node, "$IoItem": tag, "$Textkey": text_key, "$Class": tag_class,
                                   "$Groupkey": group_key, "$Location": "", "$Active": "1", "$Priority": "50",
                                   "$LogEnabled": "1", "$PlantID": plant_id, "$PlantType": " ", "$EquipmentID": "PLC",
                                   "$Devicename": "", "Cfg_Inst_Structure": "0"})
            texts_out_array.append({"$Textkey": text_key, "$Subkey": "message", "$English": en_text, "$German":"",
                                    "$French": "", "$Spanish": "", "$Portuguese": "", "$Chinese": "", "$Local1": "",
                                    "$Local2": "", "$Unicode1": "", "$Unicode2": ""})

    try:
        with open('CSVExport/AlmTags.csv', 'w', newline="", encoding='UTF-8') as file:
            headers = tags_fields
            filters = csv.DictWriter(file, delimiter=';', fieldnames=headers, quoting=csv.QUOTE_NONNUMERIC)
            filters.writerow(dict((heads, heads) for heads in headers))
            filters.writerows(tags_out_array)
            print('Alarm Tags exported to CSVExport/AlmTags.csv file')
    except FileNotFoundError:
        print('Error saving file. file not found')

    try:
        with open('CSVExport/AlmTexts.csv', 'w', newline="", encoding='UTF-8') as file:
            headers = texts_fields
            filters = csv.DictWriter(file, delimiter=';', fieldnames=headers, quoting=csv.QUOTE_NONNUMERIC)
            filters.writerow(dict((heads, heads) for heads in headers))
            filters.writerows(texts_out_array)
            print('Alarm Texts exported to CSVExport/AlmTexts.csv file')
    except FileNotFoundError:
        print('Error saving file. file not found')

