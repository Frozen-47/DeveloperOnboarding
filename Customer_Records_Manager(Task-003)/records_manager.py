customers = [
    {
        "id" : 101,
        "name" : "Arun",
        "email" : "arun@gmail.com",
        "phone" : "9876543210"
    },
    {
        "id" : 102,
        "name" : "Bala",
        "email" : "bala@gmail.com",
        "phone" : "9765432108"
    }
]

def validate_name(name):
    if not name.strip():
        print("Invalid Name: Name Must not be empty or contain only spaces")
        return False
    return True

def validate_email(email):
    if "@" not in email or "." not in email:
        print("Invalid Email: Email Must contain @ and .")
        return False
    return True

def validate_phone(phone):
    if len(phone) != 10:
        print("Invalid Phone: Phone number must contain exactly 10 digits.")
        return False
    if not phone.isdigit():
        print("Invalid Phone: Phone number must contain numeric values")
        return False
    return True

def get_valid_customer_id():
    raw_id = input("Enter Customer ID: ")
    try:
        cust_id = int(raw_id)
        if cust_id <= 0:
            print("Invalid ID: Customer ID must be a positive integer greater than zero.")
            return None
        return cust_id
    except ValueError:
        print("Invalid ID: Customer ID must be a valid integer.")
        return None

def finder(id):
    for i in range(len(customers)):
        if id == customers[i].get("id"):
            return i
    return -1
    
def addCustomer():
    cust_id = get_valid_customer_id()
    if cust_id is None:
        return

    if finder(cust_id) != -1:
        print("-" * 34)
        print("Customer Already Exist!")
        print("-" * 34, "\n")
        return

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    phone = input("Enter Phone: ")

    is_name_valid = validate_name(name)
    is_email_valid = validate_email(email)
    is_phone_valid = validate_phone(phone)

    if is_name_valid and is_email_valid and is_phone_valid:
        customer = {
            "id": cust_id,
            "name": name.strip(),
            "email": email.strip(),
            "phone": phone.strip()
        }
        customers.append(customer)
        print("-" * 34)
        print("Customer added successfully!")
        print("-" * 34, "\n")
    else:
        print("-" * 34)
        print("Failed to add customer due to invalid inputs.")
        print("-" * 34, "\n")

def viewCustomers():
    if not customers:
        print("-" * 34)
        print("No customers found!")
        print("\nTotal Customer: ", len(customers))
        print("-" * 34, "\n")
    else:
        print("=" * 10, " CUSTOMER LIST ", "=" * 10, "\n")
        for customer in customers:
            print(f"{'Customer ID':<10}: {customer.get('id')}")
            print(f"{'Name':<10}: {customer.get('name')}")
            print(f"{'Email':<10}: {customer.get('email')}")
            print(f"{'Phone':<10}: {customer.get('phone')}")
            print("-" * 34)
        print("Total Customer:", len(customers))
        print("-" * 34, "\n")

def searchCustomer():
    cust_id = get_valid_customer_id()
    if cust_id is None:
        return

    index = finder(cust_id)
    if index == -1:
        print("-" * 34)
        print("\nCustomer not found!")
        print("-" * 34, "\n")
    else:
        print("-" * 34)
        print("\nCustomer Found!\n")
        print("-" * 34)
        print(f"{'Customer ID':<10}: {cust_id}")
        print(f"{'Name':<10}: {customers[index].get('name')}")
        print(f"{'Email':<10}: {customers[index].get('email')}")
        print(f"{'Phone':<10}: {customers[index].get('phone')}")
        print("-" * 34, "\n")

def updateCustomer():
    cust_id = get_valid_customer_id()
    if cust_id is None:
        return

    index = finder(cust_id)
    if index == -1:
        print("-" * 34)
        print("\nCustomer not found!")
        print("-" * 34, "\n")
        return

    print("-" * 34)
    new_name = input("Enter New Name: ")
    new_email = input("Enter New Email: ")
    new_phone = input("Enter New Phone: ")

    is_name_valid = validate_name(new_name)
    is_email_valid = validate_email(new_email)
    is_phone_valid = validate_phone(new_phone)

    if is_name_valid and is_email_valid and is_phone_valid:
        customers[index]["name"] = new_name.strip()
        customers[index]["email"] = new_email.strip()
        customers[index]["phone"] = new_phone.strip()
        print("-" * 34)
        print("Customer updated successfully!")
        print("-" * 34, "\n")
    else:
        print("-" * 34)
        print("Update failed: Invalid data provided. Existing customer record preserved.")
        print("-" * 34, "\n")

def deleteCustomer():
    cust_id = get_valid_customer_id()
    if cust_id is None:
        return

    index = finder(cust_id)
    if index == -1:
        print("-" * 34)
        print("\nCustomer not found!")
        print("-" * 34, "\n")
    else:
        customers.pop(index)
        print("-" * 34)
        print("\nCustomer deleted successfully!")
        print("-" * 34, "\n")

print("\n", "=" * 10, " CUSTOMER RECORD MANAGER ", "=" * 10, "\n")
while True:
    print("1. Add Customer\n2. View All Customers\n3. Search Customer\n4. Update Customer\n5. Delete Customer\n6. Exit")

    raw_choice = input("\nEnter your choice: ")
    try:
        choice = int(raw_choice)
    except ValueError:
        print("Invalid Choice: Please enter a numeric option from 1 to 6.")
        continue

    match choice:
        case 1:
            addCustomer()
        case 2:
            viewCustomers()
        case 3:
            searchCustomer()
        case 4:
            updateCustomer()
        case 5:
            deleteCustomer()
        case 6:
            print("Thank you for using Customer Records Manager!")
            break
        case _:
            print("Invalid Choice: Please select between 1 and 6.")