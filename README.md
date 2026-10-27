# Student Grade Converter

A simple Python program that converts students' numerical scores into grade categories using Python's built-in `bisect` module. The program processes a dictionary of student names and scores, replaces each numerical score with its corresponding grade, and prints the updated dictionary.

## Features

- Stores student names and numerical scores in a dictionary.
- Uses the `bisect` module to determine grade categories.
- Converts numerical scores into four categories: Fail, Acceptable, Good, and Outstanding.
- Updates the original dictionary with the resulting grades.
- Displays the final dictionary of student names and their grades.

## How to Run

1. Make sure Python 3 is installed on your computer.
2. Save the code in a file named `student_grade_converter.py`.
3. Open a terminal or command prompt.
4. Run the program:

   ```bash
   python student_grade_converter.py
   ```

## Example

**Input data:**

```python
student_scores = {
    "John": 90,
    "Edy": 68,
    "Marry": 88,
    "Ewan": 79,
    "Park": 62
}
```

**Output:**

```python
{
    'John': 'Good',
    'Edy': 'Acceptable',
    'Marry': 'Good',
    'Ewan': 'Acceptable',
    'Park': 'Fail'
}
```

## Grade Categories

| Score | Grade |
|---|---|
| 64 and below | Fail |
| 65–84 | Acceptable |
| 85–100 | Good |
| Above 100 | Outstanding |

**Note:** The actual boundaries in the code are determined by `bisect.bisect(point, score)`. Because the threshold list is `[64, 84, 100]`, scores of 64, 84, and 100 fall into the next category, respectively. Therefore, the table above is a simplified description; the exact behavior is:

- Scores below 64: `Fail`
- Scores from 64 to below 84: `Acceptable`
- Scores from 84 to below 100: `Good`
- Scores of 100 or higher: `Outstanding`

## Concepts Practiced

- **Dictionaries:** Storing and updating student scores.
- **Functions:** Creating `convert_grade()` to handle grade conversion.
- **Loops:** Iterating through student names and updating their values.
- **Modules:** Using Python's built-in `bisect` module.
- **Lists:** Defining score thresholds and their corresponding grade categories.

## Language

Python 3
