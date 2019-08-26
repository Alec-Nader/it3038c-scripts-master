#Creating a script which prints disk space utilization
#I will import a tool named PSUTIL which is a python plugin
#PSUtil assists with system monitoring
#PSUtil allows me to create an object which contains system information
#A call to psutil.disk_usage will populate an object with many variable
#This includes a .total, .used, and .free which returns a byte integer
#https://pypi.org/project/psutil
import psutil
#Creating my initial objects from psutil
disk = psutil.disk_usage('/')
mem = psutil.virtual_memory()
#creating memory objects
memtotal = mem.total /(1024 **3)
memused = (mem.used /1024 **3)
memfree = (mem.free /1024 **3)

#Pulling the byte integer for each call and reducing it down to GB
total = (disk.total /(1024 ** 3))
used = disk.used /(1024 **3)
free = disk.free /(1024 **3)
#Formatting the integer to a better representation
totalformat = "{:.2f}".format(total)
usedformat= "{:.2f}".format(used)
freeformat="{:.2f}".format(free)
#Since apparently you cannot add together an INT and a string, I reformatted my formatted int to a string to allow a cleaner visual
diskformat = str(disk.percent)
print(str(totalformat)+"GB Total")
print(str(usedformat)+"GB Used")
print(str(freeformat)+"GB Free")
print (diskformat+"% Utilized")
#Formatting and displaying memory
totalmemformat = "{:.2f}".format(memtotal)
usedmemformat= "{:.2f}".format(memused)
freememformat="{:.2f}".format(memfree)

diskformat = str(disk.percent)
print(str(totalmemformat)+"GB memory Total")
print(str(usedmemformat)+"GB memory Used")
print(str(freememformat)+"GB memory Free")
#Displaying CPU cores, logical vs non
print("CPU cores total:")
print(psutil.cpu_count())
print("CPU cores non-logical:")
print(psutil.cpu_count(logical=False))
#display a list of users on the system
print("Users logged in:")
print(psutil.users())
