"""
Tasks:

Parse it and print each employee's name and department
Find the average salary per department
Find all employees who know Python

Hint: import xml.etree.ElementTree as ET — this is Python's built-in XML parser. No pip install needed.
"""

import xml.etree.ElementTree as ET


def main():
    employees = []
    with open("./employees.xml", "r") as f:
        content = f.read()
        root = ET.fromstring(content)
        employeeElements = root.findall("employee")
        for empEle in employeeElements:
            nameAtt = empEle.find("name")
            # just to bypass pyright
            employees.append(nameAtt.text if nameAtt else "N/A")
    print(employees)


if __name__ == "__main__":
    main()
