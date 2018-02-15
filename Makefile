.PHONY: doc clean


doc: asciiimage/*
	PYTHONPATH=. pdoc --html --html-dir doc asciiimage

clean:
	rm doc/* -rf

