from django.shortcuts import render

def index1(request):
    return render(request,'form_page.html')

def index2(request):
    context = {
        'name':request.POST['name'],
        'location':request.POST['location'],
        'language':request.POST['language'],
        'comment':request.POST['comment'],
        'gender':request.POST['gender'],
        'education':request.POST['education'],
    }
    return render(request,'result_page.html',context)

