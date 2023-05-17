from data import DATA_OUTPUT, DATA_ANALYS
from games import ricroll, russian_game


def main():
    print("Программа запущена!")
    response_input = get_response()
    while response_input:
        answer = make_answer(response_input)
        print_output(answer)
        response_input = get_response()


def make_answer(response) -> list:
    output = []
    for word in response:
        value = check_text(word)
        if value:
            if DATA_OUTPUT[value] == "game":
                russian_game()
                output.append("Хорошая игра)))")
            elif DATA_OUTPUT[value] == "ricroll":
                ricroll()
                output.append("Вас зарикроллили\n")
            elif DATA_OUTPUT[value] not in output:
                output.append(DATA_OUTPUT[value])
    if not output:
        output.append("Не понимаю вас...")
    return output


def check_text(text: str) -> str:
    for word in DATA_ANALYS.keys():
        if word in text.lower():
            return DATA_ANALYS[word]


def get_response() -> list:
    response = input("Что вы хотите?!\n").split()
    return response


def print_output(answer: list):
    for output in answer:
        if type(output) is str:
            print(f"{output}")
        else:
            for val in output.items():
                print(f"{val[0]}: {val[1]}")
        print()
