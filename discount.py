# Step 1: Define the function calculate_discount
def calculate_discount(price, discount_percent):
    # If discount is 20% or higher, apply the discount
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        # Otherwise, return the original price
        return price

# Step 2: Prompt the user to enter the original price and discount percentage
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percent = float(input("Enter the discount percentage: "))

    # Step 3: Call the calculate_discount function to get the final price
    final_price = calculate_discount(original_price, discount_percent)

    # Step 4: Print the final price (or original price if no discount was applied)
    if final_price == original_price:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
    else:
        print(f"Discount applied! The final price is: ${final_price:.2f}")

except ValueError:
    print("Please enter valid numeric values for the price and discount percentage.")
