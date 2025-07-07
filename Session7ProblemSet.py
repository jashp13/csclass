
# 1. Compound Interest over 5 Years
def compound_interest(principal, rate, years=5):
    total_interest = 0.0
    print("Year\tBeginning Balance\tEnding Balance")
    for year in range(1, years + 1):
        interest = principal * rate
        ending = principal + interest
        total_interest += interest
        print(f"{year}\t${principal:,.2f}\t\t${ending:,.2f}")
        principal = ending
    print(f"\nTotal interest earned: ${total_interest:,.2f}\n")


# 2. Fibonacci Sequence (first 20 terms)
def fibonacci(n=20):
    a, b = 1, 1
    seq = [a, b]
    for _ in range(n - 2):
        c = a + b
        seq.append(c)
        a, b = b, c
    return seq


# 3. Employee Bonus
def process_employee_bonus(filename):
    total_bonus = 0.0
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    for i in range(0, len(lines), 2):
        name = lines[i]
        salary = float(lines[i + 1])
        if salary >= 100_000:
            rate = 0.20
        elif salary >= 50_000:
            rate = 0.15
        else:
            rate = 0.10
        bonus = salary * rate
        total_bonus += bonus
        print(f"{name}: Salary = ${salary:,.2f}, Bonus = ${bonus:,.2f}")
    print(f"\nTotal bonuses paid: ${total_bonus:,.2f}\n")


# 4. Order Extended Prices
def process_orders(filename):
    total_ext = 0.0
    count = 0
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    for i in range(0, len(lines), 3):
        item = lines[i]
        qty = int(lines[i + 1])
        price = float(lines[i + 2])
        ext = qty * price
        total_ext += ext
        count += 1
        print(f"{item}: Quantity = {qty}, Price = ${price:.2f}, Extended = ${ext:.2f}")
    average = total_ext / count if count else 0
    print(f"\nTotal extended = ${total_ext:,.2f}, Orders = {count}, Average order = ${average:,.2f}\n")


# 5. Student Tuition
def process_tuition(filename):
    total_tuition = 0.0
    students = 0
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f if line.strip()]
    for i in range(0, len(lines), 3):
        name = lines[i]
        code = lines[i + 1].upper()
        credits = int(lines[i + 2])
        rate = 250 if code == "I" else 500
        tuition = credits * rate
        total_tuition += tuition
        students += 1
        print(f"{name}: Credits = {credits}, Tuition owed = ${tuition:,.2f}")
    print(f"\nTotal tuition owed = ${total_tuition:,.2f}, Students = {students}\n")
