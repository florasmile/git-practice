def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """
    print("test")

    if len(numbers):
        return numbers[0]
    else:
        return None



if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
