# Session 3 Problems

def ps3p1():
    ticker = input("Enter stock ticker symbol: ")
    shares = float(input("Enter number of shares: "))
    cost   = float(input("Enter cost per share: "))
    invested = shares * cost
    print(f"{ticker}: Amount invested = ${invested:.2f}")

def ps3p2():
    last  = input("Enter your last name: ")
    mid   = float(input("Enter midterm score: "))
    fin   = float(input("Enter final exam score: "))
    total = mid + fin
    print(f"{last}: Total exam points = {total:.2f}")

def ps3p3():
    amt  = float(input("Enter total amount received: "))
    each = amt / 3
    print(f"Each receives = ${each:.2f}")

def ps3p4():
    make  = input("Enter car make: ")
    model = input("Enter car model: ")
    msrp  = float(input("Enter MSRP amount: "))
    disc  = float(input("Enter discount percent (decimal): "))
    off   = msrp * disc
    price = msrp - off
    print(f"{make} {model}")
    print(f"MSRP=${msrp:.2f}, Discount={disc*100:.1f}%")
    print(f"Amount off=${off:.2f}, Discounted price=${price:.2f}")

def ps3p5():
    r = float(input("Enter radius of circle: "))
    pi = 3.174
    area      = pi * r * r
    perimeter = 2 * pi * r
    print(f"Radius = {r:.2f}")
    print(f"Area = {area:.2f}, Perimeter = {perimeter:.2f}")

def main():
    print("Select program to run:")
    print(" 1) PS3P1 – Stock investment")
    print(" 2) PS3P2 – Exam total")
    print(" 3) PS3P3 – Split payment")
    print(" 4) PS3P4 – Auto discount")
    print(" 5) PS3P5 – Circle metrics")
    choice = input("> ")
    if   choice == '1': ps3p1()
    elif choice == '2': ps3p2()
    elif choice == '3': ps3p3()
    elif choice == '4': ps3p4()
    elif choice == '5': ps3p5()
    else: print("Invalid selection.")

if __name__ == "__main__":
    main()
