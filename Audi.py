rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

sections = {
    'a': [[0] * columns for _ in range(rows)],
    'b': [[0] * columns for _ in range(rows)],
    'c': [[0] * columns for _ in range(rows)]
}

def print_sections():
    print(f"{'Section A':<20} {'Section B':<20} {'Section C':<20}")
    for i in range(rows):
        row_a = " ".join(map(str, sections['a'][i]))
        row_b = " ".join(map(str, sections['b'][i]))
        row_c = " ".join(map(str, sections['c'][i]))
        print(f"{row_a:<20} {row_b:<20} {row_c:<20}")

while True:
    section = input("Enter which section you want (a/b/c or 'exit' to stop): ").lower()
    if section == "exit":
        break
    if section not in sections:
        print("Choose a valid section (a, b, or c).")
        continue

    try:
        row = int(input("Enter row number (starting from 1): ")) - 1
        column = int(input("Enter column number (starting from 1): ")) - 1
        if 0 <= row < rows and 0 <= column < columns:
            sections[section][row][column] = 1
        else:
            print("Row or column out of range.")
    except ValueError:
        print("Please enter valid numbers.")

    print_sections()
