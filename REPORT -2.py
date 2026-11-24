
import tkinter as tk
from tkinter import ttk


# 1. Input Relation Matrix
matrix = []

print("Enter a 5x5 relation matrix (0 or 1):")

for i in range(5):
    while True:
        row = input(f"Enter row {i+1}: ").split()

        if len(row) != 5:
            print("Invalid input! Enter exactly 5 values.")
            continue

        try:
            row = list(map(int, row))

            if all(value in [0, 1] for value in row):
                matrix.append(row)
                break
            else:
                print("Please enter only 0 or 1.")

        except ValueError:
            print("Please enter valid integers.")


# 2. Check Reflexive Property
def is_reflexive(matrix):
    for i in range(5):
        if matrix[i][i] != 1:
            return False
    return True


# 3. Check Symmetric Property
def is_symmetric(matrix):
    for i in range(5):
        for j in range(5):
            if matrix[i][j] != matrix[j][i]:
                return False
    return True


# 4. Check Transitive Property
def is_transitive(matrix):
    for i in range(5):
        for j in range(5):
            for k in range(5):
                if matrix[i][j] == 1 and matrix[j][k] == 1:
                    if matrix[i][k] != 1:
                        return False
    return True


# 5. Check Equivalence Relation
def is_equivalence(matrix):
    return (
        is_reflexive(matrix)
        and is_symmetric(matrix)
        and is_transitive(matrix)
    )


# 6. Find Equivalence Classes
def equivalence_classes(matrix):
    visited = set()
    classes = []

    for i in range(5):
        if i not in visited:
            current_class = []

            for j in range(5):
                if matrix[i][j] == 1:
                    current_class.append(j + 1)
                    visited.add(j)

            classes.append(current_class)

    return classes


# 7. Reflexive Closure
def reflexive_closure(matrix):
    result = [row[:] for row in matrix]

    for i in range(5):
        result[i][i] = 1

    return result


# 8. Symmetric Closure
def symmetric_closure(matrix):
    result = [row[:] for row in matrix]

    for i in range(5):
        for j in range(5):
            if result[i][j] == 1:
                result[j][i] = 1

    return result


# 9. Transitive Closure
def transitive_closure(matrix):
    result = [row[:] for row in matrix]

    for k in range(5):
        for i in range(5):
            for j in range(5):
                if result[i][k] == 1 and result[k][j] == 1:
                    result[i][j] = 1

    return result


# 10. Calculate Properties
reflexive = is_reflexive(matrix)
symmetric = is_symmetric(matrix)
transitive = is_transitive(matrix)
equivalence = is_equivalence(matrix)

reflexive_result = reflexive_closure(matrix)
symmetric_result = symmetric_closure(matrix)
transitive_result = transitive_closure(matrix)


# Graphical Matrix Display
def display_matrix(parent, matrix, title):

    section = tk.LabelFrame(
        parent,
        text=title,
        font=("Arial", 9, "bold"),
        padx=5,
        pady=5,
        bg="#F2F2F2"
    )
    section.pack(side="left", padx=5, pady=5)

    # Column numbers
    for j in range(5):
        tk.Label(
            section,
            text=str(j + 1),
            width=2,
            font=("Arial", 8, "bold"),
            bg="#F2F2F2"
        ).grid(row=0, column=j + 1, padx=1, pady=1)

    # Matrix rows and values
    for i in range(5):

        tk.Label(
            section,
            text=str(i + 1),
            width=2,
            font=("Arial", 8, "bold"),
            bg="#F2F2F2"
        ).grid(row=i + 1, column=0, padx=1, pady=1)

        for j in range(5):

            color = "#B7E4C7" if matrix[i][j] == 1 else "#FFFFFF"

            cell = tk.Label(
                section,
                text=str(matrix[i][j]),
                width=2,
                height=1,
                font=("Arial", 9, "bold"),
                bg=color,
                relief="solid",
                borderwidth=1
            )

            cell.grid(row=i + 1, column=j + 1, padx=1, pady=1)


# 12. Graphical Application
root = tk.Tk()
root.title("Relation Matrix Analyzer")
root.geometry("900x650")
root.configure(bg="#F2F2F2")

main_title = tk.Label(
    root,
    text="RELATION MATRIX ANALYZER",
    font=("Arial", 15, "bold"),
    bg="#F2F2F2",
    fg="#263238"
)
main_title.pack(pady=8)


# Properties Section
properties_frame = tk.LabelFrame(
    root,
    text="Relation Properties",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=5,
    bg="#F2F2F2"
)
properties_frame.pack(pady=5)

properties = [
    ("Reflexive", reflexive),
    ("Symmetric", symmetric),
    ("Transitive", transitive),
    ("Equivalence Relation", equivalence)
]

for name, result in properties:
    color = "#2E7D32" if result else "#C62828"

    tk.Label(
        properties_frame,
        text=f"{name}: {'YES' if result else 'NO'}",
        font=("Arial", 9, "bold"),
        fg=color,
        bg="#F2F2F2"
    ).pack(anchor="w", pady=1)


# Equivalence Classes
if equivalence:
    classes_text = "Equivalence Classes: " + str(
        equivalence_classes(matrix)
    )
else:
    classes_text = "Not an Equivalence Relation"

tk.Label(
    root,
    text=classes_text,
    font=("Arial", 10, "bold"),
    bg="#F2F2F2",
    fg="#333333"
).pack(pady=5)


# Original Matrix
original_frame = tk.Frame(root, bg="#F2F2F2")
original_frame.pack()

display_matrix(original_frame, matrix, "Original Matrix")


# Closure Matrices
closure_frame = tk.Frame(root, bg="#F2F2F2")
closure_frame.pack()

display_matrix(
    closure_frame,
    reflexive_result,
    "Reflexive Closure"
)

display_matrix(
    closure_frame,
    symmetric_result,
    "Symmetric Closure"
)

display_matrix(
    closure_frame,
    transitive_result,
    "Transitive Closure"
)


# Closure Properties
results_frame = tk.LabelFrame(
    root,
    text="Closure Properties",
    font=("Arial", 9, "bold"),
    padx=10,
    pady=5,
    bg="#F2F2F2"
)
results_frame.pack(pady=8)

closure_data = [
    ("Reflexive Closure", reflexive_result),
    ("Symmetric Closure", symmetric_result),
    ("Transitive Closure", transitive_result)
]

for name, result in closure_data:
    text = (
        f"{name}: "
        f"Reflexive={is_reflexive(result)}, "
        f"Symmetric={is_symmetric(result)}, "
        f"Transitive={is_transitive(result)}"
    )

    tk.Label(
        results_frame,
        text=text,
        font=("Arial", 8),
        bg="#F2F2F2"
    ).pack(anchor="w", pady=1)


# Close Button
tk.Button(
    root,
    text="Close",
    command=root.destroy,
    font=("Arial", 9, "bold"),
    bg="#37474F",
    fg="white",
    padx=12,
    pady=3
).pack(pady=5)


root.mainloop()
 