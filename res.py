def read_File ():
    with open ("./input01.txt", 'r') as file:
        lines = file.read ().splitlines ()
    return lines
