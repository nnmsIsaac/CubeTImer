import time

def time_solve(times):
    start = time.time()
    input("hit [enter] to stop the timer")
    end = time.time()
    times.append(end - start)

    print("time: {}".format(times[-1]))
    stats(times)
    return times

def stats(times):
    best = min(times)
    worst = max(times)
    average = sum(times) / len(times)
    solves = len(times)
    print("best: {}".format(best),
          "worst: {}".format(worst),
          "average: {}".format(average),
          "solves: {}".format(solves),
          sep="\n")

    if len(times) >= 5:
        last = times[-5:]
        middle = sorted(last)[1:4]
        print("aol5: {}".format(sum(middle) / 3))

    for aol in [10, 50, 100, 500, 1000]:
        if len(times) >= aol:
            last = times[-aol:]
            print("aol{}: {}".format(aol, sum(last) / aol))
        else:
            break

    return times

def top(times):
    print(*[str(time) for time in sorted(times)[:5]], sep="\n")
    return times

def all_times(times):
    print(*[str(time) for time in times], sep="\n")
    return times

def manual(times):
    time = input("manually add a time >>>")
    try:
        times.append(time)
    except:
        print("that isn't a valid time (try again by typing 'manual')")

def delete(times):
    print("deleted last time")
    return times[:-1]

def add_2(times):
    times[-1] += 2

    print("time is now {}".format(times[-1]))
    return times

def sub_2(times):
    times[-1] -= 2

    print("time is now {}".format(times[-1]))
    return times

def save(times):
    global save_file
    with open(save_file, "w") as data:
        data.write("\n".join([str(time) for time in times]))

    return times

def load(times):
    global save_file
    with open(save_file, "r") as data:
        return [float(time) for time in data.read().split()]

def list_help(times):
    global actions
    print(*[actions[action][1] for action in actions], sep="\n")

    return times

# function, command, description
actions = {
    "":       (time_solve, "hit [enter] to start/stop the timer"),
    "help":   (list_help,  "type 'help' to see this block of text again"),
    "stats":  (stats,      "type 'stats' to view your stats"),
    "top":    (top,        "type 'top' to view your top 5 times"),
    "times":  (all_times,  "type 'times' to list every signle time on record"),
    "manual": (manual,     "type 'manual' to manually add a time"),
    "+2":     (add_2,      "type '+2' to add 2 to your last time"),
    "-2":     (sub_2,      "type '-2' to subtract 2 from your last time"),
    "del":    (delete,     "type 'del' to delete your last time"),
    "save":   (save,       "type 'save' to save your times"),
    "load":   (load,       "type 'load' to reload your saved times (this is done automatically)"),
    "q":      (None,       "type 'q' to quit"),
}

save_file = "speedcube.txt"
times = load(save_file)

list_help(times)

while True:
    print()

    while True:
        command = input(">>> ")
        if command in actions:
            break
        print("not a valid command, please try again (or type 'help')\n")

    if command == "q":
        break

    times = actions[command][0](times)
    save(times)
