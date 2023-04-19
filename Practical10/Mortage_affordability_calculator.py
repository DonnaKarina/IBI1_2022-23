#define a function that can judge whether the price is 5 times cheaper than the salary
def aff_calculator(x, y):
    """
    input annual salary as x
    input the price of the house as y
    return whether the house is affordable or not
    """
    if 5*x >= y:
        print('yes')
    else:
        print('no')
#x = input('annual salary = ')
#y = input('price of the house = ')
#I found if you use input the code cannot work correctly

#this is an example
x=50000
y=150000
aff_calculator(x,y)
