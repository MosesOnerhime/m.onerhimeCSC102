# This code aims to assist in solving various formulas
# Currency is in naira
def simple_interest():
    # input the parameters
    p = int(input("What is the principal? "))
    r = int(input("What is the rate(in percentage)? "))
    t = int(input("What is the value of T(duration in years)? "))
    # calculate the change and obtain amount
    change = (1 + ((r * t) / 100))
    a = p * change
    si = a - p
    t = str(t)
    a = str(a)
    si = str(si)
    print("The amount after " + t + " year(s) is " + " N" + a + ". The simple interest is N" +
          si + ".")


def compound_interest():
    # input the parameters
    p = int(input("What is the principal? "))
    r = int(input("What is the rate(in percentage)? "))
    r = r/100
    t = int(input("What is the value of T(duration in years)? "))
    n = int(input("What is the value of n(number of times interest is compounded per year)?"))
    # calculate the change and obtain amount compound interest
    change = pow((1 + (r / n)), (n * t))
    a = p * change
    ci = a - p
    n = str(n)
    t = str(t)
    a = str(a)
    ci = str(ci)
    print("The amount after compounding " + n + " time per year for " + t + " year(s) is " + " N" + a + ". The compound interest is N" +
          ci + ".")


def annuity_plan():
    # input the parameters
    pmt = int(input("What is the pmt? "))
    r = int(input("What is the rate(in percentage)? "))
    r = r/100
    t = int(input("What is the value of T(duration in years)? "))
    n = int(input("What is the value of n(number of times interest is compounded per year)?"))
    # calculate the change and obtain amount
    change = (pow((1 + (r / n)), (n * t)) - 1) / (r / n)
    a = pmt * change
    t = str(t)
    a = str(a)
    print("The amount after " + t + " years is N" + a + ".")


# Ask user for desired formula
function = input("What formula would you like to use(choose from 1-3, 1 = Simple interest, 2 = Compound interest, "
                 "3 = Annuity plan)? ")
# run the desired formula by choosing the functions
if function == "1":
    simple_interest()
elif function == "2":
    compound_interest()
elif function == "3":
    annuity_plan()
