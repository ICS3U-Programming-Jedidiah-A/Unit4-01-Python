#!/usr/bin/env python3
# Created By: Jedidiah
# Date: Jan 11, 2021
# This program shows the amount of loops.
def main():
    # this function uses a while loop
    loop_counter = 0

    # input
    positive_integer = int(input("Enter how many times to repeat: "))
    print("")

    # process & output
    while loop_counter < positive_integer:
        print("{0} time through the loop.".format(loop_counter))
        loop_counter = loop_counter + 1


if __name__ == "__main__":
    main()
