def main():
    value = float(input("Enter the number:"))
    x = 0
    while x < 1:
        choice = int(input("Press 1 for C>F and press 2 for F>C: "))
        if (choice == 1):
            x += 1
            value = convertfa(value)
            print("{} degrees Fahrenheit".format(value))
        elif (choice == 2):
            x += 1
            value = convertcel(value)
            print("{} degrees Celcius".format(value))

def convertfa(value):
    value = (value * 1.0) + 32
    return value

def convertcel(value):
    value = (value - 30) / 2
    return value

if __name__ == '__main__':
    main()