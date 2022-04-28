from enum import Enum

class Day(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3


#PRINT THE ENUM MEMBER
print(Day.MONDAY)

# GET THE NAME OF THE ENUM MEMBER
print(Day.MONDAY.name)

# GET THE VALUE OF THE ENUM MEMBER
print(Day.MONDAY.value)