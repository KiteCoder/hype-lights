## Show Functions

from show import models

def create_show(name):

    # create object
    show = models.Show()
    show.name = name
    show.save()


def create_frame(show_name, frequency_value, order, time):

    # find Parent Show
    show = models.Show.objects.get(name=show_name)

    # create object
    frame = models.Frame()
    frame.frequency_value = frequency_value
    frame.time = time
    frame.order = order
    frame.show = show
    frame.save()


def create_grid(total_rows, seats_per_row, name):

    # create object
    grid = models.Grid()
    grid.total_rows = total_rows
    grid.seats_per_row = seats_per_row
    grid.name = name
    grid.save()


def create_pixel(row, seat, grid_name):

    # find Parent Grid
    grid = models.Grid.objects.get(name=grid_name)

    # create object
    pixel = models.Pixel()
    pixel.row = row
    pixel.seat = seat
    pixel.grid = grid
    pixel.save()


def create_framepixel(row, seat, frame_order, action, show_name):

    # find Parent Pixel
    pixel = models.Pixel.objects.filter(row=row).get(seat=seat)

    # find Parent Show
    show = models.Show.objects.get(name=show_name)

    # find Parent Frame
    frame = models.Frame.objects.filter(show=show).get(order=frame_order)

    # create object
    framePixel = models.FramePixel()
    framePixel.action = action
    framePixel.pixel = pixel
    framePixel.frame = frame
    framePixel.save()

