''' 
Paola Katherine 
Exercise 1 using input
'''



def calculate_salary(hours, wage):
    overtime_hours = hours - 40
    regular_hours = hours - overtime_hours
    overtime_wage = wage * 1.5
    regular_pay= regular_hours * wage
    overtime_pay = overtime_hours * overtime_wage
    total_pay = regular_pay + overtime_pay
    return total_pay


if __name__ == "__main__":
    hours = float(input( "Please input the hours:  "))
    wage = float(input("Please input your wage: "))
    print_total = calculate_salary(hours, wage)
    print(" The total pay is : " + str(print_total))
