class InvalidFileContentError(Exception):     #Create Custom Error (Special Alarm 🚨)
    """Custom exception for invalid file content"""  
    pass

def read_file(file_path):                           #Function to Read File
    file = None                                     #Initially → no file opened
    try:
        print("\n Attempting to open file...")      #opening safely
        
        file = open(file_path, 'r')                  # Open file in read mode
        content = file.read()                      #Read all content from file

        # Simulate validation check
        if not content.strip():                    #Check:File is empty? Only spaces?
            raise InvalidFileContentError("File is empty or invalid!")#Custom alarm triggered!

        print("\n ✅ File read successfully!")
        return content

    except FileNotFoundError:                        #File does not exist
        print("\n Error: File not found!") 

    except PermissionError:                           #No permission to open
        print("\n Error: Permission denied!")  

    except InvalidFileContentError as e: 
        print(f"\n Custom Error: {e}")              #Custom Error: File is empty or invalid!

    except Exception as e:                           #fOR Unknown error
        print(f"\n Unexpected Error: {e}") 

    finally:                                          #If file opened → close it safely
        if file:
            file.close()
            print("\n File closed safely (finally block executed)")

# ---- MAIN EXECUTION ----
# __main__ is the name of the special scope where top-level code executes

if __name__ == "__main__":                         #“Start program from here”
    path = input("Enter file path: ")                #User enters file path
    data = read_file(path)                        #Call function

    if data:                                       #If file read successfully
        print("\n 📄 File Content Preview:")
        print(data[:100], "\n")                       # print first 100 chars