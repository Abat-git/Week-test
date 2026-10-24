#x = int(input("Введите число: "))
#if x < 0:
 #   print("Отрицательные вводить нельзя")
#elif x > 10:
#    print("Число чересчур большое!")
#else:
  #  print("В точку")

#for x in range(1, 5):
    #print(f"{x} + {x} = {x + x}")

#a = int(input("Первое число: "))
#b = int(input("Второе число: "))
#if a > b:
   # print(a)
#elif b > a:
    #print(b)
#else:
   # print("Числа равны")


#print("Введите числа:")
#numbers = []
#while True:
    #n = int(input("Пользователь вводит> "))
    #if n == 0:
      #  break
    #numbers.append(n)
#print("Числа:", ", ".join(map(str, numbers)))
#print("Сумма чисел:", sum(numbers))

#grades = list(map(int, input("Введите оценки через пробел: ").split()))
#print("Средний балл:", sum(grades) / len(grades))

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f"{self.name} говорит: Мяу!")


cat = Cat("Meowsic", 12)
cat.meow()