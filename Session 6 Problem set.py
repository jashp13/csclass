def problem1():
    num = 1
    while num <= 25:
        print(num)
        num += 2

def problem2():
    start = int(input("Start value: "))
    stop = int(input("Stop value: "))
    step = int(input("Increment value: "))
    current = start
    while current <= stop:
        print(current)
        current += step

def problem3():
    count = 0
    answer = input("Enter student? (Yes/No): ")
    while answer == "Yes":
        last_name = input("Last name: ")
        score1 = float(input("Score 1: "))
        score2 = float(input("Score 2: "))
        avg = (score1 + score2) / 2
        print(f"{last_name}: average = {avg:.2f}")
        count += 1
        answer = input("Another student? (Yes/No): ")
    print(f"Total students: {count}")

def problem4():
    count = 0
    total_pay = 0.0
    answer = input("Enter employee? (Yes/No): ")
    while answer == "Yes":
        last_name = input("Last name: ")
        hours = float(input("Hours worked: "))
        rate = float(input("Rate of pay: "))
        if hours > 40:
            overtime = hours - 40
            gross = (40 * rate) + (overtime * rate * 1.5)
        else:
            gross = hours * rate
        print(f"{last_name}: gross pay = ${gross:.2f}")
        total_pay += gross
        count += 1
        answer = input("Another employee? (Yes/No): ")
    if count:
        avg_pay = total_pay / count
        print(f"Total pay = ${total_pay:.2f}, Count = {count}, Average pay = ${avg_pay:.2f}")
    else:
        print("No employees entered.")

def problem5():
    total_disc = 0.0
    answer = input("Enter order? (Yes/No): ")
    while answer == "Yes":
        quantity = int(input("Quantity: "))
        unit_price = float(input("Unit price: "))
        ext_price = quantity * unit_price
        rate = 0.25 if ext_price > 10000 else 0.10
        disc_amt = ext_price * rate
        total = ext_price - disc_amt
        print(f"Extended = ${ext_price:.2f}, Discount = ${disc_amt:.2f}, Total = ${total:.2f}")
        total_disc += disc_amt
        answer = input("Another order? (Yes/No): ")
    print(f"Sum of all discounts = ${total_disc:.2f}")

def main():
    menu = {
        "1": ("Odd numbers 1-25", problem1),
        "2": ("Sequence start/stop/increment", problem2),
        "3": ("Student averages", problem3),
        "4": ("Employee payroll", problem4),
        "5": ("Order discounts", problem5),
    }
    while True:
        print("\nWhile-Loop Problems Menu:")
        for key, (desc, _) in menu.items():
            print(f" {key}. {desc}")
        print(" Q. Quit")
        choice = input("Choose problem number: ").upper()
        if choice == "Q":
            print("Goodbye!")
            break
        if choice in menu:
            print()
            menu[choice][1]()
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
