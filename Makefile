clean:
	-rm -rf output/*

rename:
	python3 read_exif.py `ls input/*.jpg`

hdri:
	python3 debevec.py input/ output/

rgb_average:
	python3 matplot_rgb_average.py

rgb_weighted:
	python3 matplot_rgb_weights.py

rgb: rgb_average rgb_weighted

hsv_average:
	python3 matplot_hsv_average.py

hsv_weighted:
	python3 matplot_hsv_weights.py

hsv: hsv_average hsv_weighted

copy_scenery:
	-rm -rf input/*
	cp -rf statyw/dwór/*.JPG input/

copy_inside:
	-rm -rf input/*
	cp -rf statyw/pokój/*.JPG input/

scenery: clean copy_scenery rename hdri rgb hsv

inside: clean copy_inside rename hdri rgb hsv
