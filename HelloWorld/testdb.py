
from django.http import HttpResponse
from testModel.models import Test

def testdb(request):
    test1 =Test(name="w3c")
    test1.save()
    return HttpResponse("<p>添加数据成功</p>")