from django.http import JsonResponse
from .models import *
    

def getLligues(request):
    jsonData = list( Lliga.objects.all().values() )
    return JsonResponse({
            "status": "OK",
            "lliguesObj": jsonData,
        }, safe=False)

def getLligues(request):
    jsonData = list( Lliga.objects.all().values() )
    return JsonResponse({
            "status": "OK",
            "lliguesObj": jsonData,
        }, safe=False)

def getEquips(request,lliga_id):
    lliga = Lliga.objects.get(pk=lliga_id)
    jsonData = list(lliga.equips.values())
    return JsonResponse({
            "status": "OK",
            "EquipsObj": jsonData,
        }, safe=False)