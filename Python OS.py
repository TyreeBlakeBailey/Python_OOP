import os, sys, datetime, math
print(os.cpu_count())
print(datetime.datetime.now())

print(math.remainder(93, 9))

class System_path:

working_dir = os.getcwd()
print(f"This is your current working dir {working_dir}")

system_path = sys.path
print(f"This is your path {system_path}")

def current_system_path():
    print("This is your path ")
    return sys.path


def working_dir():
    print("This is your current dir")
    return os.getcwd()


print(working_dir())
print(current_system_path())
