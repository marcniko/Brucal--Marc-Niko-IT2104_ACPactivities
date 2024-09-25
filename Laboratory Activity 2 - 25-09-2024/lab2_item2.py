def calculate_discount(amount):
    if amount > 5000:
        discount = 0.10  # 10% discount
    else:
        discount = 0.05  # 5% discount

    discount_amount = amount * discount
    final_price = amount - discount_amount
    print(f"Initial Purchase Amount: {amount:.2f}")
    print(f"Discount: {discount_amount:.2f}")
    print(f"Final Price: {final_price:.2f}")

while True:
    amount = float(input("Enter the total purchase amount: "))
    calculate_discount(amount)

    try_again = input("Do you want to try again? (yes/no): ").strip().lower()
    if try_again != 'yes':
        print("Thank you!")
        break