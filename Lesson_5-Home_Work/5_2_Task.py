# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.Входные и выходные данные хранятся в отдельных текстовых файлах.
# Чтение файла
def read_file(name_file):
    from os import path
    import sys
    file_text = name_file
    if not path.exists(file_text):
        print("Файла не существует")
        sys.exit()
    with open (name_file, 'r', encoding="utf-8") as original_text:
        inform = [line.strip() for line in original_text]
    return inform
r_file = read_file('5_2-text_words.txt')
# print(r_file) вывод считанного текста
  
# Кодирование файла
def codding_str(data):
    groups = []
    keys = []
    from itertools import groupby
    for key, group in groupby(data):
        groups.append(list(group))
        keys.append(key)
    # print(groups)
    # print(keys)
    dlina = len(groups[0])
    # print(dlina)
    code = []
    for i in range(len(keys)):
        code.append(str(len(groups[i])))
        code.append(keys[i])
    # print(code)
    codelist = "".join(code)
    return codelist

def codding_text(read_file: list):
    code_text = []
    for i in range(len(read_file)):
        line = ''
        line = read_file[i]
        code_line = ''
        code_line = codding_str(line)
        code_text.append(code_line)
    return code_text
coded_text = codding_text(r_file)
# print(coded_text) вывод закодированного текста

# Запись кодированного файла
with open('5_2-text_code_words.txt', 'w',encoding="utf-8" ) as codding_text:
    for i in range(len(coded_text)):
        codding_text.write(f"{coded_text[i]}\n")

# Чтение кодированного файла

r_coded_file = read_file('5_2-text_code_words.txt')
# print(r_coded_file) вывод считанного закодированного файла

# Раскодирование
def decodding(r_code_file):
    for i in range(len(r_code_file)):
        decode_text = []
        temp_count = ''
        for char in r_code_file[i]:
            if char.isdigit():
                temp_count += char
            elif char.isalpha():
                temp_text = int(temp_count) * char
                temp_count = ''
                decode_text.append(temp_text)
        decode_line = ''.join(decode_text)
        print(decode_line)    

decodding(r_coded_file)