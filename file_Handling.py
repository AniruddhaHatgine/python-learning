class InvalidFileContentError(Exception):
    """Custom exception for invalid file content"""
    pass

def read_file(file_path):
    file = None
    try:
        print("\n Attempting to open file...")
        
        file = open(file_path, 'r')
        content = file.read()

        # Simulate validation check
        if not content.strip():
            raise InvalidFileContentError("File is empty or invalid!")

        print("\n ✅ File read successfully!")
        return content

    except FileNotFoundError:
        print("\n Error: File not found!")

    except PermissionError:
        print("\n Error: Permission denied!")

    except InvalidFileContentError as e:
        print(f"\n Custom Error: {e}")

    except Exception as e:
        print(f"\n Unexpected Error: {e}")

    finally:
        if file:
            file.close()
            print("\n File closed safely (finally block executed)")

# ---- MAIN EXECUTION ----
# __main__ is the name of the special scope where top-level code executes

if __name__ == "__main__":
    path = input("Enter file path: ")
    data = read_file(path)

    if data:
        print("\n 📄 File Content Preview:")
        print(data[:100], "\n")  # print first 100 chars