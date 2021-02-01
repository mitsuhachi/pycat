import fileinput


def main():
    for line in fileinput.input():
        print(line)
