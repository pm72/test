# # კასკადური მინიჭება
# a = b = c = 0
# print(a, b, c)


# მრავალმხრივი მინიჭება
# x, y = 1, 2
# print(x, y)

# x = 1
# y = 2
# print(x, y)


# x, y = y, x
# print(x, y)

# temp = x
# x = y
# y = temp
# print(x, y)


# # ინკრემენტაცია
# x = 0
# x = x + 15
# print(x)

# x += 2
# print(x)

# x += 1
# print(x)

# x -= 5
# print(x)

# x /= 2
# print(x)

# x *= 2
# x = int(x)
# print(x)

# x //= 2
# print(x)

# x %= 5
# print(x)


# ციკლები  Loops

# for loop

# arr = [1, 2, 3, 4, 5, 6, 7]

# for i in arr:
#   print(i)

# arr1 = [1, 2, 3, 4, 5, 6, 7]
# arr2 = iter(arr1)

# print(arr1)
# print(arr2)
# print(*arr2)

# print(next(arr2))
# print(next(arr2))
# print(next(arr2))
# print(next(arr2))
# print(next(arr2))
# print(next(arr2))
# print(next(arr2))

# print(next(arr2))

# arr2 = iter(arr1)

# print(next(arr2))
# print(next(arr2))
# print(next(arr2))

# arr2 = iter(arr1)

# print(next(arr2))
# print(next(arr2))
# print(next(arr2))
# print(next(arr2))
# print(next(arr2))



# for i in range(10)

# range()

# range(start, stop, step)
# range(1, 10, 1)
# 1-დან 10-მდე 1-ის ბიჯი   <====>  stop = 10-1 = 9

# range(stop)               range(start, stop)            range(start, stop, step)
# range(0, step-1, 1)       [start, stop-1]               [start, stop-1, step]
# range(0, 10-1)            [5, 13-1]                     [23, 31-1, 1]
# range(10)                                               [23, 31-1]
#                                                         [1, 10, 2]
#                                                         [15, 3, -2]
#                                                         [15, 3, -1]


# for i in range(10):
#   print(i)

# print("i =", i)


# for i in range(10):
#   print(i, end=' ')

# print()



# for i in range(4, 15, 3):
#   print(i, end=' ')

# print()


# for i in range(4, 15, 23):
#   print(i, end=' ')

# print()

# for i in range(24, 15, -23):
#   print(i, end=' ')

# print()


# for i in range(0, 10, 2):
#   print(i, end=' ')

# print()


# for i in range(1, 11, 2):
#   print(i, end=' ')

# print()


# for i in range(1, 15, 3):
#   print(i, end=' ')

# print()



# arr = [15, 21, 7, 26, 32, 8, 11]

# for i in arr:
#   print(i * 2)

# print(arr)


# arr = [15, 21, 7, 26, 32, 8, 11]
# print(arr, id(arr))

# # for i in range(len(arr)):    # for i in range(7)   [0, 1, 2, 3, 4, 5, 6]
# #   arr[i] *= 2     # arr[0] *= 2  arr[1] *= 2

# # print(arr, id(arr))


# for i in range(3, len(arr)):    # for i in range(7)   [0, 1, 2, 3, 4, 5, 6]
#   arr[i] *= 2     # arr[0] *= 2  arr[1] *= 2

# print(arr, id(arr))


# dict1 = {'name': 'John', 'age': 28, 'phone': '458 341200'}

# print(dict1)
# print(dict1['name'])
# print(dict1['age'])
# print(dict1['phone'])

# print(dict1.get('name'))


# dict1 = {'name': 'John', 'age': 28, 'phone': '458 341200'}

# print(dict1.keys())

# for k in dict1.keys():
#   print(k)

# print()
# for k in dict1:
#   print(k)

# print()
# for k in dict1:
#   print(dict1[k])

# print()
# for k in dict1:
#   print(dict1.get(k))



# dict1 = {'name': 'John', 'age': 28, 'phone': '458 341200'}

# if 'pirveli' in dict1:
#   print(dict1['pirveli'])
# else:
#   print("Key not found")

# print(dict1.get('pirveli'))
# print(dict1.get('pirveli', 'Key not found'))



# dict1 = {'name': 'John', 'age': 28, 'phone': '458 341200'}

# print(dict1.values())

# for v in dict1.values():
#   print(v)


# dict1 = {'name': 'John', 'age': 28, 'phone': '458 341200'}

# print(dict1.items())

# for k, v in dict1.items():    # k, v = ('name', 'John')
#   print(f"{k}: {v}")



# break and continue

# break

# for num in range(1, 11):
#   print(num)

#   if num == 5:
#     break

# print()

# for num in range(1, 11):
#   if num == 5:
#     break
  
#   print(num)


# for i in range(1, 20):
#   print(i)

#   break


# for i in range(1, 20):
#   break

#   print(i)


# for i in range(1, 11):
#   if i % 2 == 0:
#     print(i)

# for i in range(1, 11):
#   if i % 2 == 1:  # 1 == 1   True / False
#     print(i)

# for i in range(1, 11):
#   if i % 2 != 0:
#     print(i)

# for i in range(1, 11):
#   if i % 2:   # 1   True   /  0  False
#     print(i)

# for i in range(1, 11):
#   if not i % 2:   # not 1   False   /  not 0  True
#     print(i)



# even numbers with use continue
# for i in range(20):
#   if i % 2:  # if i % 2 == 1  ან  if i % 2 != 0
#     continue

#   print(i, end=' ')

# print()


# for i in range(10):
#   continue

#   print(i)
#   print(i ** 2)


# for i in range(10):
#   print(i)

#   continue

#   print(i ** 2)


# დავბეჭდოთ 1-დან 20-ის ჩათვლით რიცხვების ჯამი 10-სა და 11-ის გამოტოვებით:

# s = 0
# for i in range(1, 21):
#   # if i == 10 or i == 11:
#   if i in range(10, 12):
#     continue
  
#   s += i

# print(f"The sum is {s}")



# # continue-ს გამოყენებით დავბეჭდოთ რიცხვები 1-დან 20-ის ჩათვლით,
# # გარდა რიცხვებისა 10-დან 15-ის ჩათვლით
# for i in range(1, 21):
#   # if 10 <= i <= 15:
#   # if i >= 10 and i <= 15:
#   # if i in range(10, 16):
#   if i not in range(10, 16):
#     continue
  
#   print(i, end=' ')

# print()




# while loop

# სინტაქსი
# while <პირობა>:
#   ოპერატორი 1
#   ოპერატორი 2
#   ...
#   ოპერატორი n


# while True:   # while 1 < 2:
#   print('*')

# **********
# *********
# ********
# *******
# ******
# *****
# ****
# ***
# **
# *

# for i in range(10)  # for i = 0; i < 10; i++

# i = 10

# while True:
#   if i < 1:
#     break

#   print('*' * i)

#   i -= 1

# i = 10

# while i > 0:
#   print('*' * i)

#   i -= 1

# import time

# i = 10

# while i > 0:
#   print('*' * i)

#   i -= 1
  
#   time.sleep(0.5)



# break and continue

# import time

# i = 11

# while True:
#   i -= 1

#   if i < 1:
#     break
#   elif i < 4:
#     continue

#   print(i)
#   print("sleep\n")

#   time.sleep(0.35)



# Guess game
# import random
from random import randint

num = randint(1, 100)
i = 1

print("\nWas guessed a number between 1 and 100. Guess it...\n")

while True:
  guess = int(eval(input(f"Step: #{i}. Your guess: ")))

  if guess == num:
    print(f"You guessed a number! it was {num}.")
    break
  elif guess > num:
    print("Too great")
  else:
    print("Too less")
  
  print()

  i += 1

print("Game Over!")