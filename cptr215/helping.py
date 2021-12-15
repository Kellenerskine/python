# def final_grade(exam, hw):
#     """
#     >>> print(final_grade(90, 90))
#     90
#     >>> print(final_grade(90, 100))
#     92
#     """
#     if exam >= 50:
#         if hw <= 75:
#             return final_grade(exam * 0.76+hw * 0.25)
#     else:
#         return final_grade(exam * 1)

def final_grade(exam, hw):
    """
    >>> print(final_grade(90, 70))
    90
    >>> print(final_grade(90, 100))
    92
    """
    if exam >= 50 and hw <= 75:
        return (exam / 76) + (hw / 25)
    else:
        return exam * 1
