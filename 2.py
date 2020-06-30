student = {
    "Tom": {"A": 30, "B": 97, "C": 84, "D": 89, "E": 91, },
    "Sbody": {"A": 96, "B": 70, "C": 33, "D": 53, "E": 66, },
    "Rekkles": {"A": 45, "B": 22, "C": 99, "D": 96, "E": 97, },
    "HHH": {"A": 75, "B": 82, "C": 69, "D": 60, "E": 74, },
}
for name, grade in student.items():
    print("\n姓名:" + name + "\t\t" + "A:%d" % grade["A"] + "\t" + "B:%d" % grade["B"] + "\t" + "C:%d" % grade[
        "C"] + "\t" + "D:%d" % grade["D"] + "\t" + "E:%d" % grade["E"])

name = input("请输入学生的姓名:")
print("姓名:" + name + "\t\t" + "A:%d" % student[name]["A"] + "\t" + "B:%d" % student[name]["B"] + "\t" + "C:%d" %
      student[name]["C"] + "\t" + "D:%d" % student[name]["D"] + "\t" + "E:%d" % student[name]["E"])
sum=0
min=100
max=0
for subject, grade in student[name].items():

    sum += grade
    if min >grade:
        min = grade
    if max <grade:
        max = grade
ave = sum / 5
print(max)
print(min)
print(ave)