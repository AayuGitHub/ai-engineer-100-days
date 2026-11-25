people = [("Asha", 28, "Pune"), ("Ravi", 35, "Delhi"), ("Meera", 22, "Pune"),
          ("Kabir", 41, "Delhi"), ("Zoya", 28, "Mumbai")]

# expected = [("Kabir", 41, "Delhi"), ("Ravi", 35, "Delhi"), ("Zoya", 28, "Mumbai"),
#             ("Asha", 28, "Pune"), ("Meera", 22, "Pune")]

print(sorted(people, key=lambda person: (person[2], -person[1])))