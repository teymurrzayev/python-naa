def round_grades(grades: list) -> list:
    rounded = []
    for grade in grades:
        if grade < 38:
            rounded.append(grade)
        else:
            next_multiple = ((grade // 5) + 1) * 5
            if next_multiple - grade < 3:
                rounded.append(next_multiple)
            else:
                rounded.append(grade)
    return rounded