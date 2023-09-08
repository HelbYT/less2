i = 0

while i != 1:
    i = int(input("Продовжити/Стартувати - 0, закінчити - 1 : "))
    if (i == 1):
        break

    number1 = int(input("Введіть 1 число: "))
    number2 = int(input("Введіть 2 число: "))
    number3 = int(input("Введіть 3 число: "))

    d = 0
    iscorrect = 0
    helping = 0
    helping2 = 0

    if number1 > number2:
        helping = number1
        helping2 = number2
    else:
        helping = number2
        helping2 = number1

    while d <= number3:  
        if d >= number3:
            iscorrect = 1
        d += helping


    if d == number3:
        print("Вітаємо, ваше число ідеально підійшло")
        d / helping
        print("Вам потрібно " + d + "монеток по" + helping)
    else:
        if (d != number3):
            c = int(d / helping)
            d += helping2
            if (d == number3):
                print("Правильно")
                print("Вам потрібно " + c + "монеток по " + helping2 + "та одна по" + helping)
            else: 
                print("Ваше число не підійшло")
