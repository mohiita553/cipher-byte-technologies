def generate_receipt(customer_name, customer_phno, items, prices, payment_method):
    total = sum(prices)
    receipt = f"Payment Receipt\n{'='*30}\n"
    receipt += f"Customer Name: {customer_name}\n"
    receipt += f"customer phno: {customer_phno}\n"
    receipt += f"{'Item':<20}{'Price':>10}\n"
    receipt += '-'*30 + '\n'

    for item, price in zip(items, prices):
        receipt += f"{item:<20}{price:>10.2f}\n"

    receipt += '-'*30 + '\n'
    receipt += f"{'Total':<20}{total:>10.2f}\n"
    receipt += f"Payment Method: {payment_method}\n"
    receipt += '='*30 + '\n'
    receipt += "Thank you for your purchase!"

    return receipt

# Example usage:
customer_name = "Kaveendhar nadh"
customer_phno ="9967834672"
items = ["jackfruit", "Bananas", "pineapple", "kiwi",]
prices = [220, 120, 80, 140]
payment_method = "Credit Card"

receipt = generate_receipt(customer_name, customer_phno, items, prices, payment_method)
print(receipt)
def generate_receipt(customer_name, customer_phno, items, prices, payment_method):
    total = sum(prices)
    receipt = f"Payment Receipt\n{'='*30}\n"
    receipt += f"Customer Name: {customer_name}\n"
    receipt += f"customer phno: {customer_phno}\n"
    receipt += f"{'Item':<20}{'Price':>10}\n"
    receipt += '-'*30 + '\n'

    for item, price in zip(items, prices):
        receipt += f"{item:<20}{price:>10.2f}\n"

    receipt += '-'*30 + '\n'
    receipt += f"{'Total':<20}{total:>10.2f}\n"
    receipt += f"Payment Method: {payment_method}\n"
    receipt += '='*30 + '\n'
    receipt += "Thank you for your purchase!"

    return receipt

