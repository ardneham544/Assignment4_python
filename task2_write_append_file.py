# Taking user input
data = input("Enter data to write into the file: ")

# Writing data to file
with open("output.txt", "w") as file:
    file.write("Written Data: " + data + "\n")

# Appending additional data
with open("output.txt", "a") as file:
    file.write("Appended Data: This is additional information.\n")

# Reading and displaying final file content
print("\nFinal content of the file:\n")
with open("output.txt", "r") as file:
    print(file.read())
  
