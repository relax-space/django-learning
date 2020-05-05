from django.http import HttpResponse
from django.shortcuts import render
from django.template.context_processors import csrf

# 表单
def search_form(request):
   return render(request,'search_form.html',None)

def search(request):
    request.encoding ="utf-8"
    print(request.GET)
    if "q" in request.GET:
        message = "你搜索的内容为："+request.GET['q']
    else:
        message ="你提交了空表单"
    return HttpResponse(message)

# def post_form(request):
#    return render(request,'post_form.html',None)

def search_post(request):
    ctx={}
    ctx.update(csrf(request))
    if request.POST:
        ctx["rlt"] = request.POST['q']
    return render(request,"post.html",ctx)