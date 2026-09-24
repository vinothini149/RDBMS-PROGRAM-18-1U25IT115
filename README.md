# Assignment 18: Count Students by Department Function

## Objective
Write a PL/SQL stored function named `count_students_in_dept` that accepts a department name and returns the total number of students in that department.

## Requirements
1. **Function Name:** `count_students_in_dept`
2. **Input Parameter:** `p_dept` (VARCHAR2)
3. **Return Type:** `NUMBER`
4. **Action:** Perform a `SELECT COUNT(*)` query filtering by `department = p_dept` and return the total count.
5. **File Name:** Complete your solution inside `student_code.sql`.

## Scoring Criteria
Your submission will be evaluated automatically using the following test cases:
- `TC01`: FUNCTION definition and correct return type (`RETURN NUMBER`).
- `TC02`: Parameter declaration (`p_dept`).
- `TC03`: `SELECT COUNT(*)` aggregated query on `Student`.
- `TC04`: Correct `WHERE` condition matching `department` to `p_dept`.
- `TC05`: Presence of `RETURN` statement inside the execution block.
- `TC06`: Valid PL/SQL `BEGIN ... END;` block structure.
