with open('newfile.txt', 'w') as file:
    file.write('This is a new file created!')

try:
    with open('newfile2.txt', 'w') as file2:
        file2.writelines(['\nThis is a new file created!', '\nThis is line 2', "\nthis is line 3!"])
except FileNotFoundError as e:
    print("File not found!", e)
except Exception as e:
    print("Something went wrong:", e)