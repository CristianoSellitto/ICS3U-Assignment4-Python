#!/usr/bin/env python3

# Created by Cristiano Sellitto
# Created in October 2022
# A program that finds if a letter is capital or not


def main():
    # Finds if a letter is capital or not

    letter = input("Enter a single letter: ")
    try:
        ascii_integer = ord(letter)
        if ascii_integer >= 65 and ascii_integer <= 90:
            print("\n{0} is a capital letter.".format(letter))
        elif ascii_integer >= 97 and ascii_integer <= 122:
            print("\n{0} is not a capital letter.".format(letter))
        else:
            print("\n{} is not a valid character.".format(letter))
    except TypeError:
        print("\nError: {} is not a single or valid character.".format(letter))
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
