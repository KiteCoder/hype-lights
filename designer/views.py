from django.http import JsonResponse
from hypertron import show_builder


def create_show(request):

    # get params from request
    name = request.POST.get('name')

    # run builder
    show_builder.create_show(name)

    return JsonResponse({'Response': 'dummy response, request should be completed'})


def create_frame(request):

    # get params from request
    show_name = request.POST.get('show-name')
    frequency_value = int(request.POST.get('frequency-value'))
    order = int(request.POST.get('order'))
    time = float(request.POST.get('time'))

    # run builder
    show_builder.create_frame(show_name, frequency_value, order, time)

    return JsonResponse({'Response': 'dummy response, request should be completed'})


def create_grid(request):

    # get params from request
    total_rows = int(request.POST.get('total-rows'))
    seats_per_row = int(request.POST.get('seats-per-row'))
    name = request.POST.get('name')

    # run builder
    show_builder.create_grid(total_rows, seats_per_row, name)

    return JsonResponse({'Response': 'dummy response, request should be completed'})


def create_pixel(request):

    # get params from request
    row = int(request.POST.get('row'))
    seat = int(request.POST.get('seat'))
    grid_name = request.POST.get('grid-name')

    # run builder
    show_builder.create_pixel(row, seat, grid_name)

    return JsonResponse({'Response': 'dummy response, request should be completed'})


def create_framepixel(request):

    # get params from request
    row = int(request.POST.get('row'))
    seat = int(request.POST.get('seat'))
    frame_order = int(request.POST.get('frame-order'))
    action = request.POST.get('action')
    show_name = request.POST.get('show-name')

    # run builder
    show_builder.create_framepixel(row, seat, frame_order, action, show_name)

    return JsonResponse({'Response': 'dummy response, request should be completed'})
