
.PHONY: all

# file= explain_module.py
# file = getEnglishMP3.py
# file = freedom.py
file = makeAnkiData.py
# 
all:
	python3 $(file)

package:
	pyinstaller -F $(file)
	echo $(file)

clean:
	rm -rf *.spec
