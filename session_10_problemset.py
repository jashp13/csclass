

# Problem 5 globals
total = 0.0
tax = 0.0

def problem1_discount(qty, price, rate):
    """Return (discount_amount, discounted_price)."""
    gross = qty * price
    discount_amount = gross * rate
    discounted_price = gross - discount_amount
    return discount_amount, discounted_price

def problem2_exams(last_name, scores):
    """Return (total_points, average_score)."""
    total_points = sum(scores)
    average = total_points / len(scores)
    return total_points, average

def problem3_sales_report(last_name, sales):
    """Return (commission, next_year_target)."""
    rate = 0.10 if sales > 100_000 else 0.05
    commission = sales * rate
    next_target = sales * 0.05
    return commission, next_target

def problem4_bowler(last_name, scores, handicap):
    """Return (average_score, average_with_handicap)."""
    average_score = sum(scores) / len(scores)
    average_with_handicap = average_score + handicap
    return average_score, average_with_handicap

def problem5_paint_globals(qty, price):
    """Compute and set global total and tax."""
    global total, tax
    total = qty * price
    tax = total * 0.07

def main():
    while True:
        print("\nChoose a problem (1-5) or Q to quit:")
        print("1) Discount calculator")
        print("2) Exam average")
        print("3) Sales commission report")
        print("4) Bowler average")
        print("5) Total & tax (globals)")
        choice = input("Selection: ").strip().lower()
        if choice == 'q':
            break

        if choice == '1':
            qty = float(input("Quantity: "))
            price = float(input("Unit price: "))
            rate = float(input("Discount rate (e.g. 0.15): "))
            da, dp = problem1_discount(qty, price, rate)
            print(f"Qty: {qty}, Price: {price:.2f}")
            print(f"Discount amount: {da:.2f}, Discounted price: {dp:.2f}")

        elif choice == '2':
            last = input("Student last name: ").strip()
            scores = [float(input(f"Score {i+1}: ")) for i in range(3)]
            total_pts, avg = problem2_exams(last, scores)
            print(f"{last} → Total points: {total_pts:.2f}, Average: {avg:.2f}")

        elif choice == '3':
            last = input("Salesperson last name: ").strip()
            sales = float(input("Sales amount: "))
            comm, target = problem3_sales_report(last, sales)
            print(f"{last} → Commission: {comm:.2f}, Next year’s target: {target:.2f}")

        elif choice == '4':
            last = input("Bowler last name: ").strip()
            scores = [float(input(f"Game score {i+1}: ")) for i in range(3)]
            handicap = float(input("Handicap: "))
            avg_score, avg_handicap = problem4_bowler(last, scores, handicap)
            print(f"{last} → Avg score: {avg_score:.2f}, With handicap: {avg_handicap:.2f}")

        elif choice == '5':
            qty = float(input("Quantity: "))
            price = float(input("Unit price: "))
            problem5_paint_globals(qty, price)
            print(f"Total (global): {total:.2f}, Tax (global): {tax:.2f}")

        else:
            print("Invalid selection—try again.")

    print("Goodbye!")

if __name__ == "__main__":
    main()
