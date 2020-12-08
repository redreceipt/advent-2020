def get_cmds():
    return {i: line.strip() for i, line in enumerate(lines)}


def execute(cmds, safe=False):
    done = []
    line = 0
    acc = 0
    while True:
        try:
            cmd, val = cmds[line].split(" ")
        except KeyError:
            return acc
        if line in done:
            if safe:
                break
            return None
        done.append(line)
        if cmd == "acc":
            acc += int(val)
            line += 1
            continue
        if cmd == "jmp":
            line += int(val)
            continue
        line += 1
    return acc


def one():
    cmds = get_cmds()
    return execute(cmds, True)


def two():
    broken_cmds = get_cmds()
    for line in range(len(broken_cmds)):
        cmds = broken_cmds.copy()
        if "nop" in cmds[line]:
            cmds[line] = cmds[line].replace("nop", "jmp")
        if "jmp" in cmds[line]:
            cmds[line] = cmds[line].replace("jmp", "nop")
        acc = execute(cmds, False)
        if acc:
            return acc


f = open("input.txt")
lines = f.readlines()
print(one())
print(two())
