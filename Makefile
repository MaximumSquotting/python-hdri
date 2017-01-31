clean_output:
	-rm -rf output/*
	
clean_input:
	-rm -rf input/*

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
	cp -rf statyw/dwór/*.JPG input/

copy_inside:
	cp -rf statyw/pokój/*.JPG input/
	
copy_memorial:
	cp -rf memorial/*.jpg input/
	
copy_cave:
	cp -rf cave/* input/
	
copy_chinese_garden:
	cp -rf chinese_garden/* input/
	
copy_kluki:
	cp -rf kluki/* input/
	
copy_mountains:
	cp -rf mountains/* input/

copy_ostrow_tumski:
	cp -rf ostrow_tumski/* input/

scenery: clean_output clean_input copy_scenery rename hdri rgb hsv

inside: clean_output clean_input copy_inside rename hdri rgb hsv

memorial: clean_output clean_input copy_memorial rgb hsv

cave: clean_output clean_input copy_cave rename hdri rgb hsv

chinese_garden: clean_output clean_input copy_chinese_garden rename hdri rgb hsv

kluki: clean_output clean_input copy_kluki rename hdri rgb hsv

mountains: clean_output clean_input copy_mountains rename hdri rgb hsv

ostrow_tumski: clean_output clean_input copy_ostrow_tumski rename hdri rgb hsv
