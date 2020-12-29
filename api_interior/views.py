from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import interior , login
from .serializers import interiorSerializer , loginSerializer


@csrf_exempt
def interior_list(request):
    if request.method == 'GET':
        articles = interior.objects.all()
        serializer = interiorSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def create_interior(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = interiorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def login_list(request):
    if request.method == 'GET':
        articles = login.objects.all()
        serializer = loginSerializer(articles, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def create_user(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = loginSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def article_detail(request, pk):
    """
    Retrieve, update or delete article.
    """
    try:
        inter = interior.objects.get(pk=pk)
    except interior.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = interiorSerializer(inter)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = interiorSerializer(inter, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        inter.delete()
        return HttpResponse(status=204)