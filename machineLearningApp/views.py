import contextlib
from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CreateUserForm
import joblib
from django.contrib.auth import authenticate, login,logout
from machineLearningApp.models import *


# faka page
def index(request):

    return render(request,'machineLearningApp/index.html')


def home(request):
    if request.method == "POST":
        context = {}
        

        radius_mean = float(request.POST.get('radius_mean'))
        texture_mean = float(request.POST.get('texture_mean'))
        perimeter_mean = float(request.POST.get('perimeter_mean'))
        area_mean = float(request.POST.get('area_mean'))
        smoothness_mean = float(request.POST.get('smoothness_mean'))
        compactness_mean = float(request.POST.get('compactness_mean'))

        concavity_mean = float(request.POST.get('concavity_mean'))
        concave_points_mean = float(request.POST.get('concave_points_mean'))
        symmetry_mean = float(request.POST.get('symmetry_mean'))
        radius_se = float(request.POST.get('radius_se'))
        perimeter_se = float(request.POST.get('perimeter_se'))

        area_se = float(request.POST.get('area_se'))
        concave_points_se = float(request.POST.get('concave_points_se'))
        radius_worst = float(request.POST.get('radius_worst'))
        texture_worst = float(request.POST.get('texture_worst'))
        perimeter_worst = float(request.POST.get('perimeter_worst'))
        area_worst = float(request.POST.get('area_worst'))

        smoothness_worst = float(request.POST.get('smoothness_worst'))
        compactness_worst = float(request.POST.get('compactness_worst'))
        concavity_worst = float(request.POST.get('concavity_worst'))
        concave_points_worst = float(request.POST.get('concave_points_worst'))
        symmetry_worst = float(request.POST.get('symmetry_worst'))
        
        model = joblib.load('cancer.joblib')
        pipeline = joblib.load('pipeline')  
        prep_data = pipeline.transform([[radius_mean,texture_mean,perimeter_mean,area_mean,smoothness_mean,compactness_mean,concavity_mean,concave_points_mean,symmetry_mean,radius_se,perimeter_se,area_se,concave_points_se,radius_worst,texture_worst,perimeter_worst,area_worst,smoothness_worst,compactness_worst,concavity_worst,concave_points_worst,symmetry_worst]])
        result = model.predict(prep_data)[0]

        if result == 1:
            messages.info(request,"You have high chance of having a breast cancer!Please consult a doctor immediately")
      
        elif result == 0:
            messages.info(request,"It seems like you are safe! Keep it up")

       
        dataset = Dataset(patient=request.user,
        radius_mean = radius_mean,
        texture_mean = texture_mean ,
        perimeter_mean = perimeter_mean,
        area_mean =  area_mean,
        smoothness_mean=smoothness_mean ,
        compactness_mean = compactness_mean,

        concavity_mean =concavity_mean,
        concave_points_mean =  concave_points_mean,
        symmetry_mean =  symmetry_mean,
        radius_se = radius_se,
        perimeter_se =  perimeter_se,

        area_se =  area_se,
        concave_points_se = concave_points_se,
        radius_worst = radius_worst,
        texture_worst =  texture_worst ,
        perimeter_worst =  perimeter_worst,
        area_worst = area_worst,

        smoothness_worst = smoothness_worst,
        compactness_worst = compactness_worst,
        concavity_worst = concavity_worst,
        concave_points_worst = concave_points_worst,
        symmetry_worst = symmetry_worst ,
        result = result
        )

        dataset.save()
        print("saved")
        
        suggestion = "radius mean 11 to 17,perimeter mean 67 to 115,area mean 303 to 1005,concave_points_mean 0.01 to 0.07,radius worst 12 to 20,perimeter worst 74 to 140,area worst 311 to 1449,concave points worst 0.05 to 0.17"

        context = {
            "result" : result,
            "suggestion" : suggestion
        }
        

        return render(request,'machineLearningApp/home.html',context)

    return render(request,'machineLearningApp/home.html', )


def signInPage(request):
    
    if request.method == "POST":
        
            username = request.POST.get('username')
            password = request.POST.get('password')

            user =  authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request,user)
                messages.success(request,"Login Successful")
                return redirect('home')
            else:
                messages.info(request,"username or password is incorrect")
   

    return render(request,'machineLearningApp/signIn.html')



def signUpPage(request):
    form =  CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            
    context = {'form' : form }
    return render(request,'machineLearningApp/signup.html',context)



def historyPage(request):
    records = Dataset.objects.filter(patient = request.user)
    context = { "records" : records }

    return render(request,'machineLearningApp/history.html',context)

def logOutPage(request):
    
    logout(request)
    return redirect('signInPage')

def contact(request):

    return render(request,'machineLearningApp/contact.html')