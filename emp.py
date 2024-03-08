import json


class Department:
    def __init__(self, dept_name):
        self.dept_name = dept_name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)


class Employee:
    def __init__(self, emp_name, emp_id, title, dept_name):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.title = title
        self.dept_name = dept_name


class Company:
    def __init__(self, comp_name):
        self.comp_name = comp_name
        self.depts = {}

    def add_dept(self, dept):
        self.depts[dept.dept_name] = dept

    def remove_dept(self, dept_name):
        del self.depts[dept_name]

    def get_dept(self, dept_name):
        return self.depts.get(dept_name)

    def get_all_employees(self):
        all_employees = []
        for dept in self.depts.values():
            all_employees.extend(dept.employees)
        return all_employees


# Function to save company data to a JSON file
    
def save_data(company):
    with open("Company_Data.json", "w") as file:
        data = {
            "c_name": company.comp_name,
            "depts": [
                {
                    "dept_name": dept.dept_name,
                    "employees": [
                        {
                            "emp_name": employee.emp_name,
                            "emp_id": employee.emp_id,
                            "title" : employee.title
                        }
                        for employee in dept.employees
                    ]
                }
                for dept in company.depts.values()
            ]
        }
        json.dump(data, file, indent=4)

# Function to load company data from a JSON file
def load_data():
    try:
        with open("Company_Data.json", "r") as file:
            data = json.load(file)
            c_name = data["c_name"]
            company = Company(c_name)
            for dept_data in data["depts"]:
                dept_name = dept_data["dept_name"]
                dept = Department(dept_name)
                for employee_data in dept_data["employees"]:
                    employee = Employee(employee_data["emp_name"], employee_data["emp_id"],employee_data['title'], dept)
                    dept.add_employee(employee)
                company.add_dept(dept)
            return company
    except FileNotFoundError:
        return None

def main():
    # Load company data from file or create a new company
    company = load_data()
    if company is None:
        company = Company("East Vantage Pvt Ltd")

    while True:
        print("\nEmployee Management System Menu")
        print("1. Add the Department")
        print("2. Remove the Department")
        print("3. Add the Employee Details")
        print("4. Remove the Employee Details")
        print("5. Show all Employees details in the Company")
        print("6. Show all Departments in the Company")
        print("7. Save the data into the json file")
        print("8. Exit from the menu")

        option = input("Enter Your Option: ")

        if option == '1':
            dept_name = input("Enter the department name: ")
            dept = Department(dept_name)
            company.add_dept(dept)
            print(f"Department '{dept_name}' added successfully.")
        elif option == '2':
            dept_name = input("Enter the department name: ")
            company.remove_dept(dept_name)
            print(f"Department '{dept_name}' removed successfully.")
        elif option == '3':
            dept_name = input("Enter the department name: ")
            dept = company.get_dept(dept_name)
            if dept:
                emp_name = input("Enter the Employee Name : ")
                emp_id = input("Enter the Employee ID : ")
                title = input("Enter the Employee Title : ")
                employee = Employee(emp_name, emp_id, title, dept)
                dept.add_employee(employee)
                print("Employee added successfully.")
            else:
                print(f"Department '{dept_name}' not found.")
        elif option == '4':
            dept_name = input("Enter Department Name: ")
            dept = company.get_dept(dept_name)
            if dept:
                emp_id = input("Enter Employee ID to remove: ")
                for employee in dept.employees:
                    if employee.emp_id == emp_id:
                        dept.remove_employee(employee)
                        print("Employee removed successfully.")
                        break
                else:
                    print("Employee not found.")
            else:
                print(f"Department '{dept_name}' not found.")
        elif option == '5':
            all_employees = company.get_all_employees()
            if all_employees:
                print("List of All Employees : ")
                for employee in all_employees:
                    print(f"Name: {employee.emp_name}, Employee ID: {employee.emp_id}, Title :{employee.title}, Department: {dept.dept_name}")
            else:
                print("No employees found.")
        elif option == '6':
            print("List of All Departments are :")
            for dept_name in company.depts:
                print(dept_name)
        elif option == '7':
            save_data(company)
            print("Data Saved Successfully")
        elif option == '8':
            print("Exiting from the menu")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
