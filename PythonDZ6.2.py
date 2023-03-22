# Задача 32: Определить индексы элементов массива (списка), 
#значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
massiv=[random.randint(0,100) for i in range(1, 100, 5) ]
print(massiv)
maximum=int(input('Введите максимальное значение: '))
minimum=int(input('Введите минимальное значение: '))

masindex=[]

if maximum>=minimum:
   for i in range(len(massiv)):
      if maximum>=massiv[i] and minimum<=massiv[i]:
          masindex.append(i)
print("Значения индексов элементов массива:",masindex)




