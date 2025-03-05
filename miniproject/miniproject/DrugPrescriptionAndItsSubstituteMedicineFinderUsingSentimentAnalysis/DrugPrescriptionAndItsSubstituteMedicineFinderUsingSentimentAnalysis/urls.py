from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

from drugprescription.views import login, userregistration, activateAccount, logout, getusers, addReview, getReviews, \
    deleteReview, addMedicineAction, addReviewAction, searchMedicines

from drugprescription.views import addMedicine, getMedicines, deleteMedicine, updateMedicine, updateMedicineAction,findMedicines

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='login'),
    path('index/', TemplateView.as_view(template_name='index.html'), name='login'),
    path('loginaction/', login, name='loginaction'),
    path('userregistration/', TemplateView.as_view(template_name='userregistration.html'), name='registration'),
    path('storeregistration/', TemplateView.as_view(template_name='storeregistration.html'), name='registration'),
    path('userregaction/', userregistration, name='regaction'),
    path('logout/', logout, name='logout'),
    path('getusers/', getusers, name='getusers'),
    path('activateAccount/', activateAccount, name='activateAccount'),

    path('addmedicine/', addMedicine, name='addmedicine'),
    path('addmedicineaction/', addMedicineAction, name='addmedicine'),
    path('viewmedicines/', getMedicines, name='view medicines'),
    path('updatemedicine/', updateMedicine, name='update medicines'),
    path('updatemedicineaction/', updateMedicineAction, name='update medicines'),
    path('deletemedicine/', deleteMedicine, name='delete medicine'),

    path('findmedicine/', TemplateView.as_view(template_name='findmedicine.html'), name='addmedicine'),
    path('findmedicineaction/',findMedicines, name='addmedicine'),

    path('searchmedicine/', TemplateView.as_view(template_name='searchmedicine.html'), name='addmedicine'),
    path('searchmedicineaction/',searchMedicines, name='addmedicine'),

    path('addreview/',addReview, name='addreview'),
    path('addreviewaction/',addReviewAction, name='addreview'),
    path('viewreviews/',getReviews, name='view reviews'),
    path('deletereview/',deleteReview, name='delete review'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)