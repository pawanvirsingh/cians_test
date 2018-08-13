from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from users.models import JobFinder,ThortalDownload
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('job')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

class JobFinderSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobFinder  
        fields = '__all__'

@csrf_exempt
@login_required
@api_view(['GET', 'POST'])
def show_data(request):
    if request._request.method=="POST":
        search_str = request.data["skills"]
        if search_str:
            job_user_data = JobFinder.objects.filter(Q(skills__icontains=search_str)
            | Q(resume__icontains = search_str)
            | Q(name__icontains = search_str)
            | Q(email__icontains = search_str)
            | Q(mobile__icontains = search_str)
            | Q(current_address__icontains = search_str)
            | Q(corrected_address__icontains = search_str)
            | Q(nearest_city__icontains = search_str)
            | Q(prefered_location__icontains = search_str)
            | Q(company_current__icontains = search_str)
            | Q(designation__icontains = search_str)
            | Q(skills__icontains = search_str)
            | Q(experience__icontains = search_str)).all()
            job_data_seri = JobFinderSerializer(job_user_data, many=True)
            return Response({"data":job_data_seri.data, "success": True})
        else:
            job_user_data = JobFinder.objects.all()
            job_data_seri = JobFinderSerializer(job_user_data, many=True)
            return Response({"data":job_data_seri.data, "success": True})

    else:
        download_limiter = ThortalDownload.objects.filter(user = request.user).first()
        if download_limiter:
            count = download_limiter.download_count
            if count < download_limiter.download_allowd:
                download_limiter.download_count= count+1
                download_limiter.save()
                job_user_data = JobFinder.objects.all()
                job_data_seri = JobFinderSerializer(job_user_data, many=True)
                return Response({"data":job_data_seri.data, "success": True})
            else:
                return Response({"data":[], "success": False,"message":"you reached maximum downlaod"})
        else:
            obj_throtal = ThortalDownload(user=request.user,download_count=1)
            obj_throtal.save()
            job_user_data = JobFinder.objects.all()
            job_data_seri = JobFinderSerializer(job_user_data, many=True)
            return Response({"data":job_data_seri.data, "success": True})






