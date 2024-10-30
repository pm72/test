# print("Hello, world!..")

# მონაცემთა ტიპები

'''
სტრიქონი (str)        მთელი (int)         ათწილადი (float)
  "some text"         5, 15, -1           1.25, 0.398741, 0.0
  'some text'         0, -5, -11          -1.0, -9.25
  '1258'
'''


# Comment
# a = 90


# Variables  ცვლადები

# name1 = "Paata Mamporia"        # name1 ->  "Paata Mamporia"
# name2 = 'Paata Mamporia'
# name3 = '''Paata Mamporia'''

# print(name1, type(name1), id(name1), name1.__sizeof__())
# print(name2, type(name2), id(name2), name2.__sizeof__())
# print(name3, type(name3), id(name3), name3.__sizeof__())



# სია   list

# arr1 = []
# arr2 = list()

# print(arr1, arr2, type(arr1))


# arr1 = [15, 25, 56, 98, -9, 0]
# arr2 = [1.58, 3.9, -0.24, 1.0]
# arr3 = ["Paata", "Good", "Like"]
# arr4 = [True, "String", 25.23, 0]

# print(arr1)
# print(arr2)
# print(arr3)
# print(arr4, "\n")

# print(len(arr1))
# print(len([78]))


# arr1 = [1, 89, "Maka", [56, 37, [87, 5], -9], "Lali", 51]

# # print(arr1)
# # print(arr1[0])
# # print(arr1[2])
# # print(arr1[3], type(arr1[3]))
# # print(arr1[3][0])
# # print(arr1[3][1])
# # print(arr1[3][2])
# # print(arr1[3][2][1])
# # print(arr1[-1])   # სიაში ბოლო ელემენტი

# print(len(arr1))

# print(arr1[-15])



# ლექსიკონი    dict

# d1 = {}
# d2 = dict()

# print(d1, d2)


# d1 = {
#   'first_name': 'Paata',
#   'last_name': 'mamporia',
#   'age': 52,
#   'education': 'Programmer'
# }

# print(d1)
# print(d1['first_name'])
# print(d1['last_name'])

# print(d1.get('last_name'))
# print(d1.get('laast_name'))
# print(d1.get('laast_name', 'Incorrect key'))




# მათემატიკური ოპერაციები
# +, -, *, **, /, //, %

# n1 = 2
# n2 = 8

# print(n1 + n2)
# print(n1 - n2)
# print(n1 * n2)
# print(n1 ** n2)


# print(2 ** 3)
# print(2 ** -1)  # 1 / 2 ** 1 = 1 / 2 = 0.5
# print(2 ** -2)  # 1 / 2 ** 2 = 1 / 4 = 0.25
# print(3 ** -2)  # 1 / 3 ** 2 = 1 / 9 = 0.(1)

# print(9 ** 0.5) # 9 ** (1/2) = 3.0
# print(9 ** 1/2) # 9 / 2 = 4.5
# print(9 ** (1/2)) # 9 ** (1/2) = 4.5

# print(8 ** (1/3))
# print(8 ** 0.33333)
# print(-8 ** (1/3))
# print((-9) ** 0.5)


# პრიორიტეტი
# ()
# **
# *, /
# +, -
# =

# print(2 + 3 * 5 - 2 ** 3 * 2)     # 2 + 15 - 8 * 2 = 1
# print(2 + 3 * (5 - 2) ** 3 * 2)   # 2 + 3 * 3 ** 3 * 2 = 2 + 3 * 27 * 2 = 164



# გაყოფა
# / ჩვეულებრივი, მათემატიკური გაყოფა
# // მთელზე გაყოფა (მხოლოდ მთელი ნაწილის აღება დამრგვალების გარეშე)
# % ნაშთის აღება

# n1 = 8
# n2 = 5

# print(n1 / n2)
# print(n1 // n2)
# print(n1 % n2)

# print(4 / 2)
# print(4 // 2)
# print(4 % 2) 



# a = 4 / 3

# print(a)
# print(int(a))
# print(int(1.99999))

# print(float(25))


# a = str(25.6)
# print(a, type(a))


# print(int('25'))
# print(int('sdfghh'))    #  invalid literal for int() with base 10: 'sdfghh'
# print(int('2.5'))         #  invalid literal for int() with base 10: '2.5'


# print(float('21'))
# print(float('2.63'))
# print(float('2.63.23'))   # could not convert string to float: '2.63.23'
# print(float('Nikoloz'))   # could not convert string to float: 'Nikoloz'


# a = '23'
# print(eval(a), type(eval(a)))

# a = '2.32'
# print(eval(a), type(eval(a)))

# a = '2.32 + 5'
# print(eval(a), type(eval(a)))


# name = input()
# print("Welcome,", name)
# print("Welcome, " + name)
# # print("Welcome,", name, sep='')

# print("Paata " + "Mamporia " + "52 years old")
# print("Paata " * 5)


# number = input("Enter a number: ")    # აბრუნებს სტრიქონს  str
# print(type(number))
# # print(number + 10)


# number = input("Enter a number: ")
# # print(int(number) + 10)
# number = int(number)

# print(number + 10)


# number = int(input("Enter a number: "))
# print(number + 10)

# number = float(input("Enter a number: "))
# print(number + 10)

# number = eval(input("Enter a number: "))
# print(number + 10)


# ფორმატირებული გამოტანა
# fstring

x = eval(input("Enter first number: "))
y = eval(input("Enter second number: "))

print("The sum is", x + y)
print("The sum is {x + y}")
print(f"The sum is {x + y}")
print(f"{x} + {y} = {x + y}")
print(f"{x} - {y} = {x - y}")