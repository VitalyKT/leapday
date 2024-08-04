def leapYear(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

# Использование функции
year = int(input("Введите год:\n"))
if leapYear(year):
    print(f"{year} високосный год.")
else:
    print(f"{year} не високосный год.")