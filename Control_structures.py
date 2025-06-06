'''Check if a number is even or odd'''

n = int(input("Enter a number: "))

if n%2==0:
    print(f"{n} is an even number")
elif n%2==1:
    print(f"{n} is an odd number")
else:
    print("Enter a valid integer")

'''Sum of integers from 1 to 50 using for loop'''

total = 0
for i in range(1,51):
   total+=i
print(f"The sum of numbers from 1 to 50 is: {total}")
