

try:
    value=10/0
    print(f"division is {value}")
except ZeroDivisionError as e:
    print(e)
except ValueError:
    print("Value Error")
except:
    print("Invalid division")
