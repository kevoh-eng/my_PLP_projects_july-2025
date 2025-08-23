
def calculate_discount(price, discount_percent):

    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

def main():
    # Get user input
    try:
        original_price = float(input("Enter the original price of the item: $"))
        discount_percentage = float(input("Enter the discount percentage: "))

        # Validate inputs
        if original_price < 0:
            print("Error: Price cannot be negative.")
            return
        if discount_percentage < 0 or discount_percentage > 100:
            print("Error: Discount percentage must be between 0 and 100.")
            return

        # Calculate final price 
        final_price = calculate_discount(original_price, discount_percentage)

        # Output results
        print(f"\nResult:")
        if discount_percentage >= 20:
            discount_amount = original_price - final_price
            print(f"Discount applied: {discount_percentage}%")
            print(f"Original price: ${original_price:.2f}")
            print(f"Discount amount: ${discount_amount:.2f}")
            print(f"Final price: ${final_price:.2f}")
        else:
            print(f"No discount applied (requires 20% or higher)")
            print(f"Final price: ${original_price:.2f}")

    except ValueError:
        print("Error: Please enter valid numbers for price and discount percentage.")

if __name__ == "__main__":
    main()