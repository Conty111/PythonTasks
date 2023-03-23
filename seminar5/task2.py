b = [3,4,5,3,4,5,4,2]
c = []
grade = 0
print("Marks: ", end="")

for i in b:
    if str(i) + " :" + str(b.count(i)) not in c:
        c.append(str(i) + " :" + str(b.count(i)))

for i in b:
    print(i, end=" ")
    if i == 3 or i == 4 or i == 5:
        grade += 1

print("\n"+"; ".join(c))
print("Grade:", (grade/len(b))*100)