employees = [
    {"id": 101, "name": "Arun", "present": 22, "total": 25},
    {"id": 102, "name": "Bala", "present": 18, "total": 25},
    {"id": 103, "name": "Charan", "present": 25, "total": 25},
    {"id": 104, "name": "Divya", "present": 20, "total": 25},
    {"id": 105, "name": "Esha", "present": 15, "total": 25}
]
print("="*10," EMPLOYEE ATTENDANCE REPORT ","="*10)
def calculate_attendence(present,total):
     return (present/total)*100
     
total_employee = len(employees)
low_attendence_employee = 0
for employee in employees:

    print("ID: ",employee.get("id"))
    print("Name: ",employee.get("name"))
    percentage = calculate_attendence(employee.get("present"),(employee.get("total")))
    print(f"Attendence: {percentage:.2f}%")
    print("Status: ",end="")
    if percentage >= 90 and percentage <=100:
        print("Excellent")
    elif percentage >= 75 and percentage < 90:
            print("Good")
    elif percentage >= 0 and percentage < 75:
         print("Low Attendance")
         low_attendence_employee += 1
    else:
         print("Undefined")
    print("-"*30)

print("Total Employees: ",total_employee)
print("Low Attendance Employees: ",low_attendence_employee)