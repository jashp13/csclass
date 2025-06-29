def problem1():
    quantity = int(input("Cantidad de widgets: "))
    if quantity > 10000:
        price = 10
    elif quantity >= 5000:
        price = 20
    else:
        price = 30
    extended_price = quantity * price
    tax = extended_price * 0.07
    total = extended_price + tax
    print(f"Extended price: ${extended_price:.2f}")
    print(f"Tax (7%):   ${tax:.2f}")
    print(f"Total:      ${total:.2f}")

def problem2():
    part = input("Part number: ")
    quantity = int(input("Quantity: "))
    if part == "10" or part == "55":
        unit_cost = 1.00
    elif part == "99":
        unit_cost = 2.00
    elif part == "80" or part == "70":
        unit_cost = 3.00
    else:
        unit_cost = 5.00
    total_cost = quantity * unit_cost
    print(f"Part {part}: unit cost = ${unit_cost:.2f}, total = ${total_cost:.2f}")

def problem3():
    principal = float(input("Principal amount: "))
    years = int(input("Years to maturity: "))
    if principal > 100000 and years == 5:
        rate = 0.06
    elif 50000 <= principal <= 100000 and years == 10:
        rate = 0.05
    elif 50000 <= principal <= 100000 and years == 5:
        rate = 0.04
    else:
        rate = 0.02
    interest = principal * rate
    print(f"Principal: ${principal:.2f}")
    print(f"Rate:      {rate*100:.1f}%")
    print(f"Interest:  ${interest:.2f}")

def problem4():
    tickets = int(input("Number of tickets: "))
    if tickets >= 25:
        price = 50
    elif tickets >= 10:
        price = 60
    elif tickets >= 5:
        price = 70
    else:
        price = 75
    total = tickets * price
    print(f"Tickets: {tickets}, price: ${price}, total: ${total}")

def problem5():
    last_name = input("Employee last name: ")
    salary = float(input("Salary: "))
    level = int(input("Job level: "))
    if level >= 10:
        bonus_rate = 0.25
    elif level >= 5:
        bonus_rate = 0.20
    else:
        bonus_rate = 0.10
    bonus = salary * bonus_rate
    print(f"{last_name} bonus: ${bonus:.2f}")

def main():
    menu = {
        "1": ("Widgets pricing", problem1),
        "2": ("Part cost", problem2),
        "3": ("CD interest", problem3),
        "4": ("Concert tickets", problem4),
        "5": ("Employee bonus", problem5)
    }
    while True:
        print("\nCIS106 Problems Menu:")
        for key, (desc, _) in menu.items():
            print(f" {key}. {desc}")
        print(" Q. Quit")
        choice = input("Choose a number: ").upper()
        if choice == "Q":
            break
        if choice in menu:
            menu[choice][1]()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
