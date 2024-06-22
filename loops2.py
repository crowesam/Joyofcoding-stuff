#Writing Loops Second Effort
# Sam Crowe

#1 Multiples of 5 - 25 inclusive
for i in range(5,26,5):
    print(i, end=" ")
print()

#2 Multiples of 3 range -3 to 21 (inclusive) seperated by  comma and space
#for  i in range(-3, 22, 3)
for i in range(-3,22,3):
  if i<21:
    print(i, end=", ")
  elif i==21:
    print(21)
print()



#3 avg.py calculate the averrage of 10 real numbers entered by user
def collect_an_average():
    numbers=[] # A list to store the numbers

    for number in range(10):
     user_input = input(f"Enter input {number+1}: ")
     number = float(user_input)  # convert input to float (real number?)
     numbers.append(number) # Add the number to the list

     if numbers: #ensure that there weere numbers collected
         average = sum(numbers) / len(numbers)  # Calculate the average
     print("Average of the numbers:", average)

collect_an_average()




