
.PHONY: all

# file= hello_requests.py
file = getEnglishMP3.py

make:
	python3 $(file)
build:
	pyinstaller -F $(file)