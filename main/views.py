from django.shortcuts import render
from .models import ShortURL
from .forms import create_new_short_URL
from  datetime import datetime
import random,string

# Create your views here.
def home(request):
    context = {"rows":ShortURL.objects.all()}
    return render(request,'home.html',context)

def create(request):
    if request.method =='POST':
        form = create_new_short_URL(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['original_URL'] 
            cur_obj = ShortURL.objects.filter(original_URL=original_website)
            if len(cur_obj)!=0:
                return render(request, 'redirect.html',{'obj':cur_obj[0]})
            random_chars_list = list(string.ascii_letters)
            random_chars = ''
            for i in range(6):
                random_chars += random.choice(random_chars_list)
            while len(ShortURL.objects.filter(short_URL=random_chars ))!=0:
                for i in range(6):
                    random_chars += random.choice(random_chars_list)
    
            d= datetime.now()
            s = ShortURL(original_URL= original_website,short_URL= random_chars, time_date_created= d  )
            s.save()
            return render(request,'UrlCreated.html',{'chars':random_chars})
    else:
        form = create_new_short_URL()
        context = {'form':form}
        return render(request,'create.html',context)

def redirect(request, url):
    cur_obj = ShortURL.objects.filter(short_URL= url )
    if len(cur_obj) == 0:
        return render(request,'pageNotFound.html')
    context = {'obj':cur_obj[0]}
    return render(request, 'redirect.html',context)


