import os
import json
patient = input("Enter the full name of patient separated by a space (Ivanov Ivan Ivanovich): ")
patient_lower = patient.lower()
full_name = patient_lower.split()
surname, name, patronymic = full_name
surname = surname.capitalize()
name = name.capitalize()
patronymic = patronymic.capitalize()
patient_folder = os.path.join("patients", f"{surname}_{name}_{patronymic}")
if not os.path.exists(patient_folder):
    print("There is no such patient!")
else:
    json_folder = os.path.join(patient_folder, "card.json")
    if os.path.exists(json_folder):
        with open(json_folder, 'r', encoding='utf-8') as file:
            content = json.dumps(file, indent=4)
            print(content)
    else:
        print('There is no patient card!')
        surname = input('Enter the surname of patient: ').
        name = input('Enter the name of patient: ')
        patronymic =  input('Enter the patronymic of patient: ')
        birth = input('Enter the date of birth of patient (1994-01-10): ')
        sex = input('Enter the sex of patient (M or W): ')
        # Приводим к нужному виду
        surname_true = surname.lower().capitalize()
        name_true = name.lower().capitalize()
        patronymic_true =  patronymic.lower().capitalize()
        sex_true = sex.upper()
        # Создаём словарь
        patient_dict = {
        "Surname": surname_true,
        "Name": name_true,
        "Patronymic": patronymic_true,
        "Date of birth": birth,
        "Sex": sex_true
        }
        # Создаём путь к папке нового пациента
        new_json_folder = os.path.join("patients", f"{surname_true}_{name_true}_{patronymic_true}", "card.json")
        with open(new_json_folder, "w", encoding='utf-8') as f:
            json.dump(patient_dict, f, indent=4) # indent=4 для красивого форматирования
        # Выводим новый файл
        with open(new_json_folder, 'r', encoding='utf-8') as file:
            content = json.dumps(file, indent=4)
            print(content)
            


        
        