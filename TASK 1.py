try:
    with open('sample.txt', 'r') as file:
        print("Reading file content:")
        i = 1
        for line in file:
            print("Line " + str(i) + ": " + line.strip()) #.strip() removes Leading (start) and Trailing (end) whitespace characters from a string.
            i += 1

except FileNotFoundError:
    print('Error: The file "sample.txt" was not found.')

