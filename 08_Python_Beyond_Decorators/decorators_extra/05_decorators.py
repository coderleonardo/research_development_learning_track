import time

# Define our decorator
def execution_time(func):
    def wrapper():
        # Calculate the running time
        t0 = time.time()
        func()
        t = time.time()

        # Formats the message that will be shown on the screen
        print("[{func}] Execution time is: {total_time}".format(
            func=func.__name__,
            total_time=str(t - t0))
        )

    return wrapper

# Decorate the function with the decorator
# @execution_time is equivalent to call execution_time(main)
@execution_time
def main():
    for n in range(0, 10000000):
        pass

# Execute the main function
main()