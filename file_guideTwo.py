import fnmatch
import os

def list_files():
	for file in os.listdir('.'):
		if fnmatch.fnmatch(file, "*.txt"):
			print("Text files: ", file)

		if fnmatch.fnmatch(file, "*.yml"):
			print("Yaml files: ", file)

		if fnmatch.fnmatch(file, "*.py"):
			print("Python files: ", file)

list_files()