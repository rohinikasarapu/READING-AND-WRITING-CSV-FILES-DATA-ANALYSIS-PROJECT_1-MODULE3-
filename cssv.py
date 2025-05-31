# CSV Utilities for CodeSkulptor (string-based parsing)

# 1. Read field names
def read_csv_fieldnames_from_string(csv_text, separator):
    lines = csv_text.strip().split('\n')
    fieldnames = lines[0].split(separator)
    return fieldnames

# 2. Read as list of dictionaries
def read_csv_as_list_dict_from_string(csv_text, separator):
    lines = csv_text.strip().split('\n')
    fieldnames = lines[0].split(separator)
    data = []
    for line in lines[1:]:
        values = line.split(separator)
        row = {}
        for i in range(len(fieldnames)):
            row[fieldnames[i]] = values[i]
        data.append(row)
    return data

# 3. Read as nested dictionary
def read_csv_as_nested_dict_from_string(csv_text, keyfield, separator):
    lines = csv_text.strip().split('\n')
    fieldnames = lines[0].split(separator)
    nested = {}
    for line in lines[1:]:
        values = line.split(separator)
        row = {}
        for i in range(len(fieldnames)):
            row[fieldnames[i]] = values[i]
        nested[row[keyfield]] = row
    return nested

# 4. Write list of dictionaries to CSV string
def write_csv_from_list_dict_to_string(table, fieldnames, separator):
    output = separator.join(fieldnames) + "\n"
    for row in table:
        row_values = []
        for field in fieldnames:
            value = row[field]
            # Quote non-numeric values
            if not value.replace('.', '', 1).isdigit():
                value = '"' + value + '"'
            row_values.append(value)
        output += separator.join(row_values) + "\n"
    return output

# ========== Example usage ==========
csv_text = "name,age,city\nAlice,23,New York\nBob,30,Chicago\nCharlie,27,San Francisco"

# Fieldnames
print("Fields:", read_csv_fieldnames_from_string(csv_text, ","))

# List of dictionaries
table = read_csv_as_list_dict_from_string(csv_text, ",")
print("Table (List of Dicts):", table)

# Nested dictionary
nested = read_csv_as_nested_dict_from_string(csv_text, "name", ",")
print("Nested Dict:", nested)

# Convert back to CSV
csv_output = write_csv_from_list_dict_to_string(table, ["name", "age", "city"], ",")
print("CSV Output:\n" + csv_output)
