#!/usr/bin/env python3

# Created by: Rodas
# Created on: Sep 2021
# This program calculates the circumference of a circle
#    with user input


import constants


def main():
    # this function calculates the circumference

    # input
    radius = int(input("Enter your radius of circle (mm): "))

    # process
    circumference_of_circle = constants.TAU * radius

    # output
    print("Circumference is {} mm².".format(circumference_of_circle))
    print("\nDone.")


if __name__ == "__main__":
    main()
