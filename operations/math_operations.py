def addition(a, b):
    result = a + b
    print("Addition of %d and %d is %d" % (a, b, result))
    return result


def subtraction(a, b):
    result = a - b
    print("Subtraction of %d and %d is %d" % (a, b, result))
    return result


def multiplication(a, b):
    result = a * b
    print("Multiplication of %d and %d is %d" % (a, b, result))
    return result


def division(a, b):
    if b != 0:
        result = a / b
        print("Division of %d and %d is %d" % (a, b, result))
        return result
    else:
        print("Division of %d and %d is not possible. (Zero division error)" % (a, b))
        return None
