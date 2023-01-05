# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below. def hello_name(user_name):

def hello_name(user_name):
    print("hello_" + user_name + "!")

print("\nQuestion 1:\n")
hello_name("USERNAME")

# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing def first_odds():

def first_odds():
    return [x for x in range(100) if x%2 != 0]

print("\nQuestion 2:\n")
print(first_odds())

# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below. def max_num_in_list(a_list):

def max_num_in_list(a_list):  
 
    max = a_list[0]
    for x in a_list:
        if x > max:
            max = x
    return max
 
a_list = [1, -666, 13, 4, 3]

print("\nQuestion 3:\n")
print("Largest value is:", max_num_in_list(a_list))

# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100 unless it is also divisible by 400. The return should be boolean Type (true/false). def is_leap_year(a_year):

def is_leap_year(a_year):
  leap = False

  if (a_year % 4 == 0) and [(a_year % 100 != 0) or (a_year % 400 == 0)]: 
      leap = True

  return leap

print("\nQuestion 5:\n")
print(is_leap_year(2004))


# Question 5
# Write a function to check to see if all numbers in the list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type. def is_consecutive(a_list):

def is_consecutive(a_list):
    return (a_list) == list(range(min(a_list), max(a_list)+1))
     
test_list = [2,3,5,6,7,4]
#test_list = [1, -666, 13, 4, 3]
print("\nQuestion 5:\n")
print(is_consecutive(test_list))