import os

if os.name == "nt":
	print("İşletim sistemin Windows")
	dizin = "C:/Windows/System32/drivers/etc/hosts"

elif os.name == "posix":
    print("İşletim sistemin Linux")
    dizin = "/etc/hosts"

site = input("\nHangi web sitesini engellemek istiyorsun?\n")
with open(dizin, "a") as hosts:
    hosts.write("\n" + "127.0.0.1 " + site)
    hosts.close()
