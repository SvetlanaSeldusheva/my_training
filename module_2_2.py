f = first = int(input('Введите первое число: '))
s = second = int(input('Введите второе число: '))
t = third = int(input('Введите третье число: '))

if f == s and f == t and s == t:
    print(3, 'числа равны')
elif f == s or f == t or s == t:
    print(2, 'числа равны')
else:
    print(0, '- равных чисел нет')