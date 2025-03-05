from django.contrib import admin

# Register your models here.
from.models import *

admin.site.register(UserModel)
admin.site.register(MedicineModel)
admin.site.register(LoginModel)
admin.site.register(ReviewModel)
