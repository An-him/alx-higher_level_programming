def read_file(filename=""):
    """Function just reads file and prints to STDOUT"""
    with open(filename, encoding="UTF-8") as f:
        for line in f:
            print(line, end="")
