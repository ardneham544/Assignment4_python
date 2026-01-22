try:
    # Opening the file in read mode
    file = open("sample.txt", "r")

    # Reading and printing file content line by line
    print("File content:\n")
    for line in file:
        print(line.strip())

    # Closing the file
    file.close()

except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
  
