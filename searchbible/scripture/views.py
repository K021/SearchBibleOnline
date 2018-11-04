from django.http import HttpResponse
from django.shortcuts import render


def main(request):
    context = {

    }
    return render(request, 'index.html')


def search_result(request):
    keyword = '잘못된 접근입니다.'
    if request.method == 'POST':
        keyword = request.POST.get('keyword', '')
        if not keyword:
            keyword = '키워드가 입력되지 않았습니다.'
    return HttpResponse(keyword)

