CREATE OR REPLACE FUNCTION count_students_in_dept (
    p_dept IN VARCHAR2
) RETURN NUMBER IS
    v_count NUMBER := 0;
BEGIN
    SELECT COUNT(*)
    INTO v_count
    FROM Student
    WHERE department = p_dept;

    RETURN v_count;
END count_students_in_dept;
/
