import lib.ctl as ctl
import os
import ascii_owl

def main():
    ascii_owl.owl()
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
        elif session.current_command == "load_os":
            os.system('cls' if os.name == 'nt' else 'clear')
            session.load_os(session.sliced_line[1])
        elif session.current_command == "wipe":
            os.system('cls' if os.name == 'nt' else 'clear')
            session.wipe()
        else:
            session.next()


main()
