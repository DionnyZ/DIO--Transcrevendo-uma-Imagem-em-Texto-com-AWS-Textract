import json
from pathlib import Path

json_file_path = str(Path(__file__).parent/"response.json")
print(json_file_path)

def extract_materials_from_json(json_file_path):
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    materials_list = []

    for block in data['Blocks']:
        if block['BlockType'] == 'LINE':
            materials_list.append(block['Text'])

    return materials_list

def format_item(item):
    if item.startswith('.'):
        return first_letter_uppercase(' - ' + item[1:])
    return item

def first_letter_uppercase(item):
    for i, caractere in enumerate(item):
        if caractere.isalpha():
            return item[:i] + caractere.upper() + item[i+1:]
    return item

materials_list = extract_materials_from_json(json_file_path)
print("------------------------------")
for item in materials_list:
    print(format_item(item))
print("------------------------------")