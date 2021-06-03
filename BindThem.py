import lib.ctl as ctl
import os


def main():
    session = ctl.Session()
    os.system('cls' if os.name == 'nt' else 'clear')
    session.welcome()
    while session.current_command != "exit":
        if session.current_command == "load":
            os.system('cls' if os.name == 'nt' else 'clear')
            session.load(session.sliced_line[1])
        elif session.current_command == "find":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(session.find())
        elif session.current_command == "wipe":
            os.system('cls' if os.name == 'nt' else 'clear')
            session.wipe()
        else:
            session.next()


main()
