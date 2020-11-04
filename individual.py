a = int(input("Введите числоа а:"))
b = int(input("Введите числоа b:"))
c = (a % b) * (b % a) + 1
print(f"Результат: {c}")