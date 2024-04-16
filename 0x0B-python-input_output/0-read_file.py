def read_file(filename=""):
    """Function just reads file and prints to STDOUT"""
    with open(filename, mode="r", encoding="UTF-8") as f:
        print(f.read())
