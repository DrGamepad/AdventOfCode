def read_File (input_file):
    with open (input_file, 'r') as file:
        lines = file.read ().splitlines ()
    return lines
