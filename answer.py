def modify_content(content):
    """
    Modify the content of the file (example: convert text to uppercase).
    """
    return content.upper()  # Modify as needed (e.g., uppercase transformation)


def read_and_write_file():
    """
    Reads a file and writes the modified content to a new file.
    Handles errors for invalid filenames.
    """
    try:
        # Ask the user for the input filename
        input_filename = input("Enter the name of the file to read: ")

        # Attempt to open the file for reading
        with open(input_filename, "r") as infile:
            content = infile.read()  # Read the content of the file

        # Modify the content
        modified_content = modify_content(content)

        # Ask the user for the output filename
        output_filename = input("Enter the name of the file to save the modified content: ")

        # Write the modified content to the new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"Modified content has been written to '{output_filename}' successfully!")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist. Please check the filename.")
    except PermissionError:
        print(f"Error: You don't have permission to access '{input_filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Run the program
read_and_write_file()
