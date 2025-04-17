def file_operations():
    filename = "output.txt"

    try:
        user_input_write = input("Enter text to write to the file: ")
        with open(filename, 'w') as file:
            file.write(user_input_write + "\n")  # Add a newline character
        print(f"Data successfully written to {filename}.")
    except Exception as e:
        print(f"Error writing to file: {e}")
        return

    try:
        user_input_append = input("Enter additional text to append: ")
        with open(filename, 'a') as file:
            file.write(user_input_append + "\n") 
        print(f"Data successfully appended.")
    except Exception as e:
        print(f"Error appending to file: {e}")
        return

    try:
        print(f"\nFinal content of {filename}:")
        with open(filename, 'r') as file:
            for line in file:
                print(line, end='')  
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"Error reading from file: {e}")

if __name__ == "__main__":
    file_operations()