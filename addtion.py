
def add(*args):
    total = 0
    for num in args:
        total = total + num
    return total

print(add(0,0))
print(add(-1,-1))
print(add(4,5))    
print(add(1,2,3,4))

def multiply(num1, *args):
    total = num1
    for num in args:
        total = total * num
    return total
    
print(multiply(1,2))
print(multiply(1,2,3,4))
