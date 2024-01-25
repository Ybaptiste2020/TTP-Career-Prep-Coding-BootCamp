'''
Given a positive integer n, find the sum of all integers in the range [1, n] inclusive that are divisible by 3, 5, or 7.
Return an integer denoting the sum of all numbers in the given range satisfying the constraint.

'''

#Creating a difinition to handle the questions' requirments.
def sum_int():
  #Prompts the user to enter a positive number.
  n = int(input("Enter a positive integer: "))
  sum = 0

  #range based for loop
  for i in range(1,n+1):
    #if statement dealing with the divisibility by 3, 5, 7.
    if i%3==0 or i%5==0 or i%7==0:
      sum += i
  return sum
#print statement with defined function to get the code up and running.
print(sum_int())
