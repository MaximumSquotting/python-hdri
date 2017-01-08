clean:
	-rm -rf output/*

hdri:
	python3 create_hdri.py input output

average:
	python3 pixels_average.py

all: clean
