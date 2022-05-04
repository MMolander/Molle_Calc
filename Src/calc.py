def add(x, y):
    """
    Returns the sum of x and y
    """
    # ^ This is a multi-line doc-string ("""),
    #   used to document the function.
    return x + y


if __name__ == "__main__":
    # Read input from user, convert to int
    our_x = int(input())
    our_y = int(input())
    # Calculate the answer
    answer = add(our_x, our_y)
    # Print out the answer
    print(answer)
