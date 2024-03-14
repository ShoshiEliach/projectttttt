import ctypes
import random


# Load the shared library
lib = ctypes.CDLL("C:\\Users\\User\\Documents\\projecttt\\Threads\\main.so")

# Define the function prototype
add_value = lib.addValueToList
add_value.argtypes = [ctypes.c_int]


remove_value = lib.deleteLastAfterDelay

waiters_now=lib.waiters
waiters_now.restype = ctypes.c_int


# Call the C++ function from Python
while True:
    x=random.randrange(0,2)
    add_value(x)

    thread = threading.Thread(target=remove_value)
    thread.start()
    mone = waiters_now()
    print(mone)



