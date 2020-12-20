time = int(input("Введите  сколько сек"))
h = time // 3600
min = (time - h * 3600) // 60
sec = time - (h * 3600 + min * 60)
print(f"Время  чч:мм:сс   {h} : {min} : {sec}")