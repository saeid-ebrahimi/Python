from threading import Lock
# you don't need to use try and don't need to close file
with open("notes.txt","w") as file:
    file.write("some todo...")

# you don't need to aqcuire an release lock
with Lock() as lock:
    pass
