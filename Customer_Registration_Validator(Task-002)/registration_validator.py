def validate_name(name):
    if not name.strip():
        print("Invalid Name: Name Must not be empty or contain only spaces")
        return False
    return True

def validate_age(age):
    try:
        age = int(age)
    except ValueError:
        print("Invalid Age: Age must be an integer")
        return False
    if age < 18 or age > 100:
        print("Invalid Age: Age must be between 18 and 100.")
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

name = input("Enter Your Name: ")
age = input("Enter Your Age (18 - 100): ")
email = input("Enter Your email: ").strip()
phone = input("Enter Your phone: ")

print("\n" + "=" * 40)

name_valid = validate_name(name)
age_valid = validate_age(age)
email_valid = validate_email(email) 
phone_valid = validate_phone(phone)

if name_valid and age_valid and email_valid and phone_valid:
    print("       REGISTRATION SUCCESSFUL")
    print("-" * 40)
    print(f"Customer Name : {name}")
    print(f"Age           : {age}")
    print(f"Email         : {email}")
    print(f"Phone         : {phone}")
else:
    print("        REGISTRATION FAILED")

print("=" * 40)