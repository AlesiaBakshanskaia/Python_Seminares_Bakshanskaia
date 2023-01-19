# 4. Функция принимает в качестве аргументов строки в формате «Имя Фамилия», возвращает словарь,
# ключи — первые буквы фамилий, значения — словари, реализованные по схеме предыдущего задания.
names = input('Введите имена и фамилии через пробел: ')


def process_string(string):
    ns_list = string.split()
    # отработка случаев введения не всех имен с заглавной буквы
    ns_list = [i.capitalize() for i in ns_list]
    surname_list = [ns_list[i] for i in range(len(ns_list)) if i % 2 != 0]
    name_surname_list = []
    for i in range(0, len(ns_list), 2):
         temp =  ns_list[i] + ' ' + ns_list[i+1]
         name_surname_list.append(temp)
        
    return name_surname_list, surname_list


name_surname_list, surname_list = process_string(names)

# print(name_surname_list)
# print(surname_list)

def dict_names(s_list, n_list ):
    k_list = [s_list[i][0] for i in range(len(s_list))]
    n_dict = {}.fromkeys(k_list, '')
    for k in n_dict:
        temp = []
        for ind in range(len(s_list)):
            if s_list[ind][0] == k:
                temp.append(n_list[ind])
                # сортировка по именам людей с фамилией на одинаковую букву
                temp.sort()
        n_dict[k] = temp
    sorted_n_dict = dict(sorted(n_dict.items()))
    return sorted_n_dict


print(dict_names(surname_list, name_surname_list))

