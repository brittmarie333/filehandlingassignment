import os

def list_directory_contents(path):
    # List and print all files and subdirectories in the given path
    try:
        if not os.path.isdir(path):
            raise NotADirectoryError(f"'{path}' is an invalid directory.")
        
        print(f"Contents of '{path}':")
        for item in os.listdir(path):
            item_path = os.path.join(path, item)
            if os.path.isdir(item_path):  # Check if it's a directory
                print(f"[DIR] {item}")
            elif os.path.isfile(item_path):  # Check if it's a file
                print(f"[FILE] {item}")
            else:
                print(f"[OTHER] {item}")  # In case there are any other types of entries
                
    except FileNotFoundError:
        print("File or directory not found!")
    except NotADirectoryError:
        print(f"'{path}' is not a valid directory!")
    except PermissionError:
        print("You do NOT have access to this directory!")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")    

def main():
    path = input("Please provide directory path: ")
    list_directory_contents(path)

if __name__ == "__main__":
    main()
