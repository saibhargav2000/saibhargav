import pyttsx3
import os


while True:
	print("chat me with ur requirements: ",end='')
	p=input()
	

	if("run" in p) and ("chrome" in p):
		os.system("chrome")

	elif(("run" in p) or ("execute" in p)) or (("notepad" in p) or ("editor" in p)):
		os.system("notepad")

	elif(("windows" in p) and ("media" in p)) and ("player" in p):
		os.system("wmplayer")

	elif(("vlc" in p) or ("open" in p)) or (("vlc" in p) and ("player" in p)):
		os.system("vlc")

	elif(("acrobat" in p) or ("reader" in p)) or (("pdf" in p) and ("viewer" in p)):
		os.system("acrord32")

	elif("start" in p) and ("excel" in p):
		os.system("excel")

	elif(("waves" in p) or ("3d sound" in p)) or (("maxaudio" in p) or ("audio control" in p)):
		os.system("WavesSvc64")

	elif(("mca" in p) or ("antivirus" in p)) or (("security check" in p) or ("scan virus" in p)):
		os.system("McUICnt")

	elif("start" in p) and ("msedge" in p):
		os.system("msedge")

	elif(("drive" in p) or ("backup" in p)):
		os.system("OneDrive")

	elif("notes" in p) or ("notebook" in p):
		os.system("ONENOTE")
	
	elif("start" in p) and ("RiotClientServices" in p):
		os.system("RiotClientServices")

	elif(("start" in p) and ("powerpoint" in p)) or ("ppt" in p):
		os.system("powerpnt")


	elif("exit" in p) or ("quit" in p):
		break

	else:
			print("dont support")
	
	