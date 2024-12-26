from django.http.response import HttpResponse


# Create your views here.


def submit(request):
    f = open(r"F:\projects\beifan\submit.html", encoding='utf-8')
    html = f.read()
    return HttpResponse(html)


def result(request):
    f = open(r"F:\projects\beifan\result.html", encoding='utf-8')
    html = f.read()
    return HttpResponse(html, status=404)
