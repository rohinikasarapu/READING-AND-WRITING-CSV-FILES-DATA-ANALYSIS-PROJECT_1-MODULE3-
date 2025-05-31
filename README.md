# Rice University Data Analysis Course — Module 3 Project 1: CSV Utilities

This repository contains Python CSV utility functions developed as part of the first project in Module 3 of the Rice University Data Analysis course on Coursera.

The utilities are designed for string-based CSV parsing and generation, suitable for environments like CodeSkulptor that require handling CSV data without file I/O.

## Project Overview

In this project, we implement a set of CSV parsing and writing functions that work with CSV data provided as strings. These functions include:

- Reading CSV field names
- Parsing CSV data into a list of dictionaries
- Parsing CSV data into a nested dictionary keyed by a specified field
- Writing a list of dictionaries back to a CSV string format

These utilities facilitate processing CSV data for data analysis tasks in restricted coding environments.

## Functions

1. `read_csv_fieldnames_from_string(csv_text, separator)`  
   Extracts the header field names from a CSV-formatted string.

2. `read_csv_as_list_dict_from_string(csv_text, separator)`  
   Parses CSV string into a list of dictionaries, where each dictionary corresponds to a row.

3. `read_csv_as_nested_dict_from_string(csv_text, keyfield, separator)`  
   Parses CSV string into a nested dictionary keyed by the specified field.

4. `write_csv_from_list_dict_to_string(table, fieldnames, separator)`  
   Converts a list of dictionaries back to a CSV formatted string.

## Example Usage

```python
csv_text = "name,age,city\nAlice,23,New York\nBob,30,Chicago\nCharlie,27,San Francisco"

# Get field names
fields = read_csv_fieldnames_from_string(csv_text, ",")
print("Fields:", fields)

# Parse CSV to list of dictionaries
table = read_csv_as_list_dict_from_string(csv_text, ",")
print("Table:", table)

# Parse CSV to nested dictionary using 'name' as key
nested = read_csv_as_nested_dict_from_string(csv_text, "name", ",")
print("Nested dict:", nested)

# Convert list of dictionaries back to CSV string
csv_output = write_csv_from_list_dict_to_string(table, ["name", "age", "city"], ",")
print("CSV Output:\n", csv_output)
