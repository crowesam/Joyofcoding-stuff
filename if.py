#Sam Crowe
#What will this program output when it's...
#1. Monday? Wake up at 7 am
#2. Saturday? Wake up at 9am
#3. Sunday? Wake up at 10am
#4. Raining? Wake up at 7 am

DoW = str.title(input("What day is it?"))
# DoW ="Monday"

if DoW == "Saturday":
    print("Wake up at 9am")
elif DoW == "Sunday":
    print("Wake up at 10am")
else:
    print("Wake up at 7 am")

#1 See top of page comments

#2  changed line#8 from  - input("What day is it?")