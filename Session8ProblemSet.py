

# 1. Quantity × Price with Discount
def compute_total(qty, price):
    total = qty * price
    if total > 100000.00:
        total *= 0.90 
    return total

def run_quantity_price():
    grand_total = 0.0
    while input("Do you want to enter quantity & price? (Yes/No): ").strip().lower() == 'yes':
        qty = int(input("  Quantity: "))
        price = float(input("  Price: "))
        total = compute_total(qty, price)
        print(f"  Qty={qty}, Price=${price:.2f}, Total=${total:.2f}\n")
        grand_total += total
    print(f"Grand total of all entries: ${grand_total:.2f}\n")


# 2. Batting Average
def batting_avg(hits, at_bats):
    return hits / at_bats if at_bats > 0 else 0

def run_batting():
    player_count = 0
    while input("Do you want to enter player stats? (Yes/No): ").strip().lower() == 'yes':
        name = input("  Last name: ")
        hits = int(input("  Hits: "))
        at_bats = int(input("  At-bats: "))
        avg = batting_avg(hits, at_bats)
        print(f"  {name}: Batting Average = {avg:.3f}\n")
        player_count += 1
    print(f"Total players entered: {player_count}\n")


# 3. Trip MPG
def compute_mpg(miles, gallons):
    return miles / gallons if gallons > 0 else 0

def run_trips():
    trip_count = 0
    while input("Do you want to enter trip data? (Yes/No): ").strip().lower() == 'yes':
        city = input("  Destination city: ")
        miles = float(input("  Miles traveled: "))
        gallons = float(input("  Gallons used: "))
        mpg = compute_mpg(miles, gallons)
        print(f"  {city}: Miles={miles}, MPG={mpg:.2f}\n")
        trip_count += 1
# 4. Employee Gross Pay
def get_rate(code):
    rates = {'L': 25.0, 'A': 30.0, 'J': 50.0}
    return rates.get(code.upper(), 0.0)

def run_payroll():
    total_gross = 0.0
    while input("Do you want to enter employee data? (Yes/No): ").strip().lower() == 'yes':
        name = input("  Last name: ")
        code = input("  Job code (L/A/J): ")
        hours = float(input("  Hours worked: "))
        rate = get_rate(code)
        if hours > 40:
            gross = 40 * rate + (hours - 40) * rate * 1.5
        else:
            gross = hours * rate
        print(f"  {name}: Gross pay = ${gross:.2f}\n")
        total_gross += gross
    print(f"Total gross pay for all employees: ${total_gross:.2f}\n")


# 5. Student Tuition
def compute_tuition(credits, code):
    rate = 250.0 if code.upper() == 'I' else 550.0
    return credits * rate

def run_tuition():
    total_tuition = 0.0
    while input("Do you want to enter student data? (Yes/No): ").strip().lower() == 'yes':
        name = input("  Last name: ")
        credits = int(input("  Credit hours: "))
        code = input("  District code (I/O): ")
        tuition = compute_tuition(credits, code)
        print(f"  {name}: Tuition owed = ${tuition:.2f}\n")
        total_tuition += tuition
    print(f"Total tuition owed for all students: ${total_tuition:.2f}\n")


