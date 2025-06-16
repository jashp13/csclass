# Problem 1
ticker = input("Enter stock ticker symbol: ")
num_shares = float(input("Enter number of shares: "))
cost_per_share = float(input("Enter cost per share: "))
amount_invested = num_shares * cost_per_share

print(f"\nTicker: {ticker}")
print(f"Amount invested: ${amount_invested:,.2f}")

# Problem 2
last_name = input("Enter your last name: ")
midterm = float(input("Enter midterm score: "))
final_exam = float(input("Enter final exam score: "))
total_points = midterm + final_exam

print(f"\nStudent: {last_name}")
print(f"Total exam points: {total_points:.1f}")

# Problem 3
total_amount = float(input("Enter total amount received: $"))
each_share = total_amount / 3

print(f"\nEach person receives: ${each_share:,.2f}")

# Problem 4
make  = input("Enter make: ")
model = input("Enter model: ")
msrp  = float(input("Enter MSRP amount: $"))
disc  = float(input("Enter discount percent (decimal): "))

amount_off       = msrp * disc
discounted_price = msrp - amount_off

print(f"\n{make} {model}")
print(f"MSRP: ${msrp:,.2f}")
print(f"Discount: {disc*100:.1f}%")
print(f"Amount off: ${amount_off:,.2f}")
print(f"Discounted price: ${discounted_price:,.2f}")


# Problem 5
radius = float(input("Enter radius of circle: "))
pi = 3.174

area = pi * radius * radius
perimeter = 2 * pi * radius

print(f"\nArea: {area:.2f}")
print(f"Perimeter: {perimeter:.2f}")


