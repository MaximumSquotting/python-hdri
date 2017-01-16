clean:
	-rm -rf output/*

hdri:
	python3 debevec.py input output

pixels_average:
	python3 pixels_average.py

hsv_average:
	python3 hsv_average.py

copy_scenery:
	-rm -rf input/*
	cp -rf statyw/dwór/*.JPG input/

copy_inside:
	-rm -rf input/*
	cp -rf statyw/pokój/*.JPG input/

all: clean
