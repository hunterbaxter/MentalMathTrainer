from random import randint
from time import perf_counter
from settings import MAX_TIME, FEEDBACK
from questions import get_question

QUESTION_TYPES = 7

def greeting():
    print("Welcome to Mental Math Trainer\n")


def goodbye():
    print("Goodbye!")


def main():
    greeting()
    game_start_time = perf_counter()
    count_correct = 0
    count_wrong = 0
    while perf_counter() - game_start_time < MAX_TIME:
        question_string, correct_answer = get_question(randint(0, QUESTION_TYPES - 1))
        if float(input(question_string)) == correct_answer:
            count_correct += 1
            if FEEDBACK:
                print(f"Correct Answer")
        else:
            count_wrong += 1
            if FEEDBACK:
                print(f"WRONG: {correct_answer}")
    print(f"Count Correct: {count_correct}")
    print(f"Count Wrong: {count_wrong}")
    goodbye()


if __name__ == "__main__":
    main()
