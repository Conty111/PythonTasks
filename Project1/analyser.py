from data import DATA_OUTPUT, DATA_ANALYS


def make_answer(response) -> list:
    output = []
    for word in response:
        value = check_text(word)
        if value:
            if DATA_OUTPUT[value] not in output:
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


def print_output(answer: list) -> str:
    for output in answer:
        if type(output) is str:
            print(f"{output}")
        else:
            for val in output.items():
                print(f"{val[0]}: {val[1]}")
        print()
