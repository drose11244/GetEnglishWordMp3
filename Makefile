
.PHONY: all

# file= explain_module.py
# file = getEnglishMP3.py
# file = explain.py
file = makeAnkiData.py

all:
	python3 $(file)

file:
	pyinstaller -F $(file)
