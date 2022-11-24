
def sum_with_range(min, max):
    sum = 0

    print(min, max)
    for x in range(min, max):
        sum += x
        return(sum) # result of the function is returned, that can be used in other functions or be saved


result = sum_with_range(1, 10)
sum_with_range(20, 30)

