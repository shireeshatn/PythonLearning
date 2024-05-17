def reverse_string(input_string):
    result = input_string[::-1]
    print("Reversed of a given string: %s is: %s " % (input_string, result))
    return result


def count_characters(input_string):
    result = len(input_string)
    print(
        "Number of characters in the given string: %s is: %s"
        % (input_string, result)
    )
    return result


def convert_to_uppercase(input_string):
    result = input_string.upper()
    print("Uppercase of a given string: %s is: %s" % (input_string, result))
    return result
