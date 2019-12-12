
def add(*args):
    total = 0
    for num in args:
        total = total + num
    return total

add(0,0)
add(-1,-1)
add(4,5)    
add(1,2,3,4)

def multiply(num1, *args):
    total = num1
    for num in args:
        total = total * num
    return total
    
multiply(1,2)
multiply(1,2,3,4)
