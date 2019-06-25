# Example of TRY CATCH
#
# @author SunilOS  
# @version 1.0
# @Copyright (c) SunilOS  
# @Url www.SunilOs.com
#

a =4
b = 2
try:
    c= a/b
    print('C:',c)
except ZeroDivisionError:
    print("check your divident is Zero")
else:
    print("Your divident was greater than zero")
finally:
    print("Exception testing is over")

print("-------------------------")
try:
    c= a/b
    print('C:',c)
except ZeroDivisionError as e:
    print("Check your divident is Zero", e)
except NameError as e:
    print("Undefined variable", e)
else:
    print("Wow no error")
finally:
    print("Exception testing is over")
