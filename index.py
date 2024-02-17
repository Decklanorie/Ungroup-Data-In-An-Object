def ungroup_students(students):
    result = []
    for student in students:
        mapped_data = [{"teacher": student["teacher"], **d} for d in student.get("data", [])]
        result.extend(mapped_data)
    return result
