import re
original_file = open('main.ab', 'r')
lines = original_file.readlines()

for line in lines:

    result = re.search("^(\s*[a-zA-z0-9(){}\[\]\-;:+=_\"\'.]+\s*)+$", line)

    if result:

        ls = line.split()
        debug_file = open("main.abd", "a")

        for l in ls:
            if ls.index(l) == len(ls) -1:
                if lines.index(line) == len(lines) -1:
                    debug_file.write(l)
                else:
                  debug_file.write(l+"\n")
            else:
               debug_file.write(l+" ")