# print("1 == 1 is", 1 == 1)                # True
# print("21 == 14 is", 21 == 14)            # False
# print("  is", 36 > 15)              # True
# print("0 != 0 is", 0 != 0)                # False
# print("1.58 >= -2.69 is", 1.58 >= -2.69)  # True



#  ჭეშმარიტობის ცხრილი

# ლოგიკური „და“  and            „ლოგიკური გამრავლება“
# True and True = True              1 * 1 = 1
# True and False = False            1 * 0 = 0
# False and True = False            0 * 1 = 0
# False and False = False           0 * 0 = 0



# ლოგიკური „ან“  or            „ლოგიკური შეკრება“
# True or True = True              1 + 1 = 1
# True or False = True             1 + 0 = 1
# False or True = True             0 + 1 = 1
# False or False = False           0 + 0 = 0



# ლოგიკური უარყოფა not
# not True = False
# not False = True


# print(bool(15), bool(-8), bool(2.58), bool([1, 5, 0]), bool({'two': 2}))
# print(bool(0), bool(0.0), bool([]), bool({}))


# print(int(True), float(True))
# print(int(False), float(False))



# login = input("Login: ")
# password = input("Password: ")

# print(login == 'pm72' and password == 'Step2024')


# 72-დან 100-ის ჩათვლით დავბეჭდოთ True
# score = 61
# print(score > 72 and score < 101)
# print(72 < score < 101)



# ==========================

# if ოპერატორი

'''
სინტაქსი
if <პირობა>:
  ოპერატორი 1
  ოპერატორი 1
  ...
  ოპერატორი n

if-ის შემდგომი ოპერატორები


if <პირობა>:
  ოპერატორი 1
  ოპერატორი 1
  ...
  ოპერატორი n
else:
  ოპერატორი 1
  ოპერატორი 1
  ...
  ოპერატორი n

if-ის შემდგომი ოპერატორები



if <პირობა>:
  ოპერატორი 1
  ოპერატორი 1
  ...
  ოპერატორი n
elif <პირობა>:
  ოპერატორი 1
  ...
  ოპერატორი n
elif <პირობა>:
  ოპერატორი 1
  ...
  ოპერატორი n
elif <პირობა>:
  ოპერატორი 1
  ...
  ოპერატორი n
else:
  ოპერატორი 1
  ოპერატორი 1
  ...
  ოპერატორი n

if-ის შემდგომი ოპერატორები

'''


# if True:
#   print("YES")
#   p = 51

# x = 53
# print(x, p)


# if False:
#   print("YES")
#   p = 51

# x = 53
# print(x, p)


# arr = [1, 9, 10, 15, 27, -5, 31]
# x = 15

# if x > arr[3]:
#   print(f"{x} > {arr[3]} = {x > arr[3]}")
# else:
#   print(f"{x} <= {arr[3]} <= {x <= arr[3]}")



# arr = [1, 9, 10]
# x = 15

# if x > arr[3]:
#   print(f"{x} > {arr[3]} = {x > arr[3]}")
# else:
#   print(f"{x} <= {arr[3]} <= {x <= arr[3]}")


# arr = [1, 9, 10, 15, 27, -5, 31]
# x = 15

# if len(arr) > 3:
#   if x > arr[3]:
#     print(f"{x} > {arr[3]} = {x > arr[3]}")
# else:
#     print("Array contains only three items")

# x = 13
# if len(arr) > 13:
#   if x > arr[3]:
#     print(f"{x} > {arr[3]} = {x > arr[3]}")
#   elif x == arr[3]:
#     print(f"{x} == {arr[3]} is {x == arr[3]}")
#   else:
#     print("OK!")
# else:
#     print("Array contains only three items")


# print("\n\nDone")



# score = 87

# if score > 60:
#   print("Grade D")
# elif score > 70:
#   print("Grade C")
# elif score > 80:
#   print("Grade B")
# else:
#   print("Grade A")


# score = 61

# if 60 < score < 101:
#   if 90 < score <= 100:
#     print("Grade A")
#   elif 80 < score <= 90:
#     print("Grade B")
#   elif 70 < score <= 80:
#     print("Grade C")
#   else:
#     print("Grade D")
# else:
#   print(None)




# პრიორიტეტი
# not, and, or

# arr = [1, 9, 10, 15, 27, -5, 31]
# x = 15

# if x > arr[3] and x == arr[2] or x > 10:
#   print(True)

# if (x > arr[3] and x == arr[2]) or x > 10:
#   print(True)

# if x > arr[3] and (x == arr[2] or x > 10):
#   print(True)

# if (x == arr[2] or x > 10) and x > arr[3]:
#   print(True)


# if x > arr[3]: print(True)
# else: print(False)

# if x >= arr[3]: print(True); print("YES! YES!"); print("END")
# else: print(False)




# arr = [1, 9, 10, 15, 27, -5, 31]
# x = 15

# if x > arr[3]:
#   print(f"{x} > {arr[3]} is {x > arr[3]}")
# elif not x == arr[3]:    # x != arr[3]
#   print(f"{x} = {arr[3]} is {x == arr[3]}")
# elif x == arr[2]:
#   print(f"{x} = {arr[2]} is {x == arr[2]}")
# else:
#   print(f"{x} > {arr[3]} is {x > arr[3]}")

# print("\nDone!..")


# if not False:
#   print("if true")
# else:
#   print(False)

# if not True:
#   print("if True")
# else:
#   print(False)



# ==========================

# is   in

# is

# arr1 = [1, 2, 3]
# arr2 = [1, 2, 3]

# print(arr1 == arr2)
# print(arr1 is arr2)
# print(id(arr1), id(arr2))


# in

# arr1 = [1, 2, 3, [1, 2, 3]]

# print([1, 2, 3] in arr1)

# # if 31 in arr1:
# #   print("YES")
# # else:
# #   print("NO")


name = "Paata Mamporia"

print('a' in name)
print('ata' in name)
print('ata ma' in name)
print('ata Ma' in name)