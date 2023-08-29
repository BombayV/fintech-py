# ## 1. Print out every number 1-100
# for i in range(1,101):
#   print(i)
#
# ## 2. Print out every number from 50-100
# for i in range(50,101):
#     print(i)
#
#
# ## 3. Find the sum of the first 100 digits
# sum = 0
# for i in range(1,101):
#     sum += i
#     print(f"The sum is currently {sum}.")
#
#
# ## 4. Find the sum of the numbers from 1000 to 2000
# sum = 0
# for i in range(1000,2001):
#     sum += i
#     print(f"The sum is currently {sum}.")
#
#
# ## 5. Print out every perfect square number less than or equal to 100
# for i in range(1,11):
#     print(i**2)
#
#
# ## 6. If you got one grain of rice on day 1, two grains of rice on day 2, and four grains of rice on day 3, and it kept doubling like that, print out a daily report of how much rice you'd receive on each day for 30 days.
# rice = 1
# for i in range(1, 31):
#     print(f"On day {i} you would receive {rice} grains of rice.")
#     rice *= 2
#
#
# ## 7. Print out every number that ends in a 7 from 7-1007.
# for i in range(7,1008):
#     if i % 10 == 7:
#         print(i)


## 8. Print out every even number from 1-100.
# for i in range(1, 101):
#     if (i % 2 == 0):
#         print(i)
#
#
# ## 9. Print out every multiple of three from 1-100
# for i in range(1, 101):
#     if (i % 3 == 0):
#         print(i)
#
# ## 10. Print out multiples of two, another list of multiples of three, and then a third list of items which appear in both lists.
# for i in range(1, 101):
#     if (i % 2 == 0):
#         print(i)
# for i in range(1, 101):
#     if (i % 3 == 0):
#         print(i)
# for i in range(1, 101):
#     if (i % 2 == 0) and (i % 3 == 0):
#         print(i)


## CHALLENGE: Print out numbers which are multiples of 3 OR multiples of 2, but not multiples of both.
# if (86 % 2 == 0) or (86 % 3 == 0):
#     print('yes')

for i in range(1, 101):
    if (i % 2 == 0) and (i % 3 == 0):
        continue
    if (i % 2 == 0) or (i % 3 == 0):
        print(i)

## SUPER CHALLENGE: Print out the first 40 numbers in the Fibonacci sequence.
# n1, n2 = 0, 1
# while n1 < 40:
#     print(n1)
#     local = n1 + n2
#     n1 = n2
#     n2 = local
