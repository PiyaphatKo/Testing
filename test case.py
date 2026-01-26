from datetime import datetime
import itertools

# -------------------------------
# รับข้อมูลจากผู้ใช้
# -------------------------------
tester = input("Tester Name : ")

w_min = int(input("Wide Min : "))
w_max = int(input("Wide Max : "))
h_min = int(input("Height Min : "))
h_max = int(input("Height Max : "))

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
# เลือกเทคนิค (ตัดซ้ำด้วย set)
# -------------------------------
testcases = set()
w_nom = (w_min + w_max) // 2
h_nom = (h_min + h_max) // 2

if choice == 1:  # BVA
    W_values = bva(w_min, w_max)
    H_values = bva(h_min, h_max)

    for w in W_values:
        testcases.add((w, h_nom))
    for h in H_values:
        testcases.add((w_nom, h))

elif choice == 2:  # Robustness
    W_values = robustness(w_min, w_max)
    H_values = robustness(h_min, h_max)

    for w in W_values:
        testcases.add((w, h_nom))
    for h in H_values:
        testcases.add((w_nom, h))

elif choice == 3:  # Worst Case
    W_values = bva(w_min, w_max)
    H_values = bva(h_min, h_max)

    for w, h in itertools.product(W_values, H_values):
        testcases.add((w, h))

elif choice == 4:  # Worst Case Robustness
    W_values = robustness(w_min, w_max)
    H_values = robustness(h_min, h_max)

    for w, h in itertools.product(W_values, H_values):
        testcases.add((w, h))

else:
    print("Invalid choice")
    exit()

# แปลง set → list และเรียงลำดับ
testcases = sorted(list(testcases))

# -------------------------------
# เขียนไฟล์ ExecuteLog
# -------------------------------
filename = "ExecuteLog.txt"
count = 0

with open(filename, "w", encoding="utf-8") as file:
    file.write(f"Tester Name : {tester}\n")
    file.write(f"DateTime Generate : {datetime.now()}\n")
    file.write("Loop :\n")

    for i, (w, h) in enumerate(testcases, start=1):

        # เงื่อนไข Robustness → ERROR
        if choice in (2, 4) and (w < w_min or w > w_max or h < h_min or h > h_max):
            area = "ERROR"
        else:
            area = (w * h) / 2

        file.write(f"{i}, W={w}, H={h}, Area={area}\n")
        count += 1

    file.write(f"DateTime finish : {datetime.now()}\n")
    file.write(f"Total number of test case : {count}\n")

print("\nGenerate ExecuteLog.txt Completed")
print("Total Test Case :", count)
