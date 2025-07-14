def forecast_sales():
    forecasts = {
        'jan': 0.10, 'feb': 0.10, 'mar': 0.10,
        'apr': 0.15, 'may': 0.15, 'jun': 0.15,
        'jul': 0.20, 'aug': 0.20, 'sep': 0.20,
        'oct': 0.25, 'nov': 0.25, 'dec': 0.25,
    }
    while input("Run sales forecast? (Yes/No): ").strip().lower() == 'yes':
        last_name = input("Last name: ").strip()
        month = input("Month (Jan–Dec): ").strip().lower()[:3]
        sales = float(input("Current sales amount: "))
        pct = forecasts.get(month, 0)
        next_sales = sales * (1 + pct)
        print(f"{last_name}, next month's sales forecast is: {next_sales:.2f}\n")


def paint_gallons():
    while input("Run paint calculator? (Yes/No): ").strip().lower() == 'yes':
        L = float(input("Length of room: "))
        W = float(input("Width of room: "))
        H = float(input("Height of room: "))
        area = 2*(L*W) + 2*(L*H) + 2*(W*H)
        gallons = area / 50
        print(f"Room surface area: {area:.2f} sq ft → Gallons needed: {gallons:.2f}\n")


def car_price():
    total_msrp = 0.0
    total_final = 0.0
    while input("Run car pricing? (Yes/No): ").strip().lower() == 'yes':
        make = input("Make (e.g. Honda): ").strip().lower()
        model = input("Model (e.g. Accord): ").strip().lower()
        ev_code = input("Electric vehicle? (Y/N): ").strip().lower()
        msrp = float(input("MSRP: "))
        total_msrp += msrp

        if ev_code == 'y':
            discount = 0.30
        elif make == 'honda' and model == 'accord':
            discount = 0.10
        elif make == 'toyota' and model == 'rav4':
            discount = 0.15
        else:
            discount = 0.05

        price_after_discount = msrp * (1 - discount)
        final_price = price_after_discount * 1.07  # +7% tax
        total_final += final_price

        print(f"Out-the-door price: {final_price:.2f}\n")

    print(f"Sum of all MSRPs: {total_msrp:.2f}")
    print(f"Sum of all final sales prices: {total_final:.2f}\n")


def ticket_price():
    total_revenue = 0.0
    while input("Run ticket calculator? (Yes/No): ").strip().lower() == 'yes':
        last_name = input("Last name: ").strip()
        miles = float(input("Miles from downtown Chicago: "))
        if miles >= 30:
            price = 12
        elif miles >= 20:
            price = 10
        elif miles >= 10:
            price = 8
        else:
            price = 5
        total_revenue += price
        print(f"{last_name}'s ticket price: ${price:.2f}\n")

    print(f"Total ticket revenue: ${total_revenue:.2f}\n")


def assessed_value():
    rates = {
        'cook': 0.90,
        'dupage': 0.80,
        'mchenry': 0.75,
        'kane': 0.60,
    }
    total_market = 0.0
    total_assessed = 0.0
    while input("Run assessment calculator? (Yes/No): ").strip().lower() == 'yes':
        county = input("County: ").strip().lower()
        market = float(input("Market value of home: "))
        total_market += market
        rate = rates.get(county, 0.70)
        assessed = market * rate
        total_assessed += assessed
        print(f"Assessed value: {assessed:.2f}\n")

    print(f"Sum of market values: {total_market:.2f}")
    print(f"Sum of assessed values: {total_assessed:.2f}\n")


def main():
    actions = {
        '1': ('Sales Forecast', forecast_sales),
        '2': ('Paint Calculator', paint_gallons),
        '3': ('Car Pricing', car_price),
        '4': ('Ticket Calculator', ticket_price),
        '5': ('Home Assessment', assessed_value),
        'q': ('Quit', None)
    }
    while True:
        print("Select a program to run:")
        for key, (name, _) in actions.items():
            print(f"  {key}) {name}")
        choice = input("Choice: ").strip().lower()
        if choice == 'q':
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action:
            action[1]()
        else:
            print("Invalid choice; try again.\n")


if __name__ == '__main__':
    main()
