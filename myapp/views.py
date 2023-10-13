from django.shortcuts import render, redirect
from .models import student
from django.contrib import messages
from django.db.models import Q
import json

def index(request):

    
    students = student.objects.all()
    query = ""

    
    if request.method == "POST":
        if "add" in request.POST:
            name = request.POST.get("name")
            dob = request.POST.get("dob")
            email = request.POST.get("email")
            Age = request.POST.get("Age")
            gender = request.POST.get("gender")
            country = request.POST.get("country")
            state = request.POST.get("state")
            city = request.POST.get("city")
            pincode = request.POST.get("pincode")
            qualification = request.POST.get("qualification")
            student.objects.create(Fullname = name, DOB = dob, Email = email, Age = Age,
                                   Gender = gender, Country = country, State = state, City = city, 
                                   Pincode = pincode, Qualification = qualification)
            messages.success(request, "New Student Added Successfull")
            return redirect('index')
        
        
        elif "update" in request.POST:
            id = request.POST.get("id")
            name = request.POST.get("name")
            dob = request.POST.get("dob")
            email = request.POST.get("email")
            Age = request.POST.get("Age")
            gender = request.POST.get("gender")
            country = request.POST.get("country")
            state = request.POST.get("state")
            city = request.POST.get("city")
            pincode = request.POST.get("pincode")
            qualification = request.POST.get("qualification")

            Update_student = student.objects.get(id=id)
            Update_student.Fullname = name
            Update_student.DOB = dob
            Update_student.Email = email
            Update_student.Age = Age
            Update_student.Gender = gender
            Update_student.Country = country
            Update_student.State = state
            Update_student.City = city
            Update_student.Pincode = pincode
            Update_student.Qualification = qualification
            Update_student.save()

            messages.success(request, "Student Data Updated Successfull")
            return redirect('index')
    


        elif "delete" in request.POST:
            id = request.POST.get("id")
            student.objects.get(id=id).delete()  
            messages.success(request, "Student Deleted Successfully")
            return redirect('index')
        
        elif "namesearch" in request.POST:
            namequery = request.POST.get("namesearchquery")
            students = student.objects.filter(Fullname = namequery)
            context = {"students" : students, "namequery" : namequery}

        elif "dobsearch" in request.POST:
            dobquery = request.POST.get("dobsearchquery")
            students = student.objects.filter(DOB__contains = dobquery)
            context = {"students" : students, "dobquery" : dobquery}

        elif "emailsearch" in request.POST:
            emailquery = request.POST.get("emailsearchquery")
            students = student.objects.filter(Email = emailquery)
            context = {"students" : students, "emailquery" : emailquery}


        elif "search" in request.POST:
            query = request.POST.get("searchquery")
            students = student.objects.filter(Q(Fullname__icontains=query) | Q(DOB__icontains=query) | Q(Email__icontains=query) |
                                              Q(Age__icontains=query) | Q(Gender__icontains=query) | Q(City__icontains=query) | 
                                              Q(Qualification__icontains=query))

    context = {"students" : students, "query" : query}
    return render(request,'index.html', context = context)



def pie_chart(request):
    # Query the database to get the data you need
    students = student.objects.all()

    # Extract age data and labels for the chart
    age_data = [student.Age for student in students]
    labels = [student.Fullname for student in students]

    # Create a dictionary containing the chart data
    chart_data = {
        'data': age_data,
        'labels': labels,      
    }

    return render(request, 'chart.html', {'chart_data': json.dumps(chart_data)})





