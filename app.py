"""
The code is a simple file management application implemented in Python. It allows the user to perform
operations like creating, viewing, deleting, reading, and editing files.
"""
import os #here os is a module we imported to interact withthe operating system such as listing files and managing files in the Directory
def create_file(filename):
    try:
        with open(filename,'x')as f:#The 'x' mode in file handling is used to create a new file for writing
            print(f"File Name {filename}: Created successfully!")
    except FileExistsError:
        print(f"file name{filename}already exists!")
    except Exception as E:
        print("An error occurred!")


def view_all_files():
    files=os.listdir()
    if not files:
        print("No File Found!")
    else:
        print("Files in Directory!")
        for file in files:
            print(file)


def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename}has been deleted sucessfully!")
    except FileNotFoundError:
        print("File Not Found")
    except exception as e:
        print("an error occurred!")


def read_file(filename):
    try:
        with open("sample.txt",'r')as f:
            content=f.read()
            print(f"content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"{filename}Does not exist!")
    except Exception as e:
        print('an error occurred!')


def edit_file(filename):
    try:
        with open('sample.txt','a') as f:
            content= input('Enter data to add=')
            f.write(content +"\n")
            print('content added to {filename} successfully!')
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")
    except Exception as e:
        print('an error occurred!')

#main function
def main():
    while True:
        print('FILE MANAGEMENT APP')
        print('1:Create file')
        print('2:View all files')
        print('3:Delete file')
        print('4:Read file')
        print('5:Edit file')
        print('6:Exit')

        choice=input('Enter your choice(1-6)=')
        if choice=='1':
            filename=input("Enter the file-name to create=")
            create_file(filename)
        elif choice=='2':
            view_all_files()
        elif choice=='3':
            filename=input('enter the name of file you want to delete =')
            delete_file(filename)
        elif choice=='4':
            filename=input('Enter file name to read=')
            read_file(filename)
        elif choice=='5':
            filename=input('Enter the file name to edit=')
            edit_file(filename)
        elif choice=='6':
            print('closing the app.....')
            break
        else:
            print('In-valid Syntax')

if __name__=="__main__" :
    main()























