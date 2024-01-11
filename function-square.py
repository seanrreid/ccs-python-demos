def square(x):
    return x * x
    
# print(square(2))


# functionKeyword functionName(someArguments):
#     stuff to be done...

def count_tip(tip_amount, bill):
    tip = bill * tip_amount;
    total = bill + tip;
    return total

print(count_tip(.2, 100))