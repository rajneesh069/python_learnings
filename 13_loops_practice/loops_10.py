import time

attempts = 0
wait_time = 1
max_tries = 5

while attempts < max_tries:
    print("Attempt:", attempts + 1, " - wait time: ", wait_time)
    time.sleep(wait_time)
    wait_time *= 2
    attempts += 1
