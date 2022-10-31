#Assigned input of multiple is Even then return sum of all integers
#Assigned input of multiple is Odd then return 0

def even_odd_sum(input):
    a = 1
    b = 0
    for i in input:
        a = i*a
        b = i+b

    if a%2 == 0:
        print("The multiplication of number is even: ", a)
        print("The Sum of all integers")
        return b
    else:
        print("The multiplication of number is even: ", a)
        return 0

input = [5,7,9]
#input = [1,2,3,4]
#input = [3,5,6]
expected = even_odd_sum(input)
print(expected)
