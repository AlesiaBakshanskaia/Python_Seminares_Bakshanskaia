
load_file = open("Poly.txt", "r", encoding="utf-8")
inform = [line.strip() for line in load_file]
print(inform)
load_file.close()

load_file2 = open("Poly2.txt", "r", encoding="utf-8")
inform2 = [line.strip() for line in load_file2]
print(inform2)
load_file.close()

if len(inform) == len(inform2):
    for i in range(0, len(inform)):
        new_str = ""
        new_str = inform[i].rstrip(" =0")
        new_str += " + "
        new_str += inform2[i]
        with open("Poly3.txt", "a", encoding="utf-8") as file3:
            file3.write(f"{new_str}\n") 
else:
    print("Содержимое файлов не совпадает")    
