def add(x, y):
    """
    Returns the sum of x and y
    """
    # ^ This is a multi-line doc-string ("""),
    #   used to document the function.
    return x + y

def sub(x, y):
    """
        Returns the diff between x and y
        """
    return x - y

def mul(x, y):
    """
    Returns the multiple of x times y.
    """
    return x * y


def div(x, y):
    """
    Divide x by y

    Args:
        x: number to divide
        y: number to divide by

    Returns: Divided value
    """
    return x/y



if __name__ == "__main__":
    # Read input from user, convert to int
    our_x = int(input())
    our_y = int(input())
    # Calculate the answer
    answer = add(our_x, our_y)
    # Print out the answer
    print(answer)
