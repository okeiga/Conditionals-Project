# Conditionals Project

This repository contains a collection of Python programs that demonstrate the use of conditional statements and user input handling. Each program serves a specific function related to common scenarios.

## Programs

1. **deep.py**
   - Prompts the user for the answer to the Great Question of Life, the Universe and Everything. Outputs "Yes" if the user inputs `42`, `forty-two`, or `forty two` (case-insensitively). Otherwise, outputs "No".

2. **bank.py**
   - Prompts the user for a greeting. Outputs:
     - `$0` if the greeting starts with "hello".
     - `$20` if it starts with an "h" (but not "hello").
     - `$100` for any other greeting.
   - Ignores leading whitespace and treats input case-insensitively.

3. **extensions.py**
   - Prompts the user for a filename and outputs the file's media type based on its suffix:
     - `.gif` → `image/gif`
     - `.jpg` → `image/jpeg`
     - `.jpeg` → `image/jpeg`
     - `.png` → `image/png`
     - `.pdf` → `application/pdf`
     - `.txt` → `text/plain`
     - `.zip` → `application/zip`
   - Outputs `application/octet-stream` for unrecognized suffixes or no suffix at all.

4. **interpreter.py**
   - Prompts the user for an arithmetic expression formatted as `x y z` (where `x` and `z` are integers and `y` is an operator). Outputs the result as a floating-point value formatted to one decimal place.

5. **meal.py**
   - Prompts the user for a time in 24-hour format and outputs whether it’s breakfast, lunch, or dinner time:
     - Breakfast: 7:00 - 8:00
     - Lunch: 12:00 - 13:00
     - Dinner: 18:00 - 19:00
   - Does not output anything for times outside these ranges.

## Usage

To run any of these programs, ensure you have Python installed on your machine. Open a terminal, navigate to the directory where the program is located, and execute the program using the command:

```bash
python filename.py
