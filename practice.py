# Write a function to check if a number is even or odd.
# def num(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# n = int(input("Enter the number: "))
#
# if num(n) == True:
#     print(f"{n} is even.")
# else:
#     print(f"{n} is odd.")

#  Write a function that takes two numbers and returns the larger one.
# def max_of_two(n1,n2):
#     if n1 < n2:
#         return True
#     else:
#         return False
# n1 = int(input("Enter the first number: "))
# n2 = int(input("Enter the second number: "))
#
# if max_of_two(n1, n2) == True:
#     print(f"Larger number b/w {n1} & {n2} : {n2}")
# else:
#     print(f"Larger number b/w {n1} & {n2} : {n1}")

# Write a function to calculate the sum of the first N natural numbers.
# def sum(n):
#     s = (n*(n+1))/2
#     return s
# n = int(input("Enter the number upto which you want the sum : "))
#
# print(f"The sum of first {n} is {sum(n)}")

#  Reverse a Number

# n = int(input("Enter the number you want to reverse : "))
#
# s = str(n)
#
# print(f"{n} reverse is : {s[::-1]}")

#  Mathematical Approach
# def s(n):
#     n2 = 0
#     while n > 0:
#         p = n % 10
#         n //= 10
#         n2 = n2*10 + p
#     return n2
#
# n = int(input("Enter the number you want to reverse : "))
# print(f"{n} reverse is : {s(n)}")

# Count Digits in a Number
# n = int(input("Enter the number: "))
# s = str(n)
#
# print(f"{n} has {len(s)} digits.")

# Mathematical approach
# def count(n):
#     c = 0
#     while n > 0:
#             n //= 10
#             c += 1
#     return c
# n = int(input("Enter the number: "))
#
# print(f"{n} has {count(n)} digits.")

# checking if a number is Palindrome using this function.
# def s(n):
#     n2 = 0
#     while n > 0:
#         p = n % 10
#         n //= 10
#         n2 = n2*10 + p
#     return n2
#
# n = int(input("Enter the number you want to check palindrome : "))
# n2 = s(n)
# if n == n2:
#     print(f"Yes {n} is palindrome i.e.: {n2}")
# else:
#     print(f"oho number {n} and {n2} are not palindrome")

# sum of the digits of a given number.
# def s(n):
#     sum = 0
#     while n > 0:
#         p = n % 10
#         n //= 10
#         sum += p
#     return sum
#
# n = int(input("Enter the number whose sum of digit you want : "))
#
# print(f"The sum of {n} digits : {s(n)}")

# product of digits of a number
# def s(n):
#     pro = 1
#     while n > 0:
#         p = n % 10
#         n //= 10
#         pro *= p
#     return pro
#
# n = int(input("Enter the number whose product of digit you want : "))
#
# print(f"The product of {n} digits : {s(n)}")

# Count the number of even and odd digits in a number.
# def count_even_odd(n):
#     even = 0
#     odd = 0
#     while n > 0:
#         p = n % 10
#         n //= 10
#         if p % 2 == 0:
#             even += 1
#         else:
#             odd += 1
#     return even, odd
#
# n = int(input("Enter the number whose number of odd and even digits you want to find: "))
#
# even_count, odd_count = count_even_odd(n)
# print(f"Number of even and odd digits in {n} are {even_count} and {odd_count}, respectively.")

# Wap a function to calculate factorial of a numbr using recursion
# def fac(n,m):
#     if n == 1:
#         return m
#     else:
#         return fac(n-1, m*n)
#
# n = int(input("Enter the number whose factorial you would like to calculate: "))
# m = 1
# print(f"Factorial of {n} is {fac(n,m)}")

# Print numbers from n to 1 using recursion

# def rec(n):
#     if n == 1:
#         print(n)
#     else:
#         print(n)
#         rec(n-1)
#
# n = int(input("Enter the number: "))
#
# print(f"Number is {n} and the numbers are as follows:")
# rec(n)

# Print numbers from 1 to n  using recursion
# def rec(n,i):
#     if n >= 1:
#         print(i)
#         i += 1
#         rec(n-1, i)
#     else:
#         pass
# n = int(input("Enter the number: "))
# i = 1
# print(f"Number is {n} and the numbers are as follows:")
# rec(n, i)

#  Another approach without i  Print numbers from 1 to n  using recursion

# def rec(n):
#     if n >= 1:
#         rec(n-1)
#         print(n)
#
#     else:
#         pass
# n = int(input("Enter the number: "))
# print(f"Number is {n} and the numbers are as follows:")
# rec(n)

# Write a recursive function that takes an integer n and returns the sum of all numbers from 1 to n.
# def rec(s,n):
#     if n >= 1:
#         return rec(s+n, n-1)
#     else:
#         return s
# n = int(input("Enter the number : "))
# s = 0
# print(f"The sum of first {n} numbers is: {rec(s,n)}")

# try solving it without passing s as an argument and just using n
# def rec(n):
#     if n >= 0:
#         rec(n-1)
#         n += n
#         return n
#     else:
#         pass
# n = int(input("Enter the number : "))
# print(f"The sum of first {n} numbers is: {rec(n)}")

# Write a function to find the maximum of three numbers.
# def max(a,b,c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
#
# a = int(input("Enter the first number : "))
# b = int(input("Enter the second number: "))
# c = int(input("Enter the third number: "))
#
# print(f"The largest number between {a},{b} & {c} is : {max(a,b,c)}")

# Write a function to calculate the factorial of a number (without recursion).
# def fac(n):
#     z = 1
#     while n >= 1:
#         z *= n
#         n -= 1
#     else:
#         return z
#
# n = int(input("Enter the number: "))
#
# print(f"The factorial of number {n} is {fac(n)}")

# Write a function that checks if a number is prime.
# def prime(n):
#     count = 1
#     i = 2
#     while i <= n:
#         if n % i == 0:
#             count += 1
#             i += 1
#         else:
#             i += 1
#     if count == 2:
#         return "Yes", n
#     else:
#         return "No", n
#
# n = int(input("Enter the number: "))
# y, p = prime(n)
# if y == "Yes":
#     print(f"{y} number {p} is prime ")
# else:
#     print(f"{y} number {p} is not prime ")

# Write a function that returns the sum of all digits in a number.
# def s(n):
#     total = 0
#     while n > 0:
#         p = n % 10
#         n //= 10
#         total += p
#     return total
# n = int(input("Enter the number:"))
#
# print(f"The sum of all digits in number {n} is {s(n)}")

# Implement a recursive function to calculate factorial.
# def fac(n,mul):
#     if n <= 1:
#         return mul
#     return fac(n-1, mul*n)
#
# n = int(input("Enter the number: "))
# mul = 1
# print(f"The factorial of number {n} is {fac(n,mul)}")


# Implement a recursive function to reverse a number.

# def rec(n, rev=0):
#     if n <= 0:
#         return rev
#     else:
#         rev = rev * 10 + n % 10
#         return rec(n // 10, rev)
#
# n = int(input("Enter the number: "))
# print(f"The reverse of number {n} is {rec(n)}")

# Implement a recursive function to print numbers from 1 to N.
# def rec(n, i=1):
#     if i <= n:
#         print(i)
#         rec(n,i+1)
#
# n = int(input("Enter the number: "))
#
# print(f"The number has printed from 1 upto {n} as follows:")
# rec(n)

# Write a function that returns a lambda function to calculate the square of a number.

# n = int(input("Enter the number: "))
# s = lambda n: n ** 2
# print(f"The square of {n} is : {s(n)}")

# Use a lambda function to sort a list of tuples based on the second element.

# import random
#
# data = [(random.randint(1, 10), random.randint(1, 10)) for i in range(4)]
# print(data)
# sorted_list = sorted(data, key=lambda x: x[1])
# print(sorted_list)

# Implement a recursive function to find the sum of digits of a number.
# def rec(n, s=0):
#     if n <= 0:
#         return s
#     else:
#         s += n % 10
#         return rec(n//10, s)
#
# n = int(input("Enter the number: "))
#
# print(f"The sum of digits of {n} is {rec(n)}")

# Implement a recursive function to check if a string is a palindrome.
# def rec(n,rev=0):
#     if n <= 0:
#         return rev
#     else:
#         rev = rev * 10 + n % 10
#         return rec(n // 10, rev)
# def pro(n):
#     return "Yes" if rec(n) == n else "No"
#
# s = input("Enter the string : ")
# n = int(s)
# y = pro(n)
# if y == "Yes":
#     print(f"The string {s} is palindrome ")
# else:
#     print(f"The string {s} is not palindrome.")

# Implement a recursive function to compute the nth Fibonacci number.
# def fib(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
# n = int(input("Enter the number: "))
#
# print(f"The {n}th number in fibonacci sequence is : {fib(n)}")

# Create a list of 5 numbers and print the first, last, and middle elements.

# l = []
# n= int(input("How many elements do you want in your list: "))
#
# for i in range(n):
#     o = int(input(f"Enter the element at index {i}: "))
#     l.append(o)
#
# print(f"The first element of list is : {l[0]}")
# print(f"The middle elements of list are : {l[1:(n-1)]}")
# print(f"The last element of list is: {l[n-1]}")


# Create a list of mixed data types (int, string, float, bool).
# Change the third element of a list to "Python" and print the list.

# li = [18, "hello", 3.13, True, "Hey", 6, 3.14]
# print("Original List: ")
# for _ in li:
#     print(_, end=" ")
# print("\n")
# li[2] = "Python"
# print("Modified list: ")
# for _ in li:
#     print(_, end=" ")

# Write a Python program that does the following:
#
# 1️⃣ Take an integer n as input (the number of elements in a list).
# 2️⃣ Accept n integer inputs from the user and store them in a list.
# 3️⃣ Print the list after creation.
# 4️⃣ Replace the second element with 100.
#     5️⃣ Add 999 to the end of the list.
# 6️⃣ Remove the third element from the list.
# 7️⃣ Check if 50 exists in the list and print "50 is in the list" if found, else print "50 is not in the list".
# 8️⃣ Print the final list and its length.

# n = int(input("Enter the number of elements you want in the list: "))
# li = []
# for i in range(n):
#     p = int(input(f"The element at {i} index is: "))
#     li.append(p)
# print("Original list: ")
# print(li, end=" ")
# li[2] = 100
# li.append(999)
# li.pop(2)
# print("\n")
# if 50 in li:
#     print("50 is the list")
# else:
#     print("50 is not in the list")
# print("Final list is : ")
# print(li, end=" ")
# print("\n")
# print(f"The length of list is: {len(li)}")

# Write a program that:
# 1️⃣ Takes a list of numbers as input.
# 2️⃣ Prints only the **even numbers** using **list comprehension**.

n = int(input("Enter the number of elements you want in the list: "))
li = []
for i in range(n):
    p = int(input(f"The element at {i} index is: "))
    li.append(p)
print("Original list: ")
print(li, end=" ")
print("\n")
even = [x for x in li if x % 2 == 0]
print("Even number list is : ")
print(even, end=" ")
