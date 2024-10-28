class JustNotCoolError(Exception):
    pass

x = 2
try:
    raise JustNotCoolError("This just isn't cool, man.")
    # raise Exception("I'm a custom exception")
    # print(x/1)
    # if not type(x) is str:
    #     raise TypeError("Only strings are allowed.")
except NameError:
    print("NameError means something is not defined")
except ZeroDivisionError:
    print("ZeroDivisionError means division by zero")
except Exception as error:
    print(error)
else:
    print('No errors')
finally:
    print("I'm going to print this no matter what")