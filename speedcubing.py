import time as timer

def calc_average(times):
    return sum(times) / len(times)

def calc_ao5(times):
    times =  times[-5:]
    times.remove(min(times))
    times.remove(max(times))
    return calc_average(times)

def calc_best(times):
    return min(times)

def calc_stats(times):
    if len(times) < 5:
        return None, None, None
    best = calc_best(times)
    average = calc_average(times)
    ao5 = calc_ao5(times)
    return best, average, ao5

def read(file_name):
    with open(file_name, "r") as data:
        return [float(time) for time in data.read().split()]

def save(file_name, times):
    with open(file_name, "w") as data:
        data.write("\n".join([str(time) for time in times]))

file_name = "speedcube.txt"
times = read(file_name)

instructions = """
hit [enter] to start/stop the timer
type 'del' then hit [enter] to delete your last time
type 'times' then hit [enter] to view your times
type '+2' then hit [enter] to add 2 seconds to your last time
type '-2' then hit [enter] to subtract two seconds from your last time
type 'manual' then hit [enter] to manually add a time
type 'top' then hit [enter] to view your 5 best times
type 'q' then hit [enter] to quit"""

print(instructions)

actions = ["", "del", "times", "+2", "-2", "manual", "top" ,"q"]

while True:
    best, average, ao5 = calc_stats(times)
    print("best: {} \naverage: {} \nao5: {}\n".format(best, average, ao5))

    while True:
        action = input(">>> ")
        if action in actions:
            break
        print("invalid action, please try again")

    if action == "":
        start = timer.time()
        input("hit [enter] to stop >>> ")
        end = timer.time()
        time = end - start
        print("time: {}".format(time))
        times.append(time)
    if action == "del":
        times = times[:-1]
    if action == "times":
        print("\n".join([str(time) for time in times]))
    if action == "+2":
        times[-1] += 2
    if action == "-2":
        times[-1] -= 2
    if action == "manual":
        try:
            time = float(input("enter time manually >>> "))
            times.append(time)
        except:
            print("invalid time, type 'manual' then hit [enter] to try again")
    if action == "top":
        print(*[str(time) for time in sorted(times)[0:5]], sep="\n")
    if action == "q":
        break

    save(file_name, times)
