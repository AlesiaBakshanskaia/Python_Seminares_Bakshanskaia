# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён, значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
names = input('Введите имена через пробел: ')

def process_string(string):
    names_list = string.split()
    names_list = [i.capitalize() for i in names_list]#отработка случаев введения не всех имен с заглавной буквы
    names_list.sort()
    return(names_list)

list_names = process_string(names)

# print(names_list)
def dict_names(n_list):
    k_list = [n_list[i][0] for i in range(len(n_list))]
    n_dict = {}.fromkeys(k_list,'')
    for k in n_dict:
        temp = []
        for ind in range(len(n_list)):
            if n_list[ind][0] == k:
                temp.append(n_list[ind])
        n_dict[k] = temp
    return n_dict

print(dict_names(list_names))
