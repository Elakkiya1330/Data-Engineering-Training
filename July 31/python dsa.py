# Section 1: Nested Lists & Access
students = [
    ["Ravi", [85, 72, 90]],
    ["Sneha", [95, 88, 92]],
    ["Kabir", [65, 70, 60]],
    ["Anita", [75, 80, 78]]
]

# 1. Ravi’s second mark
print("Ravi’s second mark:", students[0][1][1])

# 2. Average mark for each student
for name, marks in students:
    avg = sum(marks) / len(marks)
    print(f"{name}'s average: {avg}")

# 3. Students who scored above 80 in all subjects
for name, marks in students:
    if all(mark > 80 for mark in marks):
        print(f"{name} scored >80 in all subjects")

# 4. New list of [name, average]
avg_list = [[name, round(sum(marks)/len(marks),2)] for name, marks in students]
print("Name & Average List:", avg_list)

# Section 2: Dictionary of Lists
data = {
    "products": ["Mobile", "Laptop", "Tablet", "Camera"],
    "prices": [12000, 55000, 18000, 25000],
    "ratings": [4.5, 4.7, 4.0, 4.2]
}

# 1. Create list of dictionaries
product_list = [{"name": n, "price": p, "rating": r}for n, p, r in zip(data["products"], data["prices"], data["ratings"])
]
print("Product List:", product_list)

# 2. Filter: price > 20000 and rating >= 4.5
filtered = [p for p in product_list if p["price"] > 20000 and p["rating"] >= 4.5]
print("Filtered Products:", filtered)

# 3. Sort by rating (descending)
sorted_products = sorted(product_list, key=lambda x: x["rating"], reverse=True)
print("Sorted by Rating:", sorted_products)

# Section 3: Frequency Dictionary + Set Operations
text = "ai is the future and ai will change everything in the ai world"

# 1. Word frequency
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print("Frequency:", freq)

# 2. Words that appear more than once
print("Repeated Words:", [word for word, count in freq.items() if count > 1])

# 3. Sorted unique words
unique_sorted = sorted(set(text.split()))
print("Unique Words:", unique_sorted)

# 4. Common words between sets
set1 = set(text.split())
set2 = {"ai", "ml", "data", "future"}
print("Common Words:", set1 & set2)

# Section 4: Dictionary Comprehension + Conditional Logic
sales = {
    'Amit': 70000,
    'Sneha': 45000,
    'Ravi': 30000,
    'Anita': 90000,
    'Kabir': 20000
}

# 1. Add 10% bonus
bonus_sales = {k: v * 1.10 for k, v in sales.items()}
print("With Bonus:", bonus_sales)

# 2. Filter sales > 50k
filtered_sales = {k: v for k, v in sales.items() if v > 50000}
print("Sales > 50k:", filtered_sales)

# 3. Label as High/Medium/Low
labels = {k: 'High' if v >= 75000 else 'Medium' if v >= 40000 else 'Low' for k, v in sales.items()}
print("Labels:", labels)

# Section 5: Tuples, Sets, and Zipping
names = ("Ravi", "Sneha", "Kabir")
marks = (88, 92, 76)

# 1. Zip to dictionary
zipped = dict(zip(names, marks))
print("Zipped:", zipped)

# 2. Min/Max marks
print("Min:", min(marks), "Max:", max(marks))

# 3. Set from marks + new value
mark_set = set(marks)
mark_set.add(100)
print("Updated Set:", mark_set)

# 4. Merge 2 sets
extra_set = {90, 85, 76}
merged = mark_set | extra_set
print("Merged Unique Set:", merged)

# Bonus Challenge
employees = {
    "E101": {"name": "Ravi", "dept": "Sales", "salary": 50000},
    "E102": {"name": "Sneha", "dept": "Engineering", "salary": 80000},
    "E103": {"name": "Kabir", "dept": "HR", "salary": 45000}
}

# 1. Add E104
employees["E104"] = {"name": "Anita", "dept": "Engineering", "salary": 85000}

# 2. Increase Engineering salary by 10%
for emp in employees.values():
    if emp["dept"] == "Engineering":
        emp["salary"] *= 1.10

# 3. Department with highest average salary
from collections import defaultdict
dept_salaries = defaultdict(list)
for emp in employees.values():
    dept_salaries[emp["dept"]].append(emp["salary"])
avg_salaries = {dept: sum(sals)/len(sals) for dept, sals in dept_salaries.items()}
highest = max(avg_salaries, key=avg_salaries.get)
print("Department with highest avg salary:", highest)
