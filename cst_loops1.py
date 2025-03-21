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
#     print("Welcome to USA 2025")
#
# else:
#     print("Country not supported")












######### LOOPS
#
#
#
#
# ############################



nums = [10,20,30,40,50]

# for x in nums:
#     print(x+1)

# for x in nums:
#     print(x * 3)



### sample program to find how many scored more than 60

# perc = [78,23,89,44,17,21,90,98]
# count = 0
#
# for x in perc:
#     if(x>60):
#         print(x)
#         count += 1
#
# print(count , " persons scored more than 60 %")









# names = ["krishna", "harish", "kiran", "preethi", "harsha", "satish"]
#
# for x in names:
#     print(x)



#### complete prog to find failed , third  , second , first , distn , inva;id count


# perc = [78,23,89,44,17,21,90,98,132,-30,113,88,92,65,55,54,10,15]
#
# failc,thirdc,secondc,firstc,distc,invalidc = (0,0,0,0,0,0)
#
# for p in perc:
#     if(p >= 0 and p < 35):
#         failc += 1
#     elif(p >= 35 and p < 50):
#         thirdc += 1
#     elif (p >= 50 and p < 60):
#         secondc += 1
#     elif (p >= 60 and p < 80):
#         firstc += 1
#     elif (p >= 80 and p <= 100):
#         distc += 1
#     else:
#         invalidc += 1

# print("third grade students count = ", thirdc)
# print("second grade students count = ", secondc)
# print("first grade students count = ", firstc)
# print("distinction grade students count = ", distc)
# print("failed grade students count = ", failc)
# print("invalid grade students count = ", invalidc)



### explaining range function

# nums = [1,2,3,4,5,6,7,8,9,10]
# for x in nums:
#     print(x)




# for x in range(1,11):
#     print(x)
#
# print("\n =======================================================  \n")
#
# for x in range(11):
#     print(x)



# for x in range(1,11):
#     print("sandy")



# for x in range(1,51):
#     if(x % 5 == 0):
#         print(x)




# for x in range(1,51):
#     if(x%2 == 0 and x%3==0):
#         print(x)
#
















# conditional or while loop


# a = 50
#
# while(a > 0):
#     print(a)


### Break , continue and pass


# nums = [10,20,30,40,50,60]
#
# for x in nums:
#     if(x == 30):
#         pass
#     print(x)





########## some programs

# while(True):
#     cnt = str(input("enter the cname = "))
#
#     if(cnt == "ind"):
#         print("India")
#         break
#
#     elif (cnt == "usa"):
#         print("usa")
#         break
#
#     else:
#         print("invalid try again")




#### Number Guessing Game

# I jhave taken a num 7 to be guessed
# mynum = 7
# count = 0
#
# # start the loop and ask use to guess the num
# while(True):
#     userin = int(input("guess the number btwn 1 to 10 = "))
#     count += 1
#
#     # checking the userin and mynum if both are same then i will break the loop
#     if(userin == mynum):
#         print("Bingo you guessed it right and the attempts taken was - " , count)
#         break
#     else:
#         print("Wrong guess try again.")













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





########## user name and pwd validation prog

# success = 0
# user = "santhosh"
# password = "San@123"
# attempts = 3
#
# for x in range(3):
#
#     name = str(input("enter the user name = "))
#     pwd  = str(input("enter the password = "))
#
#     attempts -= 1
#
#     if(user == name and password == pwd):
#         print("correct cred please proceed")
#         success = 1
#         break
#     else:
#         print("invalid credentials try again you are left with attempts - ", attempts)
#
#
# if(success == 0 and attempts == 0):
#     print("Your account is locked ")
#



############ Fibbonaci series ##########
#
# a=0
# b=1
#
# print(a, end = " ")
# print(b, end = " ")
#
# for x in range(10):
#     # res = f + s
#     # print(res, end = " ")
#     # f = s
#     # s = res
#
#     a = a + b
#     b = a + b
#
#     print(a , end = " ")
#     print(b , end = " ")
#








































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

















