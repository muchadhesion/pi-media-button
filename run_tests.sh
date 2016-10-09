
python -c 'from media_button import *; test_volume_up()'
python -c 'from media_button import *; test_radio_play()'

if [ "$USER" = "pi" ]; then
	python -c 'from media_button import *; test_find_button_device("Satechi Media Button")'
fi
