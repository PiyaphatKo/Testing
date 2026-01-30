# นายปิยภัทร คงเจริญวุฒิ 6630202503 S19
from datetime import datetime
import itertools

# -------------------------------
# รับข้อมูลจากผู้ใช้
# -------------------------------
tester = input("Enter Tester Name : ")

w_min = int(input("Enter Wide Min : "))
w_max = int(input("Enter Wide Max : "))
h_min = int(input("Enter Height Min : "))
h_max = int(input("Enter Height Max : "))

print("\nSelect Test Design Technique")
print("1. BVA")
print("2. Robustness")
print("3. Worst Case")
print("4. Worst Case Robustness")
choice = int(input("Choice : "))

# -------------------------------
# ฟังก์ชันสร้างค่า test
# -------------------------------
def bva(min_v, max_v):
    mid = (min_v + max_v) // 2
    return [min_v, min_v + 1, mid, max_v - 1, max_v]

def robustness(min_v, max_v):
    mid = (min_v + max_v) // 2
    return [min_v - 1, min_v, min_v + 1, mid, max_v - 1, max_v, max_v + 1]

# -------------------------------
# เตรียมตัวแปร
# -------------------------------
testcases = set()
w_nom = (w_min + w_max) // 2
h_nom = (h_min + h_max) // 2

# -------------------------------
# เลือกเทคนิค (วนซ้ำถ้าเลือกผิด)
# -------------------------------
while True:

    if choice == 1:  # BVA
        tc_prefix = "BVA"
        tech_name = "Boundary Value Analysis (BVA)"
        W_values = bva(w_min, w_max)
        H_values = bva(h_min, h_max)

        for w in W_values:
            testcases.add((w, h_nom))
        for h in H_values:
            testcases.add((w_nom, h))
        break

    elif choice == 2:  # Robustness
        tc_prefix = "ROB"
        tech_name = "Robustness Testing"
        W_values = robustness(w_min, w_max)
        H_values = robustness(h_min, h_max)

        for w in W_values:
            testcases.add((w, h_nom))
        for h in H_values:
            testcases.add((w_nom, h))
        break

    elif choice == 3:  # Worst Case
        tc_prefix = "WC"
        tech_name = "Worst Case Testing"
        W_values = bva(w_min, w_max)
        H_values = bva(h_min, h_max)

        for w, h in itertools.product(W_values, H_values):
            testcases.add((w, h))
        break

    elif choice == 4:  # Worst Case Robustness
        tc_prefix = "WCR"
        tech_name = "Worst Case Robustness Testing"
        W_values = robustness(w_min, w_max)
        H_values = robustness(h_min, h_max)

        for w, h in itertools.product(W_values, H_values):
            testcases.add((w, h))
        break

    else:
        print("❌ Invalid choice! Please select 1-4")
        choice = int(input("Choice : "))

# -------------------------------
# เรียง Test Case
# -------------------------------
testcases = sorted(list(testcases))

# -------------------------------
# เขียนไฟล์ ExecuteLog
# -------------------------------
filename = "ExecuteLog.txt"
count = 0

with open(filename, "w", encoding="utf-8") as file:
    file.write(f"Tester Name : {tester}\n")
    file.write(f"Test Design Technique : {tech_name}\n")
    file.write(f"DateTime Generate : {datetime.now()}\n")
    file.write("Loop :\n")

    for i, (w, h) in enumerate(testcases, start=1):

        tc_id = f"{tc_prefix}-{i:02d}"

        # Robustness → Invalid Input = ERROR
        if choice in (2, 4) and (w < w_min or w > w_max or h < h_min or h > h_max):
            area = "ERROR"
        else:
            area = (w * h) / 2

        file.write(
            f"{tc_id}, W = {w}, H = {h}, Area = {area}\n"
        )
        count += 1

    file.write(f"DateTime finish : {datetime.now()}\n")
    file.write(f"Total number of test case : {count}\n")

print("\nGenerate ExecuteLog.txt Completed")
print("Total Test Case :", count)
