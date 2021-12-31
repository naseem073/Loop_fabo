#Python program get Fibonacci series til 'N' value
n = int(input("Enter the value of 'n': "))
a = 0
b = 1
sum = 0
z = 1
print("Series : ", end = " ")
while(z <= n):
  print(sum, end = " ")
  z += 1
  a = b
  b = sum
  sum = a + b
