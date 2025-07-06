inputTxt=input("Enter text to write to the file: ")

file_3=open('output.txt', 'r+')
file_3.write(inputTxt)
print("data successfully written")
file_3.close()

appendTxt=input("Enter additional text to append: ")
file_3=open('output.txt', 'a')
file_3.write(appendTxt)
print("data successfully appended")
file_3.close()

print("final content of output.txt")
file_3=open('output.txt', 'r+')
print(file_3.read())
file_3.close()