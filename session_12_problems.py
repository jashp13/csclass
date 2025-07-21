# dynamic_list_processing.py

def task_separator(n):
    print("\n" + "="*10 + f" Task {n} " + "="*10)

if __name__ == "__main__":
    # 1. Prompt user for N integers, load into first_list, display
    task_separator(1)
    first_list = []
    n = int(input("Enter number of items: "))
    for i in range(n):
        val = int(input(f"  Enter integer #{i+1}: "))
        first_list.append(val)
    print("First list:", first_list)

    # 2. Insert 99 at position 1
    task_separator(2)
    first_list.insert(1, 99)
    print("After insert 99 at index 1:", first_list)

    # 3. Replace the 99 with 100
    task_separator(3)
    idx_99 = first_list.index(99)
    first_list[idx_99] = 100
    print("After replace 99→100:", first_list)

    # 4. Create second_list, display, extend first_list, display
    task_separator(4)
    second_list = [500, 600, 700, 800, 900]
    print("Second list:", second_list)
    first_list.extend(second_list)
    print("First list after extend:", first_list)

    # 5. Remove value 800
    task_separator(5)
    first_list.remove(800)
    print("After remove 800:", first_list)

    # 6. Remove the third item (index 2)
    task_separator(6)
    del first_list[2]
    print("After delete index 2:", first_list)

    # 7. Create grades list
    task_separator(7)
    grades = ["A", "B", "C", "A", "A", "C"]
    print("Grades:", grades)

    # 8. Count of "A"
    task_separator(8)
    print("Number of A grades:", grades.count("A"))

    # 9. Index of first "B"
    task_separator(9)
    print("Index of first B grade:", grades.index("B"))

    # 10. Look for "F" without error
    task_separator(10)
    if "F" in grades:
        print("Found F at index", grades.index("F"))
    else:
        print("F is not in the list")

    # 11. Clear (but not delete) second_list, display
    task_separator(11)
    second_list.clear()
    print("Second list after clear:", second_list)

    # 12. Delete second_list and attempt to display
    task_separator(12)
    del second_list
    try:
        print(second_list)
    except NameError as e:
        print("Error displaying second_list:", e)

    # 13. Create players list
    task_separator(13)
    players = ["Rizzo", "Davis", "Baez", "Happ", "Bryan"]
    print("Players:", players)

    # 14. Sort players, display
    task_separator(14)
    players.sort()
    print("Sorted players:", players)

    # 15. Copy to players2, display
    task_separator(15)
    players2 = players.copy()
    print("players2 copy:", players2)

    # 16. Reverse players2, then display both
    task_separator(16)
    players2.reverse()
    print("Original players:", players)
    print("Reversed players2:", players2)
