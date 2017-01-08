clean:
	-rm -rf output/*

hdri:
	python create_hdri.py input output

average:
	python pixels_average.py

all: clean
