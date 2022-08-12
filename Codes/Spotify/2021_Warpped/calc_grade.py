def get_grade():
    grade_dict = {
        "a": 10,
        "a-": 9,
        "b": 8,
        "b-": 7,
        "c": 6,
        "c-": 5,
        "d": 4,
        "e": 2,
        "f": 0,
    }
    sum_grade = 0
    subjects = [
        "Classical Mechanics",
        "Mathematical Physics",
        "Quantum Mechanics",
        "Electronics",
        "Lab",
    ]
    print("Press 'Q' anytime to escape!")
    for subject in subjects:
        while True:
            subject_grade = input(f"Enter your {subject} Grade: ").lower()
            if subject_grade == "q":
                print("Exiting!")
                return None
            if subject_grade in grade_dict.keys():
                num_grade = grade_dict[subject_grade]
                sum_grade += num_grade
                break
            else:
                print("Please provide a valid grade.")
                print(f"Valid grades are: {', '.join(grade_dict.keys()).upper()}")
    total_grade = sum_grade / len(subjects)
    grade = round(total_grade, 2)
    print(f"Your Average Grade Point is: {grade}")


if __name__ == "__main__":
    get_grade()
