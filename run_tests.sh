
python -c 'from media_button import *; test_volume_up()'

if [ "$USER" = "pi" ]; then
	python -c 'from media_button import *; test_find_button_device("Satechi Media Button")'
fi
