import os

def logger(filename, message):

    if os.path.exists(filename):
        with open(filename, 'a') as file:
            file.write(f"{message}\n")
    else:
        with open(filename, 'w') as file:
            file.write(f"{message}\n")
    return