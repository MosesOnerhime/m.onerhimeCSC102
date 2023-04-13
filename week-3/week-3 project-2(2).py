def greater_zero():
    # Input the values
    print("Using the format ax² + bx + c = 0")
    a = int(input("What is the value of a? "))
    b = int(input("What is the value of b? "))
    c = int(input("What is the value of c? "))
    # Almighty formula
    x1 = ((0 - b) + (((b ** 2) - (4 * a * c)) ** (1/2)))/(2 * a)
    x2 = ((0 - b) - (((b ** 2) - (4 * a * c)) ** (1/2)))/(2 * a)

    print(f"The roots of the quadratic equation are {x1} and {x2}.")


greater_zero()
