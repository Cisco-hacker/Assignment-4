try:
    data1 = input("Enter text to write to the file: ")
    with open('output.txt', 'w') as file:
        file.write(data1)
    print("Data successfully written to output.txt.")

    data2 = input("\nEnter additional text to append: ")
    with open('output.txt', 'a') as file:
        file.write("\n" + data2)
    print("Data successfully appended.")

    with open('output.txt', 'r') as file:
        print("\nFinal content of output.txt:")
        print(file.read())

except FileNotFoundError:
        print('Error: The file "sample.txt" was not found.')