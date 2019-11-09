
.PHONY: all

# file= hello_requests.py
file = getEnglishMP3.py

file:
	pyinstaller -F $(file)

all:
	python3 $(file)
