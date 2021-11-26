from colorama import init
from colorama import Fore, Back, Style
init()
print(Back.MAGENTA)
what = input("Какую операцию вы желаете выполнить ? (+,-,*,/): ")
print(Fore.BLACK)
a = float(input("Введите первое число : "))
b = float(input("Введите второе число : "))
print(Fore.CYAN)
if what == "+":
    c = a + b
    print("Результат : " + str(c))
elif what == "-":
    c = a - b 
    print("Результат : " + str(c))
elif what == "*":
    c = a * b
    print("Результат : " + str(c))
elif what == "/":
    c = a / b
    print("Результат : " + str(c))
else:
    print("Вы ввели неправильную операцию") 