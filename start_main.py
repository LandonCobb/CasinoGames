import main

def start(user_money = 10000):
    main.start_main(user_money)

if __name__ == "__main__":
    money = 0
    with open("money.txt", "r") as file:
        money = int(file.readline())
    start(money)