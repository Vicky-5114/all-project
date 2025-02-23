from argparse import ArgumentParser


def main(args):
    username = args.username
    password = args.password

    while True:
        print("########### Welcome to login system ###########")
        user_input = input("[r]: register, [l]: login, [q]: quit\n>>> ")
        if user_input == "r":
            username = input("usename: ")
            password = input("password: ")
            print("[INFO] Rregister success!")
        elif user_input == "l":
            if username is None or password is None:
                print("[WARNING] Please register first!")
                continue
            input_usename = input("usename: ")
            input_password = input("password: ")
            if input_usename == username and input_password == password:
                print("[INFO] Login success!")
            else:
                print("[WARNING] Login failed!")
        elif user_input == "q":
            break
        else:
            print("[ERROR] Invalid input!")


if __name__ == "__main__":

    arg_parser = ArgumentParser()
    arg_parser.add_argument("--username", type=str, help="Input Username", default=None)
    arg_parser.add_argument("--password", type=str, help="Input Password", default=None)
    arg_parser.add_argument("--n", type=int, help="Number", default=None)
    args = arg_parser.parse_args()

    print(args.n)

    # main(args)
