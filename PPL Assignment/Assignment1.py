name = input("Enter Vendor Name: ")
year = int(input("Enter Year of Association: "))
contact = input("Enter Contact Number: ")
email = input("Enter Email ID: ")

monthly_purchase = float(input("Enter Monthly Purchase Amount: "))

annual_purchase = monthly_purchase * 12

print("\n--- Vendor Annual Purchase/Billing Report ---")
print("Vendor Name:", name)
print("Year of Association:", year)
print("Contact Number:", contact)
print("Email ID:", email)
print("Monthly Purchase:", monthly_purchase)
print("Annual Purchase:", annual_purchase)