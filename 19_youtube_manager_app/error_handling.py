file = open("./youtube.txt", "w")
# error handling
try:
    file.write("Hello, Rajneesh")
finally:
    file.close()


with open("./19_youtube_manager_app/youtube.txt", "w") as file:
    file.write("Hello")
