hours = int(input("Введите часы:"))
minutes = int(input("Введите минуты:"))
if hours < 0 or minutes < 0 or minutes > 59:
    print("error")
else:
    print("Ответ:", ((hours % 24) * 60 + minutes))
