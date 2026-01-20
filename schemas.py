
# Инновационный алгоритм (внутри backend)
def get_gap_analysis(user_grades: dict, target_uni_avg: dict):
    # Сравниваем профиль пользователя с "идеальным" профилем вуза
    gaps = {}
    for subject, grade in target_uni_avg.items():
        user_grade = user_grades.get(subject, 0)
        if user_grade < grade:
            gaps[subject] = grade - user_grade
    return gaps # Возвращает список "пробелов", которые нужно закрыть
