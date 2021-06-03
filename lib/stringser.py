import re
import lib.redis_lib as redis_lib

def load_strings(file):
    count = 1
    n = 1
    nn = 1
    r = redis_lib.Server()
    string_match = re.compile("[\w\d$\\/]+")
    with open(file, errors="ignore") as f:
        reading = True
        while reading:
            line = f.readline()
            if line:
                strings_raw = string_match.findall(line)
                for string_slice in strings_raw:
                    r.add_string(str(string_slice),str(n) + "." + str(nn))
                    nn = nn + 1
                    count = count + 1
                n = n + 1
                print("\rLines read: " + str(n) + " | Strings Found: " + str(count), flush=True, end="")
                nn = 1

            else:
                reading = False


