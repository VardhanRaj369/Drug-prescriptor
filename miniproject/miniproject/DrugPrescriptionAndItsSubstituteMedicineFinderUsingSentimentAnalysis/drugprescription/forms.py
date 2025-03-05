from django.forms import Form, CharField, FileField


class UserForm(Form):
    name = CharField(max_length=500)
    username = CharField(max_length=500)
    password = CharField(max_length=500)
    email = CharField(max_length=500)
    mobile = CharField(max_length=500)
    address = CharField(max_length=500)
    role = CharField(max_length=500)


class LoginForm(Form):
    username = CharField(max_length=100)
    password = CharField(max_length=100)
    type = CharField(max_length=100)