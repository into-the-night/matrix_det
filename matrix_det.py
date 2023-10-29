
def get_input():                            # Gets input and returns a list of lists (each row in a matrix).
    mylist = []
    order = int(input('Enter the order of the matrix (like 3 for a 3x3 matrix): '))
    i = 0
    print('Enter each element of the matrix seperated by a space, press enter for new row.')
    while i < order:
        nums = input().split()
        nums = [int(x) for x in nums]
        mylist.append(nums)
        i += 1
    return mylist

def change_signs(l):                        # Changes the signs of the first row of the matrix
    i = 0
    new = []
    while i < len(l):
        if i//2 == i/2:
            new.append(l[i])
        else:
            new.append(-l[i])
        i += 1
    return new

def matrix_det(l):                          # Find the determinant by recursion
    if len(l) == 1:
        return int(l[0][0])   
    l[0] = change_signs(l[0])
    res = 0
    c = 0
    for i in l[0]:
        n = []
        j = 1
        while j < len(l):
            temp = l[j].copy()
            temp.pop(c)
            n.append(temp)
            j += 1
        c += 1
        res += i * matrix_det(n)
    return res


answer = matrix_det(get_input())
print(f'The determinant is {answer}.')      # Prints output

        





        



        