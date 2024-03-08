class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def remove_employee(self, employee):
        self.employees.remove(employee)


class Employee:
    def __init__(self, name, id_number, department):
        self.name = name
        self.id_number = id_number
        self.department = department


class Company:
    def __init__(self, name):
        self.name = name
        self.departments = {}

    def add_department(self, department):
        self.departments[department.name] = department

    def remove_department(self, department_name):
        del self.departments[department_name]

    def get_department(self, department_name):
        return self.departments.get(department_name)

    def get_all_employees(self):
        all_employees = []
        for department in self.departments.values():
            all_employees.extend(department.employees)
        return all_employees


def main():
    company = Company("XYZ Company")

    while True:
        print("\nEmployee Management System")
        print("1. Add Department")
        print("2. Remove Department")
        print("3. Add Employee")
        print("4. Remove Employee")
        print("5. List All Employees")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            department_name = input("Enter department name: ")
            department = Department(department_name)
            company.add_department(department)
            print(f"Department '{department_name}' added successfully.")
        elif choice == '2':
            department_name = input("Enter department name: ")
            company.remove_department(department_name)
            print(f"Department '{department_name}' removed successfully.")
        elif choice == '3':
            department_name = input("Enter department name: ")
            department = company.get_department(department_name)
            if department:
                name = input("Enter employee name: ")
                id_number = input("Enter employee ID: ")
                employee = Employee(name, id_number, department)
                department.add_employee(employee)
                print("Employee added successfully.")
            else:
                print(f"Department '{department_name}' not found.")
        elif choice == '4':
            department_name = input("Enter department name: ")
            department = company.get_department(department_name)
            if department:
                id_number = input("Enter employee ID to remove: ")
                for employee in department.employees:
                    if employee.id_number == id_number:
                        department.remove_employee(employee)
                        print("Employee removed successfully.")
                        break
                else:
                    print("Employee not found.")
            else:
                print(f"Department '{department_name}' not found.")
        elif choice == '5':
            all_employees = company.get_all_employees()
            if all_employees:
                print("List of All Employees:")
                for employee in all_employees:
                    print(f"Name: {employee.name}, ID: {employee.id_number}, Department: {employee.department.name}")
            else:
                print("No employees found.")
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
