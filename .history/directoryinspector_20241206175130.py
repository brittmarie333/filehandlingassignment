#Create a Python script that lists all files and subdirectories in a given directory. 
# Your script should prompt the user for the directory path and then display the contents.
#Expected Outcome: The script should correctly list all files and subdirectories in the specified directory. 
# Handle exceptions for invalid paths or inaccessible directories.

C:\Users\pmari\OneDrive\Desktop\CODING TEMPLE HW\MODULE 3 PYTHON INTERMEDIATE\LESSON 5 FILE HANDLING\FILE HANDLING ASSIGNMENT\directoryinspector.py
def list_directory_contents(path):
        # List and print all files and subdirectories in the given path
    try:
        if not os.path.isdir(path):
            raise NotADirectoryError(f"'{path}' is invalid directory.")
        print(f"Contents of '{path}' :")
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isfile(item_path):
                print(f"[DIR] {item}")
            else:
                print("[FILE] {item}")
    except FileNotFoundError:
        print("File not found!")
    except NotADirectoryError:
        print("Directory not found!")
    except PermissionError:
        print("You do NOT have access to this directory!")
    except Exception as e:
        print(f"An unexpected error occured {e}")    

def main():
    path = input("Please provide directory path: ")
    list_directory_contents(path)

if __name__ == "__main__":
    main()