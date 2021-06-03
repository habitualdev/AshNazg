import lib.redis_lib as redis_lib
import readline
import lib.cli as cli
import lib.stringser as stringser


class Session:
    def __init__(self):
        self.server = redis_lib.Server()
        self.server.ping_start()
        comp = cli.Completer()
        readline.set_completer_delims(' \t\n=;')
        readline.parse_and_bind("tab: complete")
        readline.set_completer(comp.complete)
        self.current_command = "entry"
        self.sliced_line = ""

    def welcome(self):
        print("Welcome to the one stringser to find them all")
        print("Commands:\nfind - Search through the DB \nload - Load a new file into the DB \nexit - Exit the script \nwipe - Exit and clear the DB\n\n")
        raw_line = input(">>> ")
        self.sliced_line = raw_line.split()
        self.current_command = self.sliced_line[0]


    def load(self, path):
        stringser.load_strings(str(path))
        self.current_command = "next"

    def next(self):
        print("\nCommands:\nfind - Search through the DB \nload - Load a new file into the DB \nexit - Exit the script \nwipe - Clear the DB\n\n")
        raw_line = input(">>> ")
        self.sliced_line = raw_line.split()
        self.current_command = self.sliced_line[0]

    def find(self):
        self.current_command = "next"
        return self.server.search(str(self.sliced_line[1]))

    def wipe(self):
        self.server.wipe_redis()
        self.current_command = "next"
