# Session 4 Problem Set

def problem1():
    q = int(input("Enter quantity: "))
    if q >= 1000:
        unit = 3.00
    else:
        unit = 5.00
    ext = q * unit
    tax = ext * 0.07
    total = ext + tax
    print(f"Quantity: {q}")
    print(f"Unit price: ${unit:.2f}")
    print(f"Extended price: ${ext:.2f}")
    print(f"Tax (7%): ${tax:.2f}")
    print(f"Total: ${total:.2f}")

def problem2():
    code = input("Enter item code (A or B): ")
    qty  = int(input("Enter quantity: "))
    if code == "A":
        unit = 10.00
    else:
        unit = 20.00
    ext = qty * unit
    print(f"Item: {code}")
    print(f"Unit price: ${unit:.2f}")
    print(f"Extended price: ${ext:.2f}")

def problem3():
    books = int(input("Number of books to order: "))
    cost  = float(input("Cost per book: "))
    total = books * cost
    if total > 50.00:
        ship = 0
    else:
        ship = 25
    print(f"Order total: ${total:.2f}")
    print(f"Shipping charge: ${ship:.2f}")

def problem4():
    name = input("Appliance name: ")
    cost = float(input("Cost of appliance: "))
    if cost > 1000:
        warr = cost * 0.10
    else:
        warr = cost * 0.05
    tot = cost + warr
    print(f"Appliance: {name}")
    print(f"Cost: ${cost:.2f}")
    print(f"Warranty cost: ${warr:.2f}")
    print(f"Total (cost + warranty): ${tot:.2f}")

def problem5():
    last = input("Enter your last name: ")
    dep  = int(input("Number of dependents: "))
    gross = float(input("Gross income: "))
    agi = gross - dep * 12000
    if agi > 50000:
        rate = 0.20
    else:
        rate = 0.10
    tax = agi * rate
    if tax < 0:
        tax = 100
    print(f"Last name: {last}")
    print(f"Gross income: ${gross:.2f}")
    print(f"Dependents: {dep}")
    print(f"Adjusted gross income: ${agi:.2f}")
    print(f"Income tax: ${tax:.2f}")

def main():
    print("Select problem to run (1-5):")
    print(" 1) Quantity Pricing")
    print(" 2) Item A/B Pricing")
    print(" 3) Book Order Shipping")
    print(" 4) Appliance Warranty")
    print(" 5) Income Tax Calculation")
    choice = input("> ")
    if   choice == '1': problem1()
    elif choice == '2': problem2()
    elif choice == '3': problem3()
    elif choice == '4': problem4()
    elif choice == '5': problem5()
    else: print("Invalid selection. Please choose 1-5.")

if __name__ == "__main__":
    main()