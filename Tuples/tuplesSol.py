'''
Python Assignment
Tuples
'''
# Easy

#Q1
def swap_pairs(t):
    swapped = []
    i = 0
    while i < len(t) - 1:
        swapped.append(t[i + 1])  
        swapped.append(t[i])      
        i += 2
    if len(t) % 2 == 1:
        swapped.append(t[-1])     
    return tuple(swapped)

#q2
def get_stats(numbers):
    total = 0
    for num in numbers:
        total += num
    minimum = min(numbers)
    maximum = max(numbers)
    average = total / len(numbers)
    return (minimum, maximum, total, average)

# Medium
#Q1
from collections import namedtuple
Student = namedtuple('Student', ['name', 'age', 'grades'])
def top_student(students):
    highest_avg = 0
    top = None
    for s in students:
        avg = sum(s.grades) / len(s.grades)
        if avg > highest_avg:
            highest_avg = avg
            top = s
    return top

#Q2
def count_coordinate_occurrences(coords):
    result = {}
    for coord in coords:
        if coord in result:
            result[coord] += 1
        else:
            result[coord] = 1
    return result

# Hard
#Q1
def group_by_department(employees):
    dept_info = {}
    for name, dept, salary in employees:
        if dept not in dept_info:
            dept_info[dept] = {'total': 0, 'count': 0, 'names': []}
        dept_info[dept]['total'] += salary
        dept_info[dept]['count'] += 1
        dept_info[dept]['names'].append(name)

    result = {}
    for dept in dept_info:
        avg_salary = dept_info[dept]['total'] // dept_info[dept]['count']
        names = dept_info[dept]['names']
        result[dept] = (avg_salary, names)
    return result

#Q2
def flatten_tuple(t):
    flat = []
    for item in t:
        if isinstance(item, tuple):
            flat += flatten_tuple(item)  # recursive call
        else:
            flat.append(item)
    return tuple(flat)

# -----------------------------
#    OUTPUTS
# -----------------------------
if __name__ == "__main__":

#-------------- easy -----------------
#Q1
    print(swap_pairs((1, 2, 3, 4)))       
    print(swap_pairs((1, 2, 3)))          
#q2
    print("\nGet Stats:")
    print(get_stats([1, 2, 3, 4, 5]))     




#-------------- medium -----------------
#q1
    alice = Student("Alice", 20, (85, 90, 95))
    bob = Student("Bob", 19, (70, 80, 90))
    charlie = Student("Charlie", 21, (90, 92, 93))
    print(top_student([alice, bob, charlie]))

#Q2
    coords = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
    print(count_coordinate_occurrences(coords))  




#-------------- hard -----------------
#Q1
    employees = [
        ("Alice", "Engineering", 80000),
        ("Bob", "Marketing", 70000),
        ("Charlie", "Engineering", 90000),
        ("Diana", "HR", 65000),
        ("Eve", "Marketing", 75000)
    ]
    print(group_by_department(employees))

#Q2
    nested = (1, (2, 3), (4, (5, 6)), 7)
    print(flatten_tuple(nested))  
