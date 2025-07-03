from cli import *
from osint import *


clear()
main_banner()
menu()
while True:
	menu = askmenu()
	if processmenu(menu):
		break
