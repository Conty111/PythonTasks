from analyser import get_response, make_answer, print_output


def main():
    print("Программа запущена!")
    response_input = get_response()
    while response_input:
        answer = make_answer(response_input)
        print_output(answer)
        response_input = get_response()


if __name__ == "__main__":
    main()
