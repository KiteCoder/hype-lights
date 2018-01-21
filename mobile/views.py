from django.http import JsonResponse
from show import config_builder


def get_config_json(request):

    # get params from request
    row = int(request.POST.get('row'))
    seat = int(request.POST.get('seat'))
    name = request.POST.get('name')

    try:
        return JsonResponse(config_builder.build_config_json(row, seat, name))
    except:
        return JsonResponse({'Error': 'internal service error'})
