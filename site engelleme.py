#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
isletm_sistemi = os.name

if isletm_sistemi == "nt":
	print("İşletim sistemin Windows")
	dizin = input("Windows hangi disk üzerine kurulu? \n")
	site = input("\nHangi web sitesini engellemek istiyorsun?\n")
	with open(dizin + ":/Windows/System32/drivers/etc/hosts", "a") as hosts:
		hosts.write("\n" + "127.0.0.1 " + site + "\n")
		hosts.close()


elif isletm_sistemi == "posix":
	print("İşletim sisteminiz Linux")

	site = input("\nHangi web sitesini engellemek istiyorsun?\n")
	with open("/etc/hosts", "a") as hosts:
		hosts.write("\n" + "127.0.0.1 " + site + "\n")
		hosts.close()
else:
	print("Bu hata da nereden çıktı?")