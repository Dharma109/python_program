# simple if else block

# age = int(input("enter your age = "))
#
# if(age >= 21 and age <= 30):
#     print("eligible for marraige")
#     print("get ready dude")
# else:
#     print("Not eligible for marraige")
#     print("dont get ready pls wait")






















# # Nested if example

# age = int(input("enter the age = "))
#
# if(age >= 21):
#     if(age < 30):
#         print("correct age")
#     if(age >= 30 and age < 35):
#         print("Marry soon")
#     if(age >= 35):
#         print("No Marraige age barred / expired to get married")
#     if(age == 25):
#         print("Sweet age")
# else:
#     print("not eligible pls wait")



# # if -elif - else or switch cond

#
# age = int(input("enter the age = "))
#
# if(age >= 21):
#     if(age < 30):
#         print("correct age")
#     elif(age == 31):
#         print("marraige fixed perfect age")
#     elif(age >= 30 and age < 35):
#         print("Marry soon")
#     elif(age >= 35):
#         print("No Marraige")
#     elif(age == 25):
#         print("sweet age")
# else:
#     print("not eligible")



# another example for switch
#
# c = str(input("enter the country name = "))
#
# if(c == "IND"):
#     print("Welcome to india")
#
# elif(c == "USA"):
#     print("Welcome to USA")
#
# elif(c == "UK"):
#     print("Welcome to UK")
#
# elif(c == "USA"):
#     print("Welcome to USA 2024")
#
# else:
#     print("Country not supported")












######### LOOPS ############################



nums = [10,20,30,40,50]
#
# for x in nums:
#     print(x+1)

# for x in nums:
#     print(x * 3)

#
# perc = [78,23,89,44,17,21,90,98]
#
# cnt = 0
# for x in perc:
#     if(x > 60):
#         print(x)
#         cnt = cnt + 1
#
# print("total first class students cpunt = ", cnt)


# names = ["kanna", "harish", "kiran", "preethi", "harsha", "satish"]
#
# for x in names:
#     print(x)


# perc = [78,23,89,44,17,21,90,98]
# count = 0
#
# for x in perc:
#     if(x >= 90):
#         print(x)
#         count += 1
#
# print("distn stu count  = ", count)

# perc = [78,23,89,44,17,21,90,98,132,-30,113,88,92,65,55,54]
#
# failc = 0
# firstc = 0
# secondc = 0
# thirdc = 0
# distc = 0
# invalidc = 0
#
# for x in perc:
#
#     if(x >= 0 and x < 35):
#         # print("====> Fail")
#         failc += 1
#     elif(x >= 35 and x < 50):
#         thirdc += 1
#     elif(x >= 50 and x < 60):
#         secondc += 1
#     elif(x >= 60 and x < 80):
#         firstc += 1
#     elif(x >= 80 and x <= 100):
#         distc += 1
#     else:
#         # print("Invaid  = ", x)
#         invalidc += 1
#
#
# print("distinction  = " , distc)
# print("first  = ", firstc)
# print("second = " , secondc)
# print("third = ", thirdc)
# print("fail = " , failc)
# print("invalid = " , invalidc)
#


# nums = [1,2,3,4,5,6,7,8,9,10]
#
# for x in nums:
#     print(x)


# for x in range(1,101):
#     print(x)




# for x in range(1,11):
#     print("sandy")



# for x in range(1,51):
#     if(x % 2 == 0):
#         print(x)


# for x in range(1,51):
#     if(x%2 == 0 and x%3==0):
#         print(x)

















# conditional or while loop

#
# a = 50
#
# while(a > 0):
#     print(a)
#     a = a - 1




# a = 50
#
# while(a > 0):
#
#     if(a%5==0):
#         print(a)
#
#     a = a - 1
#
#



#
# for x in range(1,10):
#     print("*" * x)









#########################################################


# mynum = 3
# count = 0
# while(True):
#     guessnum = int(input("guess the number from 1 to 10 = "))
#     count = count + 1
#     if(mynum == guessnum):
#          print("bingo u guessed it right in counts ", count)
#          break
#     else:
#          print("sorry wrong guess pls try again ")
#
#



#### break , continue and pass
# break = loop termination statement
# continue = iteration skip statement
# pass = ignore statement



# nums = [10,20,30,40,50,60]
#
# for x in nums:
#     if(x == 30):
#         pass
#     print(x)





# USERNAME PWD validation prog

# attempts = 3
#
# myuser = "sandy@gmail.com"
# mypass = "San@123"
# success = 0
#
# while(attempts > 0):
#     username = str(input("enter the user name = "))
#     password = str(input("enter the Password = "))
#
#     attempts = attempts - 1
#
#     if(username == myuser and password == mypass):
#         print("welcome to home page ")
#         success = 1
#         break
#
#     else:
#         print("sorry wrong cred try again attempts left ", attempts)
#
# if(success == 0):
#     print("You have exceeded your attempts and acc is locked")




####   Snake and ladder
#
# attempts = 0
# import random
# pos = 0
#
# while(pos <= 100):
#
#     dice = random.randrange(1,7)
#     attempts = attempts + 1
#     pos = pos + dice
#     print(pos)
#
#     if (pos == 100):
#         print("awesome i completed game in attempts = ", attempts)
#         break
#
#     if(pos > 100):
#         pos = pos - dice
#         print("your number cannot exceed 100 ", pos, dice , pos+dice)
#
#     if(pos == 23):
#         print("ladder from 23 to 67")
#         pos = 67
#
#     elif (pos == 45):
#         print("ladder from 45 to 88")
#         pos = 88
#
#     elif (pos == 17):
#         print("ladder from 17 to 77")
#         pos = 77
#
#     elif (pos == 62):
#         print("snake from 62 to 10")
#         pos = 10
#
#     elif (pos == 94):
#         print("snake from 94 to 12")
#         pos = 12
#
#     elif (pos == 32):
#         print("snake from 32 to 3")
#         pos = 3
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

















