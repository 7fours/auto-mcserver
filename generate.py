#!/usr/bin/env python3
import os
import threading
import time
import argparse

class master():
	parser = argparse.ArgumentParser()
	parser.add_argument('-a', '--auto-start',
		dest='start', 
		help='auto-start minecraft server after generated',
		action='store_true')

	parser.add_argument('-g', '--gui',
		help='enable gui for auto-start (BY DEFAULT OFF, ONLY USE FLAG IF WANTED)',
		dest='gui',
		action='store_true')

	parser.add_argument('-v', '--vanilla',
		dest='vanilla',
		help='create vanilla mc server',
		action='store_true')

	parser.add_argument('-p', '--paper',
		dest='paper',
		help='create papermc server',
		action='store_true')

	parser.add_argument('-f', '--fabric',
		dest='fabric',
		help='create fabric mc server',
		action='store_true')

	parser.add_argument('-c', '--custom',
		dest='custom',
		help='create premade custom server',
		action='store_true'
	)

	parser.add_argument('-l', '--local',
		dest='local',
		help='Local server',
		action='store_true')

	parser.add_argument('-pb', '--public',
		dest='public',
		help='Public server',
		action='store_true'
	)

	parser.add_argument('-ap', '--add-plugins',
		dest='addp',
		help='add custom plugins set without the whole server file',
		action='store_true'
	)

	parser.add_argument('-vr', '--version',
		dest='version',
		help='desired version. by default, set to newest available.\n',
		type=str)
	args = parser.parse_args()


	def main():
		if master.args.custom == True:
			master.paper.custom.setup()

		if master.args.paper == True:
			master.paper.setup()

		if master.args.vanilla == True:
			master.vanilla.setup()

		if master.args.fabric == True:
			master.fabric.setup()

		if master.args.start == True:
			print("server downloaded. now starting..")
			if master.args.gui == True:
				os.system("./start.py --g")
			if master.args.gui == False:
				os.system("./start.py")
		if master.args.addp == True:
			master.paper.custom.plugins()

	def server_props():
		print(" waiting on download...")
		#server.properties download
		os.system("gdown https://drive.google.com/uc?id=1AvgcS9Q7SvlGxrT6Qf4WgX1QGNN9kXn2")
		#eula.txt download
		os.system("gdown https://drive.google.com/uc?id=1AtqU4GK_iE0QdthnEQswXAuq_5BeZpVy")
		print("done")

	class fabric():
		defaultv = 'https://meta.fabricmc.net/v2/versions/loader/1.18.1/0.13.1/0.10.2/server/jar'
		v118 = 'https://meta.fabricmc.net/v2/versions/loader/1.18.1/0.13.1/0.10.2/server/jar'
		v114 = 'https://meta.fabricmc.net/v2/versions/loader/1.14/0.13.1/0.10.2/server/jar'

		def executable():
			print("use start.sh to startup server")
			if master.args.public == True:
				os.system("echo '#!/bin/bash\njava -Xmx6G -Xms6G -jar fabric.jar --nogui' >> start.sh")
				os.system("echo '#!/bin/bash\njava -Xmx6G -Xms6G -jar fabric.jar' >> start_gui.sh")
			if master.args.local == True:
				os.system("echo '#!/bin/bash\njava -Xmx6G -Xms2G -jar fabric.jar --nogui' >> start.sh")
				os.system("echo '#!/bin/bash\njava -Xmx6G -Xms2G -jar fabric.jar' >> start_gui.sh")
			os.system("gdown https://drive.google.com/uc?id=1BbIyIo5qk4WVQYkY7NUfNSsfLopj223N")
			os.system("sudo chmod +x start.py")
			os.system("sudo chmod +x start.sh")
			os.system("sudo chmod +x start_gui.sh")
		def setup():
				#if version != None:
			#	if version == "help" or "h":
			#		print("Versions Available:\n1.14.2\n1.15.2\n1.16.6\n1.18.1")
			#		exit()
			#	elif version == '1.14.2' or '1.14':
			#		#os.system("curl -OJ {}".format(fabric1_14))
			#		print("Downloading fabric1.14.2.jar...")
			#	elif version == '1.18.1' or '1.18':
			#		#os.system("curl -OJ {}".format(fabric1_18))
			#		print("Downloading fabric1.18.1.jar...")
			#if master.args.version == None:
			os.system("curl -OJ {}".format(master.fabric.defaultv))
			print("Downloading fabric 1.18.1.jar...")
			master.server_props()
			master.fabric.executable()

	class paper():
		def executable():
			print("use start.py to startup server")
			if master.args.public == True:
				os.system("echo '#!/bin/bash\njava -Xmx6G -Xms6G -jar Paper_Latest.jar --nogui' >> start.sh")
				os.system("echo '#!/bin/bash\njava -Xmx6G -Xms6G -jar Paper_Latest.jar' >> start_gui.sh")
			if master.args.local == True:
				os.system("echo '#!/bin/bash\njava -Xmx6G -Xms2G -jar Paper_Latest.jar --nogui' >> start.sh")
				os.system("echo '#!/bin/bash\njava -Xmx6G -Xms2G -jar Paper_Latest.jar' >> start_gui.sh")
				os.system("gdown https://drive.google.com/uc?id=1BbIyIo5qk4WVQYkY7NUfNSsfLopj223N")
				os.system("sudo chmod +x start.py")
				os.system("sudo chmod +x start.sh")
				os.system("sudo chmod +x start_gui.sh")
		def setup():
			os.system("gdown https://drive.google.com/uc?id=1Anyd0KD1v6d6heXfV9JfeTkb3Pa3twMg")
			master.server_props()
			master.paper.executable()
		
		class custom():
			def plugins():
				print("waiting on download...\n")
				os.system("gdown https://drive.google.com/uc?id=1BKw6Q4XRueChvmzo-td0v3uiHRai2He8")
				os.system("unzip plugins.zip")
				print("done")
			def setup():
				master.paper.custom.plugins()
				os.system("gdown https://drive.google.com/uc?id=1Anyd0KD1v6d6heXfV9JfeTkb3Pa3twMg")
				master.server_props()
				master.paper.executable()

	class vanilla():
		def setup():
			os.system("gdown https://drive.google.com/uc?id=1Baz9KxRxHRKlFyxFBDmfTQsr62Wd_R68")
			master.server_props()
			master.vanilla.executable()

		def executable():
			print("use start.sh to startup server")
			if master.args.public == True:
				os.system("echo '#!/bin/bash\njava -Xmx6G -Xms6G -jar server.jar --nogui' >> start.sh")
				os.system("echo '#!/bin/bash\njava -Xmx6G -Xms6G -jar server.jar' >> start_gui.sh")
			if master.args.local == True:
				os.system("echo '#!/bin/bash\njava -Xmx6G -Xms2G -jar server.jar --nogui' >> start.sh")
				os.system("echo '#!/bin/bash\njava -Xmx6G -Xms2G -jar server.jar' >> start_gui.sh")
			os.system("gdown https://drive.google.com/uc?id=1BbIyIo5qk4WVQYkY7NUfNSsfLopj223N")
			os.system("sudo chmod +x start.py")
			os.system("sudo chmod +x start.sh")
			os.system("sudo chmod +x start_gui.sh")

master.main()