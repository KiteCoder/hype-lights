from django.http import JsonResponse
from show import show


def get_config_json(request):

    # get params from request
    row = int(request.POST.get('row'))
    seat = int(request.POST.get('seat'))
    name = request.POST.get('name')


    return JsonResponse(show.build_config_json(row, seat, name))
    try:
        return JsonResponse(show.build_config_json(row, seat, name))
    except:
        return JsonResponse({'Error': 'internal service error'})


