from django.shortcuts import render

# Create your views here.
def create(request):
   
    return render(request, 'requests\create_request.html')

def list(request):
    
    # blog_list = Post.objects.order_by("-published_date")[:5]
    # context = {"blog_list": blog_list}
    
    return render(request, 'requests\\request_list.html')


# def content_blog(request, blog_id):
#     # response = "Вы смотрите каждый блог по отдельности %s."
#     one_blog = Post.objects.get(id = blog_id)
#     context = {"one_blog": one_blog}
   
#     # return HttpResponse(response % blog_id)
#     return render(request, "oneblog.html", context)   