import time
import random

input("Press enter to start")

wait = random.randint(1, 6)
time.sleep(wait)
start = time.perf_counter()

input("Press enter to stop")

end = time.perf_counter()

print("\nStarted at " + time.strftime("%X", time.localtime(start)))
print("Ended at " + time.strftime("%X", time.localtime(end)))

print("Your reaction time was {} seconds".format(end - start))
