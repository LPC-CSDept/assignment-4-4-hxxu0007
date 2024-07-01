def main():

    numbers = []
    """
    ########################################
    Code Your Program here
    ########################################
    """
    #Getting numbers to compare, 'done' to stop, 2+
    while True:
        number = input("Enter at least 2 numbers to compare, type 'done' to finish entering:")
        if(number.lower() == 'done'):
            break
        numbers.append(int(number))
    #assign first 2 in numbers to min and max    
    if(numbers[0] <= numbers[1]):
        minval = numbers[0]
        maxval = numbers[1]
    else:
        minval = numbers[1]
        maxval = numbers[0]
    #loop through list to compare the rest members, assign new value to min and max if found
    #iterate from 1 to 10 (inclusive), you can use range(1, 11). normally need len()-1 but not here
    for i in range(2, len(numbers)):
        if(numbers[i] < minval):
            minval = numbers[i]
        if(numbers[i] > maxval):
            maxval = numbers[i]
    print(*numbers)
    print(maxval, minval)
    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, maxval, minval


if __name__ == '__main__':
    main()
