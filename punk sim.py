import random
import time

print("Панки хой !!!!")

input()
punk = input("Панки умирают ?: ")
if punk == "да":
    exit()
elif punk == "нет":
    print("Все верно добро пожаловать ")
else:
    print("Молодец даже в ответе протестуешь")
print("Зайти за пивом ?")    
money = 100
while True:
    end = input('На пилаке 1.партвейн - 140 /2.пиво - 100 / 3.кефир - 34.95(1/2/3)')
    if end == "1":
        print("Хммм не хвотает может пойти поискать ?")
        end = 1
        break
    elif end == "2":
        money -= 100
        end = 2
        break
    elif end == "3":
        money -= 34.95
        end = 3
        break
    else:
        print("И долго мнне еще тут стоять ? может что-то купишь ?")





print(f"На вашем счету осталось {money} рубллей ")


