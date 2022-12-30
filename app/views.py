from django.shortcuts import render

# Create your views here.


def filters(request):
    data='Hai PYThon and Django'
    

    import datetime
    dt=datetime.date.today()


    d={'data':data,'dt':dt,'c':1}
    return render(request,'filters.html',d)
def userdefinedfilters(request):

    data='Hai pyThon how are You'
    d={'data':data}
    return render(request,'userdefinedfilters.html',d)
