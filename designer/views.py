from django.http import JsonResponse
from hypertron import show_builder
from django.shortcuts import render, redirect
from xml.dom import minidom


def create(request):
  # return HttpResponse("Hello world, you have arrived at the index page" )

  print("testing if this prints")

  return render(request, 'create.html',)

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


def path_extracter():

    svg_file = "/static/Regions_de_France.svg"
    # svg_file = "filename"

    doc = minidom.parse(svg_file)  # parseString also exists
    path_strings = [path.getAttribute('d') for path
                    in doc.getElementsByTagName('path')]
    doc.unlink()

    print('the url worked')

    print(path_strings)

    return path_strings

    # svg = open("static/Regions_de_France.svg")
    # for line in svg:
    #     if line.startswith("<path"):
        
        # scribble=open("scrib1.txt")
        # for line in scribble:
        #     if line.startswith("<polygon"):
        #         rightline=line.split('"')
        # commas=rightline[13].split(' ') 
        # newlist=[]
        # for i in commas:
        #     tup=i.split(',')
        #     newlist.append((tup[0],tup[1]))

    








