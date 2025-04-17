def read_and_print_file(filename):
    try:
        print("Reading file content:")
        with open(filename, 'r') as file:
            line_number = 1
            for line in file:
                print(f"Line {line_number}: {line}", end='')
                line_number += 1
    except FileNotFoundError:
        print(f"\033[91mError: The file '{filename}' was not found.\033[0m")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


file_name = "sample.txt"

try:
    with open(file_name, 'w') as f:
        f.write("This is a sample text file.\n")
        f.write("It contains multiple lines.\n")
except Exception as e:
    print(f"Error creating sample.txt for testing: {e}")

read_and_print_file(file_name)


non_existent_file = "non_existent.txt"
read_and_print_file(non_existent_file)