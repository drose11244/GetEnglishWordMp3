
.PHONY: all

# file= explain_module.py
# file = getEnglishMP3.py
file = freedom.py
# file = makeAnkiData.py

all:
	python3 $(file)

file:
	pyinstaller -F $(file)
