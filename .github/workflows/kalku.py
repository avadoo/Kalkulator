# Дебильный калькулятор

from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print (Back.GREEN)
print (Fore.BLACK)

what = input ("Что делаем? (+, -):")

print ( Back.CYAN )


a = float(input ("Введи первое число: "))
b = float(input ("Введи второе число: "))

print ( Back.YELLOW )

if what == "+":
    c = a + b 
    print ("Результат: " + str(c))
    
elif what == "-":
    c = a - b 
    print ("Результат: " + str(c))

else:
    print ("Выбрана неверная операция!")

input()

