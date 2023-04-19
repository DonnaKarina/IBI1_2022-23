import re
#define the function
def code_counting(x):
    #find the code starts with ATG and ends with TGA
    y = re.findall(r'ATG\S+TGA', x)
    #the result is a list, I changed the list into string
    y_string = ''.join(y)
    print(y_string)
    #count the characters in the string
    count1 = len(y_string)
    count2 = len(x)
    percentage = count1/count2
    print(percentage)
    if percentage >= 0.5:
        print('protein-coding')
    if 0.1 < percentage <0.5:
        print('unclear')
    if percentage <= 0.1:
        print('non-coding')
#input an example
code_counting('TGGATGATGACCGAUG')
