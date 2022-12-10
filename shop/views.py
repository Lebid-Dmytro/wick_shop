from django.shortcuts import render
from django.views import View
from django.views.generic import ListView


from shop.models import Wick, User


class WickView(View):
    '''Вивід товарів'''
    def get(self, request):
        wick = Wick.objects.order_by('price')
        context = {'wick': wick,}
        return render(request, 'wick_list.html', context)


class WickInfo(View):
    def get(self, request, slug):
        info = Wick.objects.get(url=slug)

        contex = {'info': info, }

        return render(request, 'wick_detail.html', contex)


class SingIN(View):
    def get(self, request):
        return render(request, 'sing_in.html', )


class Search(ListView):

    def get_queryset(self):
        return Wick.objects.filter(title__icontains=self.request.GET.get("q"))

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["q"] = f'q={self.request.GET.get("q")}&'
        return context
