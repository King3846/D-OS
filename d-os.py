import time
RAM = "120MB"
CPU = "intel core i9-12900"
print("system is starting")
time.sleep(3)
print("RAM = " + RAM)
print("CPU = " + CPU)
time.sleep(2)
print("system is booting")
time.sleep(3)
print("running D-OS 2.0 alpha")
while True:
    enter = input(">>> ")
    if enter == "help":
        print("sysinfo, software update, whoami, shutdown")

    if enter == "sysinfo":
        print("D-OS 2.0 alpha, CPU: intel, storage: 120MB")

    if enter == "software update":
        print("D-OS 2.0 brings a new layout made from scratch. It makes the system faster and easier. The system updates automatically")

    if enter == "whoami":
        print("ADMIN")
      
