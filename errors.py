try:
    number = int(input("Koi number daalo:"))
    result = 10/number
    print("Result:", result)
except ValueError:
    print("Ye valid number nahi tha!")
except ZeroDivisionError:
    print("Zero se divide nahi kar sakte!") 