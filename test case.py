#นายปิยภัทร คงเจริญวุฒิ 6630202503 S19
from datetime import datetime
import itertools

tester = input("Enter Taster Name : ")

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


def bva(min_v, max_v):
    mid = (min_v + max_v) // 2
    return [min_v, min_v + 1, mid, max_v - 1, max_v]

def robustness(min_v, max_v):
    mid = (min_v + max_v) // 2
    return [min_v - 1, min_v, min_v + 1, mid, max_v - 1, max_v, max_v + 1]

testcases = set()
w_nom = (w_min + w_max) // 2
h_nom = (h_min + h_max) // 2

while True:

    if choice == 1:
        W_values = bva(w_min, w_max)
        H_values = bva(h_min, h_max)

        for w in W_values:
            testcases.add((w, h_nom))
        for h in H_values:
            testcases.add((w_nom, h))
        break

    elif choice == 2:
        W_values = robustness(w_min, w_max)
        H_values = robustness(h_min, h_max)

        for w in W_values:
            testcases.add((w, h_nom))
        for h in H_values:
            testcases.add((w_nom, h))
        break

    elif choice == 3:
        W_values = bva(w_min, w_max)
        H_values = bva(h_min, h_max)

        for w, h in itertools.product(W_values, H_values):
            testcases.add((w, h))
        break

    elif choice == 4:
        W_values = robustness(w_min, w_max)
        H_values = robustness(h_min, h_max)

        for w, h in itertools.product(W_values, H_values):
            testcases.add((w, h))
        break

    else:
        print("❌ Invalid choice! Please select 1-4")
        choice = int(input("Choice : "))



testcases = sorted(list(testcases))

filename = "ExecuteLog.txt"
count = 0

with open(filename, "w", encoding="utf-8") as file:
    file.write(f"Tester Name : {tester}\n")
    file.write(f"DateTime Generate : {datetime.now()}\n")
    file.write("Loop :\n")

    for i, (w, h) in enumerate(testcases, start=1):

        if choice in (2, 4) and (w < w_min or w > w_max or h < h_min or h > h_max):
            area = "ERROR"
        else:
            area = (w * h) / 2

        file.write(f"{i}, W = {w}, H = {h}, Area = {area}\n")
        count += 1

    file.write(f"DateTime finish : {datetime.now()}\n")
    file.write(f"Total number of test case : {count}\n")

print("\nGenerate ExecuteLog.txt Completed")
print("Total Test Case : ", count)