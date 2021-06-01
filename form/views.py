from django.shortcuts import redirect, render
from .models import Form
from django.http import HttpResponse, JsonResponse
# Create your views here.

def form(request):
    if request.method=="POST" and request.is_ajax:
        img_name = request.POST['image-name']
        image = request.FILES.get('image')  # multivalued dict
        print(image)
        if(img_name == "" or image is None):
            return JsonResponse({"errors":"Fields cannot be empty"}, status=400)
        elif(Form.objects.filter(name=img_name).exists()):
            return JsonResponse({"errors":"Image name already exists"}, status=400)
        else:
            form = Form(name=img_name, img=image)
            form.save()
            return JsonResponse({"msg":"AJAX: Saved Successfully"})
    else:
        return render(request, 'home.html') 
            