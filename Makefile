
.PHONY: all

file= hello_requests.py
# file = getEnglishMP3.py
# file = explain.py

all:
	python3 $(file)

file:
	pyinstaller -F $(file)
