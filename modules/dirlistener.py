import os 

def run(**args):
	print '[*] DirListener Module.'
	files = os.listdir('.')
	return files
