import time
num = int(input("Введите число от 3 до 20: "))
for i in range(3, 21):
    for j in range(3, 21):
       if (i + j) % num == 0:
            print(f"Пара чисел: {i} и {j}")
            break
time.sleep(3)
print('________________________________')
print("Ты снова победил, Индиана Джонс!")