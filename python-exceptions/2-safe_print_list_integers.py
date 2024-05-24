#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    integrers_printed = 0

    while count < x:
        try:

            print("{:d}".format(my_list[count]), end="")
            integrers_printed += 1
        except (TypeError, ValueError):
            pass
        except IndexError:

            break

        count += 1
    print()
    return integrers_printed
