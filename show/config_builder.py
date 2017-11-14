## Show Functions

from show import models

## Build  Config String
## When users request config string it will be built dynamically, We can adjust the position of the logic if we need to

def build_config_json(row, seat, name):

	''' Create JSON Response variable '''
	configJson = {}

	''' Select Show by Name '''
	show = models.Show.objects.get(name=name)

	''' Select Pixel by row, seat '''
	pixel = models.Pixel.objects.filter(row=row).get(seat=seat)

	''' Get Frames for show '''
	frames = models.Frame.objects.filter(show=show)

	''' For each frame, get the action for the pixel '''
	for frame in frames:

		''' Get frame pixel for frame '''
		framePixel = models.FramePixel.objects.filter(frame=frame).get(pixel=pixel)
		
		'''Add frame frequency as key and action as value to config json'''
		configJson[frame.frequency_value] = framePixel.action


	''' Return built config string '''
	return (configJson)