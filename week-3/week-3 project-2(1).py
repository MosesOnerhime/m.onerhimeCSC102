
# Make function for cubic equation
def cubic_eq():
    # Get the values to be used
    print("Using the format Ax³ + Bx² + Cx + D = 0")
    ai = float(input("What is the value for A? "))
    bi = float(input("Whats is the value of B? "))
    ci = float(input("What is the value of C? "))
    di = float(input("What is the value of D? "))
    # Divide through by A
    a = bi/ai
    b = ci/ai
    c = di/ai
    # Find the nature of the roots
    nature = ((a ** 2) * (b ** 2)) + (18 * a * b * c) - (4 * (b ** 3)) - (4 * (a ** 3) * c) - (27 * (c ** 2))
    # Using Cardano's formula
    q = ((3 * b) - (a ** 2))/9
    r = ((9 * a * b) - (27 * c) - (2 * (a ** 3)))/54
    s = (r + (((q ** 3) + (r ** 2)) ** (1/2))) ** (1/3)
    t = (r - (((q ** 3) + (r ** 2)) ** (1/2))) ** (1/3)
    x1 = s + t - ((1/3) * a)

    def greater_zero():
        # If discriminant is greater than zero
        print("The discriminant is greater than zero")
        print(f"Divide the cubic equation by (x - {x1})")
        print("Using the format ax² + bx + c = 0")
        # aq mean a for quadratic
        aq = int(input("What is the value of a? "))
        bq = int(input("What is the value of b? "))
        cq = int(input("What is the value of c? "))

        x2 = ((0 - bq) + (((bq ** 2) - (4 * aq * cq)) ** (1/2)))/(2 * aq)
        x3 = ((0 - bq) - (((bq ** 2) - (4 * aq * cq)) ** (1/2)))/(2 * aq)

        print(f"The roots of the cubic equation are {x1}, {x2}, and {x3}.")

    def equal_zero():
        # If discriminant is equal to zero
        print("The discriminant is equal to zero")
        x2 = x1
        x3 = x1

        print(f"The roots of the cubic equation are {x1}, {x2}, and {x3}.")

    def less_zero():
        # If discriminant is less than zero
        print("The discriminant is less than zero")
        i = (-1 ** (1/2))
        x_c = (1/2) * (3 ** (1/2)) * (s - t)
        x2 = (((-1/2) * (s + t)) - ((1/3) * a)) + (x_c * i)
        x3 = (((-1/2) * (s + t)) - ((1/3) * a)) - (x_c * i)
        print(f"The roots of the cubic equation are {x1}, {x2}, and {x3}.")

    if nature > 0:
        greater_zero()

    elif nature < 0:
        less_zero()

    elif nature == 0:
        equal_zero()


# run the code
cubic_eq()
