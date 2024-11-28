from runner import Runner
from shared.logger import Logger


def main():
    Logger.setup_logger()
    run = Runner()
    while True:
        run.show_menu()
        choice = input("Введіть номер лабораторної роботи для запуску (або 0 для виходу): ")
        if choice == "0":
            print("Вихід з програми.")
            break
        run.run_lab(choice)


if __name__ == "__main__":
    main()