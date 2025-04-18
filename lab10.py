# 1) Writing CSV
import csv

with open("students.csv", mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Roll No", "Name", "Subject1", "Subject2", "Subject3"])
    writer.writerow([1, "Alice", 85, 78, 92])
    writer.writerow([2, "Bob", 75, 88, 90])


# 2) Reading CSV and calculating totals
import csv

students = {}

with open("students.csv", mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        total = int(row["Subject1"]) + int(row["Subject2"]) + int(row["Subject3"])
        students[row["Roll No"]] = {
            "name": row["Name"],
            "marks": [int(row["Subject1"]), int(row["Subject2"]), int(row["Subject3"])],
            "total": total
        }

print(students)


# 3) Creating a vCard file
def create_vcard(name, phone, email):
    vcard = f"""BEGIN:VCARD
VERSION:3.0
FN:{name}
TEL;TYPE=CELL:{phone}
EMAIL:{email}
END:VCARD"""
    with open("contact.vcf", "w") as file:
        file.write(vcard)

# Example usage:
create_vcard("John Doe", "+1234567890", "john@example.com")


# 4) Copy file from one directory to another
import os
import shutil

src_dir = "source_dir"
dst_dir = "target_dir"
filename = "example.txt"

os.makedirs(dst_dir, exist_ok=True)
shutil.copy(os.path.join(src_dir, filename), dst_dir)


# 5) Convert file contents to uppercase
with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        outfile.write(line.upper())


# 6) Merge lines alternately from two files
with open("file1.txt", "r") as f1, open("file2.txt", "r") as f2, open("merged.txt", "w") as out:
    lines1 = f1.readlines()
    lines2 = f2.readlines()
    max_len = max(len(lines1), len(lines2))

    for i in range(max_len):
        if i < len(lines1):
            out.write(lines1[i])
        if i < len(lines2):
            out.write(lines2[i])


# 7) Serialize and deserialize Employee object using pickle
import pickle

class Employee:
    def __init__(self, empcode, empname, doj, salary):
        self.empcode = empcode
        self.empname = empname
        self.doj = doj
        self.salary = salary

    def __str__(self):
        return f"{self.empcode}, {self.empname}, {self.doj}, {self.salary}"

emp = Employee("E101", "Alice", "2022-01-10", 55000)

with open("employee.dat", "wb") as file:
    pickle.dump(emp, file)

with open("employee.dat", "rb") as file:
    loaded_emp = pickle.load(file)
    print(loaded_emp)


# 8) Remove articles from a text file using regex
import re

with open("input.txt", "r") as infile, open("output.txt", "w") as outfile:
    for line in infile:
        modified_line = re.sub(r'\b(a|an|the)\b', '', line, flags=re.IGNORECASE)
        outfile.write(modified_line)
