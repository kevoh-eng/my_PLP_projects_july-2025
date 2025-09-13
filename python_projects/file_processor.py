



import os

def read_file(file_path: str) -> str:
    """
    Reads the content from the specified file.

    Args:
        file_path (str): The path to the input file.

    Returns:
        str: The content of the file.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If an error occurs while reading the file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Oops! The file '{file_path}' does not exist.")

    try:
        with open(file_path, 'r') as file:
            return file.read()
    except IOError as e:
        raise IOError(f"Unable to read the file '{file_path}'. Error: {e}")

def write_file(file_path: str, content: str):
    """
    Writes the given content to the specified file.

    Args:
        file_path (str): The path to the output file.
        content (str): The content to be written.

    Raises:
        IOError: If an error occurs while writing the file.
    """
    try:
        with open(file_path, 'w') as file:
            file.write(content)
    except IOError as e:
        raise IOError(f"An error occurred while trying to write to '{file_path}'. Error: {e}")

def process_file(input_file: str, output_file: str):
    """
    Processes the input file by reading, modifying its content, 
    and saving it to an output file.

    Args:
        input_file (str): The path of the input file.
        output_file (str): The path of the output file.
    """
    try:
        # Read content from the input file
        content = read_file(input_file)

        # Modify the content (convert to uppercase as an example)
        modified_content = content.upper()

        # Write the modified content to the output file
        write_file(output_file, modified_content)

        print(f"Success! The content from '{input_file}' has been modified and saved to '{output_file}'.")

    except (FileNotFoundError, IOError) as error:
        print(f"Error: {error}")

def main():
    """
    Main function to interact with the user, ask for filenames,
    and call the file processing functions.
    """
    print("Welcome to the File Processor!")

    # Ask the user for the input file and output file paths
    input_file = input("Please enter the path to the input file: ")
    output_file = input("Please enter the path to the output file: ")

    # Process the files (read, modify, write)
    process_file(input_file, output_file)

if __name__ == "__main__":
    main()

