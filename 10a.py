def demonstrate_specific_exceptions():
    try:
        # NameError
        print(non_existent_variable)
    except NameError:
        print("Caught a NameError")

    try:
        # IndexError
        lst = [1, 2, 3]
        print(lst[5])
    except IndexError:
        print("Caught an IndexError")

    try:
        # KeyError
        dct = {'key': 'value'}
        print(dct['non_existent_key'])
    except KeyError:
        print("Caught a KeyError")

    try:
        # ZeroDivisionError
        result = 1 / 0
    except ZeroDivisionError:
        print("Caught a ZeroDivisionError")

demonstrate_specific_exceptions()
