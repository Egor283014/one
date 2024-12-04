first= input("Введите 1-е целое число")
second = input("Введите 2-е целое число")
third  = input("Введите 3-е целое число")


if first ==  second and second==third: #все числа равны между собой
    print('3')
elif first ==  second or second==third or first==third: #2 из 3 введённых чисел равны между собой
    print('2')
elif first !=  second and second!=third: #равных чисел среди нет
    print('0')
