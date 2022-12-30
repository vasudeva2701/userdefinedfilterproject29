from django.shortcuts import render

# Create your views here.

def filters(request):
    import datetime
    dt=datetime.date.today()
    d={'data':'HAi DJANgo and PYThoN','dt':dt,'c':1}
    return render(request,'filters.html',d)

def userdefinedfilter(request):
    d={'data':'HI Python HoW R yoU'}
    return render(request,'userdefinedfilter.html',d)