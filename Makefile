clean:
	-rm -rf output/*

hdri:
	python3 debevec.py input output

average:
	python3 pixels_average.py

all: clean
