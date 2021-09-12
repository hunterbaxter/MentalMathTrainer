from random import randint, uniform
from difficulty import MIN_ADD, MAX_ADD, MIN_SUB, MAX_SUB, MIN_MULT,\
    MAX_MULT, MIN_DIV, MAX_DIV, DEC_PLACES_ADD, DEC_PLACES_SUB, MIN_2_POW,\
    MAX_2_POW

def get_question(question_type: int):
    match question_type:
        case 0:
            return get_int_multiplication_question()
        case 1:
            return get_int_addition_question()
        case 2:
            return get_int_subtraction_question()
        case 3:
            return get_int_division_question()
        case 4:
            return get_double_addition_question()
        case 5:
            return get_double_subtraction_question()
        case _:
            return get_power_2_question()

def get_int_multiplication_question():
    x = randint(MIN_MULT, MAX_MULT)
    y = randint(MIN_MULT, MAX_MULT)
    return f"{x} * {y} = ", x * y

def get_int_division_question():
    x = randint(MIN_MULT, MAX_MULT)
    y = randint(MIN_MULT, MAX_MULT)
    z = x * y
    return f"{z} / {x} = ", y

def get_int_addition_question():
    x = randint(MIN_ADD, MAX_ADD)
    y = randint(MIN_ADD, MAX_ADD)
    return f"{x} + {y} = ", x + y

def get_double_addition_question():
    x = round(uniform(MIN_ADD, MAX_ADD), DEC_PLACES_ADD)
    y = round(uniform(MIN_ADD, MAX_ADD), DEC_PLACES_ADD)
    return f"{x} + {y} = ", x + y

def get_int_subtraction_question():
    x = randint(MIN_ADD, MAX_ADD)
    y = randint(MIN_ADD, MAX_ADD)
    return f"{x} - {y} = ", x - y

def get_double_subtraction_question():
    x = round(uniform(MIN_SUB, MAX_SUB), DEC_PLACES_SUB)
    y = round(uniform(MIN_SUB, MAX_SUB), DEC_PLACES_SUB)
    return f"{x} - {y} = ", x - y

def get_power_2_question():
    x = randint(MIN_2_POW, MAX_2_POW)
    return f"2^{x} = ", pow(2,x)

