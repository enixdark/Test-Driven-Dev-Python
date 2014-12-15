from django.shortcuts import render,render_to_response,HttpResponse
from django.db import transaction
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import TemplateView,DetailView,CreateView,UpdateView
from django.contrib import messages
# Create your views here.
from django.utils.functional import cached_property
# from .models import Flavor,FlavorReview
def index_page(request):
    if request.method == "POST":
        return render_to_response('lists/index.html',{'new_item_text':request.POST['item_text']})
    return render(request,'lists/index.html',{'new_item_text':'A new list item'})


def home_page(request,next=''):
    return render(request,'lists/home.html')

# @transaction.non_atomic_requests
# def example_non_atomic(request,pk,status):
#     # try:
#     obj = get_object_or_404(Flavor,pk=pk)
#     obj.lastest_status_change_attempt = timezone.now()
#     obj.save()
#
#     #     with transaction.atomic():
#     #         obj.status = status
#     #         obj.lastest_status_change_attempt = timezone.now()
#     #         obj.save()
#     #         return HttpResponse("CQSHINN")
#     # except:
#     #     return HttpResponse('ERROR')
#     return HttpResponse("ENIXDARK",status_code=400)
#
# class LoginRequireMixin(object):
#     def get_login(self,**kwargs):
#         return super(LoginRequireMixin,self,**kwargs).get_login()
#
# class FreshFruitMixin(object):
#
#     def get_content_date(self,**kwargs):
#         content = super(FreshFruitMixin,self,**kwargs).get_content_data()
#         content['has_fresh_fruit'] = True
#         return content
#
# class FlavorActionMixin(object):
#     fields = ('title','created','modifed')
#
#     @property
#     def success_msg(self):
#         return NotImplemented
#
#     def form_valid(self,form):
#         messages.info(self.request,self.success_msg)
#         return super(FlavorActionMixin,self).form_valid(form)
#
# class FruitFlavorView(FreshFruitMixin,TemplateView):
#
#     template_name = "fruit_flavor.html"
#
# class FlavorUpdateView(LoginRequireMixin,FlavorActionMixin,UpdateView):
#     model = Flavor
#     success_msg = "Flavor Updated"


# class FlavorDetailView(LoginRequireMixin,FlavorActionMixin,DetailView):
#     model = Flavor
#     fields = ('title','created','modifed')
#     success_msg = "Flavor Detail"
#
#
#
# class FlavorCreateView(LoginRequireMixin,FlavorActionMixin,CreateView):
#     model = Flavor
#     fields = ('title','created','modifed')
#     success_msg = "Flavor Created"

    # def form_valid(self, form):
    #     return super(FlavorCreateView,self).form_valid(form)