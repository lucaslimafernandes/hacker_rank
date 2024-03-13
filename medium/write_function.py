# Task

# Given a year, determine whether it is a leap year. 
# If it is a leap year, return the Boolean True, otherwise return False.]

# In the Gregorian calendar, three conditions are used to identify leap years:

# The year can be evenly divided by 4, is a leap year, unless:
# The year can be evenly divided by 100, it is NOT a leap year, unless:
# The year is also evenly divisible by 400. Then it is a leap year.



def year(y):
    
    y = int(y)

    if y % 4 == 0:
        if y % 100 == 0:
            if  y % 400 == 0:
                return True
            else:
                return False
        else:
            return True

    return False



if __name__ == '__main__':

    year(1990)