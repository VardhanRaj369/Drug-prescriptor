from drugprescription.forms import UserForm, LoginForm
from drugprescription.models import UserModel, LoginModel, MedicineModel, ReviewModel

from datetime import datetime
from django.shortcuts import render

from drugprescription.service import getMedicinesByStore, getReviewsByMedicine, findMedicineByName, \
    searchMedicineBySymptoms

def userregistration(request):
    status = False

    if request.method == "POST":
        # Get the posted form
        registrationForm = UserForm(request.POST)

        if registrationForm.is_valid():

            regModel = UserModel()

            regModel.username = registrationForm.cleaned_data["username"]
            regModel.password = registrationForm.cleaned_data["password"]
            regModel.email = registrationForm.cleaned_data["email"]
            regModel.mobile = registrationForm.cleaned_data["mobile"]
            regModel.address = registrationForm.cleaned_data["address"]
            regModel.name = registrationForm.cleaned_data["name"]

            loginModel=LoginModel()
            loginModel.username=registrationForm.cleaned_data["username"]
            loginModel.password=registrationForm.cleaned_data["password"]
            loginModel.role= registrationForm.cleaned_data["role"]
            loginModel.status="no"

            if loginModel.role=="user":
                loginModel.status="yes"

            user = UserModel.objects.filter(username=regModel.username).first()

            if user is not None:
                status = False
            else:
                try:
                    regModel.save()
                    loginModel.save()
                    status = True
                except:
                    status = False
    if status:
        return render(request, 'index.html', locals())
    else:
        response = render(request, 'userregistration.html', {"message": "User All Ready Exist"})

    return response

def login(request):

    if request.method == "GET":
        # Get the posted form
        loginForm = LoginForm(request.GET)

        if loginForm.is_valid():

            uname = loginForm.cleaned_data["username"]
            upass = loginForm.cleaned_data["password"]
            type = loginForm.cleaned_data["type"]

            if type in "admin":

                if uname == "admin" and upass == "admin":

                    request.session['username'] = "admin"
                    request.session['role'] = "admin"

                    users = []
                    for user in UserModel.objects.all():
                        login = LoginModel.objects.get(username=user.username)
                        if login.role=="store":
                            user.status = login.status
                            users.append(user)

                    return render(request, "stores.html", {"stores": users})

                else:
                    response = render(request, 'index.html', {"message": "Invalid Credentials"})
            else:

                login = LoginModel.objects.filter(username=uname, password=upass,status="yes").first()

                if login is not None:

                    request.session['username'] = uname
                    request.session['role'] = login.role

                    if login.role=="user":
                        return render(request, "searchmedicine.html")
                    elif login.role=="store":
                        return render(request, "viewmedicine.html", {"medicines":getMedicinesByStore(uname)})

                else:
                    response = render(request, 'index.html', {"message": "Invalid Credentials"})

    return response

def logout(request):
    try:
        del request.session['username']
        del request.session['role']
    except:
        pass
    return render(request, 'index.html', {})

def getusers(request):

    users = []
    for user in UserModel.objects.all():
        login = LoginModel.objects.get(username=user.username)
        if login.role == "store":
            user.status = login.status
            users.append(user)

    return render(request, "stores.html", {"stores": users})

def activateAccount(request):

    username = request.GET['username']
    status=request.GET['status']

    LoginModel.objects.filter(username=username).update(status=status)

    users = []
    for user in UserModel.objects.all():
        login = LoginModel.objects.get(username=user.username)
        if login.role == "store":
            user.status=login.status
            users.append(user)

    return render(request, "stores.html", {"stores": users})

#============================================================================================================================
def addMedicine(request):
    return render(request, 'addmedicine.html', {"medicines":MedicineModel.objects.all()})

def addMedicineAction(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        symptoms = request.POST.get('symptoms')
        disease = request.POST.get('disease')
        count = request.POST.get('count')
        price = request.POST.get('price')
        alternates = request.POST.getlist('alternates[]')

        MedicineModel(name=name,symptoms=symptoms,disease=disease,count=count,price=price,
                      alternates=alternates,username=request.session['username']).save()

        return render(request, "viewmedicine.html", {"medicines": getMedicinesByStore(request.session['username'])})

    # If the form is not valid, return to the form with an error message
    return render(request, 'addmedicine.html', {"message": "Medicine Adding Failed"})


def getMedicines(request):
    return render(request, "viewmedicine.html", {"medicines":getMedicinesByStore(request.session['username'])})

def deleteMedicine(request):
    MedicineModel.objects.filter(id=request.GET['id']).delete()
    return render(request, "viewmedicine.html", {"medicines":getMedicinesByStore(request.session['username'])})

def updateMedicine(request):
    return render(request, 'updatemedicine.html', {"medicine":MedicineModel.objects.get(id=request.GET['id'])})

def updateMedicineAction(request):
    MedicineModel.objects.filter(id=request.GET['id']).update(count=request.GET['count'])
    return render(request, "viewmedicine.html", {"medicines":getMedicinesByStore(request.session['username'])})

def searchMedicines(request):
    return render(request, "searchmedicine.html", {"medicines":searchMedicineBySymptoms(request.GET['location'],request.GET['symptoms'])})

def findMedicines(request):
    return render(request, "findmedicine.html", {"medicines":findMedicineByName(request.GET['location'],request.GET['name'])})

def addReview(request):
    return render(request, "addreview.html",{"id":request.GET['id']})

def addReviewAction(request):

    ReviewModel(
        medicine=request.GET['id'],
        review =request.GET['review'],
        user = request.session['username'],
        date =datetime.now()
    ).save()

    return render(request, "searchmedicine.html")

def getReviews(request):
    return render(request, "viewreviews.html", {"reviews":getReviewsByMedicine(request.GET['id'])})

def deleteReview(request):
    ReviewModel.objects.filter(id=request.GET['id']).delete()
    return render(request, "viewreviews.html", {"reviews":getReviewsByMedicine(request.GET['id'])})