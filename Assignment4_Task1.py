try:
    file_1= open('sample.txt', 'r')
    reading_file=file_1.read()
    print(reading_file)
except FileNotFoundError:
    print("the File sample.txt not found")

finally:
    print("task done")