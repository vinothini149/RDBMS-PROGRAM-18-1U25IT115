import os
import re
import sys

def run_autograder():
    file_path = "student_code.sql"
    
    if not os.path.exists(file_path):
        print(f"Error: {file_path} not found.")
        sys.exit(1)

    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    # Clean content (strip single-line and multi-line comments)
    content_clean = re.sub(r'--.*', '', content)
    content_clean = re.sub(r'/\*.*?\*/', '', content_clean, flags=re.DOTALL)
    content_upper = content_clean.upper()

    tests = [
        (
            "TC01 - Function 'count_students_in_dept' defined returning NUMBER",
            r"CREATE\s+(OR\s+REPLACE\s+)?FUNCTION\s+COUNT_STUDENTS_IN_DEPT.*RETURN\s+NUMBER"
        ),
        (
            "TC02 - Parameter 'p_dept' declared correctly",
            r"P_DEPT\s+(IN\s+)?VARCHAR2"
        ),
        (
            "TC03 - SELECT COUNT(*) from Student table is used",
            r"SELECT\s+COUNT\s*\(\s*\*?\s*\)\s+INTO\s+\w+\s+FROM\s+STUDENT"
        ),
        (
            "TC04 - WHERE clause matches department with parameter",
            r"WHERE\s+DEPARTMENT\s*=\s*P_DEPT"
        ),
        (
            "TC05 - RETURN statement is present",
            r"RETURN\s+\w+\s*;"
        ),
        (
            "TC06 - Valid PL/SQL BEGIN...END block exists",
            r"BEGIN[\s\S]+END(\s+COUNT_STUDENTS_IN_DEPT)?\s*;"
        )
    ]

    score = 0
    total = len(tests)

    print("\n--- RUNNING AUTOGRADER ---")
    for name, pattern in tests:
        if re.search(pattern, content_upper, re.IGNORECASE | re.DOTALL):
            print(f"PASS: {name}")
            score += 1
        else:
            print(f"FAIL: {name}")

    print("-" * 30)
    print(f"TOTAL SCORE: {score}/{total}")
    print("-" * 30)

    if score < total:
        print("AUTOGRADER RESULT: FAIL")
        sys.exit(1)
    else:
        print("AUTOGRADER RESULT: PASS")
        sys.exit(0)

if __name__ == "__main__":
    run_autograder()
