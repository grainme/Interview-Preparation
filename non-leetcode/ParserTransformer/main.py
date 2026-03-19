"""
Problem:
    a script that reads this file and outputs:

    Average salary per department
    The highest-paid employee in each department
    Departments where average salary is above 60,000

"""

import csv


class EmployeeSalary:
    def __init__(self, employee: str, salary: int) -> None:
        self.employee = employee
        self.salary = salary


class DepartmentStat:
    def __init__(
        self, sum_salaries: int, number_of_emps: int, highest_paid_emp: EmployeeSalary
    ) -> None:
        self.sum_salaries = sum_salaries
        self.number_of_emps = number_of_emps
        self.highest_paid_emp = highest_paid_emp


def main():
    dep_stats: dict[str, DepartmentStat] = {}

    with open("./employees.csv", "r") as f:
        # using csv is better and safer than splitting stuff manually...
        reader = csv.reader(f)
        next(reader)

        for row in reader:
            if not row:
                continue
            employee, dep, salary = row
            salary = int(salary)

            if dep not in dep_stats:
                dep_stats[dep] = DepartmentStat(0, 0, EmployeeSalary("", 0))

            # track sum of salaries (for AVG)
            dep_stats[dep].sum_salaries += salary
            dep_stats[dep].number_of_emps += 1

            # tracking highest paid employee
            if salary > dep_stats[dep].highest_paid_emp.salary:
                dep_stats[dep].highest_paid_emp = EmployeeSalary(employee, salary)

    res = []
    above6 = []
    for dep in dep_stats:
        dep_stat = dep_stats[dep]
        avg_salary = dep_stat.sum_salaries // dep_stat.number_of_emps
        res.append((dep, avg_salary, dep_stat.highest_paid_emp.employee))
        if avg_salary > 60000:
            above6.append(dep)

    print(res, above6, sep="\n---\n")


if __name__ == "__main__":
    main()
