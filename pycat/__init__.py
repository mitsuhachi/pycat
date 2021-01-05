import fileinput
import sys


def main():
    sys.stdout.writelines(fileinput.input())
