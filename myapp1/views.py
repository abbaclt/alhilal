from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('I am ready')
def home2(request):
    return HttpResponse('<h1>hloooooo2222222222222</h1>')
def home3(request):
    return render(request,'index.html')
def home4(request):
        return HttpResponse('<h1>boys<h1>')
def calculator(request):
    return render(request,'calc.html')

def calculatorfun(request):
    a=int(request.GET['n1'])
    b=int(request.GET['n2'])
    sum=a+b

    # div=a/b
    # diff=a-b
    # mul=a*b
    #print'<inputt ype="text" name="n" value=%"s">'%(a+b)

    #print(sum)
    return render(request,'calc.html',({'sum':sum}))


def calc3(request):
    if(request.method=="POST"):
        a=int(request.POST['n1'])
        b=int(request.POST['n2'])
        sum=a+b

        return render(request,'calc1.html',({'sum':sum}))


    else:
        return render(request,'calc1.html')



