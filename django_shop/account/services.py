from django.contrib.auth import login, authenticate


def auth_user(request, form):
    if form.is_valid():
        data = form.cleaned_data
        user = authenticate(username=data['email'], password=data['password'])
        if user is not None:
            login(request, user)
            return True
    return False
        

def signup_user(form):
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        return True
    return False
