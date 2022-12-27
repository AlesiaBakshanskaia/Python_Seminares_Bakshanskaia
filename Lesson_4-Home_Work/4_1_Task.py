# Вычислить число c заданной точностью d
number = float(input("Enter a real number: "))
accur = float(input("Enter the required accuracy '0.0001': "))
if accur > 1:
    print("You enter the wrong accuracy")
elif accur == 1:
    accur_numb = round(number)
    print(accur_numb)
else:
    pow_accur = 0
    while accur < 1:
        accur *= 10
        pow_accur += 1
    accur_numb = round(number, pow_accur)
    print(f"{accur_numb:.{pow_accur}f}")