from django.db.models import Sum
from django.shortcuts import render, redirect

from exam.web.forms import ProfileCreateForm, CarCreateForm, CarEditForm, CarDeleteForm, ProfileEditForm, \
    ProfileDeleteForm, ProfileBaseForm
from exam.web.models import Profile, Car


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist as ex:
        return None


def index(request):
    profile = Profile.objects.all().first()

    if profile:
        car = Car.objects.all()
        context = {"car": car, "profile": profile}
        return render(request, 'core/home-with-profile.html', context)

    if request.method == "POST":
        form = ProfileBaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home page')

    form = ProfileBaseForm()
    context = {"form": form}
    return render(request, 'core/home-with-no-profile.html', context)


def catalogue(request):
    car_count = Car.objects.count()

    context = {
        'cars': Car.objects.all(),
        'car_count': car_count,
    }
    return render(request, 'core/catalogue.html', context)


def create_car(request):
    if request.method == 'GET':
        form = CarCreateForm()
    else:
        form = CarCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'form': form,
    }

    return render(request, 'cars/car-create.html', context)


def details_car(request, pk):
    car = Car.objects.filter(pk=pk).get()

    context = {
        'car': car,
    }

    return render(request, 'cars/car-details.html', context)


def edit_car(request, pk):
    car = Car.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = CarEditForm(instance=car)
    else:
        form = CarEditForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'car': car,
        'form': form,
    }

    return render(request, 'cars/car-edit.html', context)


def delete_car(request, pk):
    car = Car.objects.filter(pk=pk).get()

    if request.method == 'GET':
        form = CarDeleteForm(instance=car)
    else:
        form = CarDeleteForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')

    context = {
        'car': car,
        'form': form,
    }

    return render(request, 'cars/car-delete.html', context)


def create_profile(request):
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {
        'form':form,
    }

    return render(request, 'profiles/profile-create.html', context )


def details_profile(request):
    profile = Profile.objects.all().get()
    car_total_price = Car.objects.aggregate(Sum('price'))

    context = {
        'profile': profile,
        'car_total_price': car_total_price,
    }

    return render(request, 'profiles/profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.all().get()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('details profile')

    context = {
        'form': form,
        'profile': profile,
    }

    return render(request, 'profiles/profile-edit.html', context)


def delete_profile(request):
        profile = Profile.objects.all().first()
        if request.method == "POST":
            form = ProfileDeleteForm(request.POST, instance=profile)
            if form.is_valid():
                form.save()
            return redirect('index')
        else:
            form = ProfileDeleteForm(instance=profile)

        context = {
            "form": form,
        }
        return render(request, 'profiles/profile-delete.html', context)