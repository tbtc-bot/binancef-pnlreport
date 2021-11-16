from sys import platform

# COSTANTI

#definisco una costante in base al sistema operativo in uso per l'adattamento dei datetime
if platform == "linux" or platform == "linux2":
    # linux
    DATETIME_SO_ADAPT = 1
elif platform == "darwin":
    # OS X
    DATETIME_SO_ADAPT = 1000
elif platform == "win32":
    # Windows...
    DATETIME_SO_ADAPT = 1