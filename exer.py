result = []
while True:
    number = input("Enter numbers to compare, type 'done' to finish entering:")
    if(number.lower() == 'done'):
        break
    result.append(int(number))
print(result)
