#Fibonacci numbers
n = int(input("Enter the value of 'n': "))
f1= 0
f2 = 1
sum = 0
count = 1
print("Fibonacci Series: ", end = " ")
while(count <= n):
  print(sum, end = " ")
  count += 1
  f1= f2
  f2= sum
  sum = f1+f2
  
  