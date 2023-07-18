from django.shortcuts import render,redirect
from .models import Student
from django.contrib import messages
import os
# Create your views here.


def index(request):
    data = Student.objects.order_by('id')
    data_with_ids = [(index + 1, student) for index, student in enumerate(data)]
    context = {"data": data_with_ids}
    return render(request, "index.html", context)


from django.conf import settings
import os

def insertData(request):
    if request.method == "POST":
        name = request.POST.get('name')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        age = request.POST.get('age')
        publisher = request.POST.get('publisher')
        
        # Save the data to the database
        query = Student(name=name, author=author, genre=genre, age=age, publisher=publisher)
        query.save()
        
        # Save the data to the file
        file_path = os.path.join(settings.BASE_DIR, 'Use books_list.txt')
        with open(file_path, 'a') as file:
            file.write(f"Name: {name}\nAuthor: {author}\nGenre: {genre}\nAge: {age}\nPublisher: {publisher}\n\n")
        
        messages.info(request, "Data Inserted Successfully")
        return redirect("/")
    
    return render(request, "index.html")


def updateData(request,id):
    if request.method=="POST":
        name=request.POST['name']
        author=request.POST['author']
        genre=request.POST['genre']
        age=request.POST['age']
        publisher = request.POST['publisher']

       

        edit=Student.objects.get(id=id)
        edit.name=name
        edit.author=author
        edit.genre=genre
        edit.age=age
        edit.publisher=publisher
        edit.save()
        messages.warning(request,"Data Updated Successfully")
        return redirect("/")

    d=Student.objects.get(id=id) 
    context={"d":d}
    return render(request,"edit.html",context)

def deleteData(request,id):
    d=Student.objects.get(id=id) 
    d.delete()
    messages.error(request,"Data deleted Successfully")
    return redirect("/")
    
def about(request):
    return render(request,"about.html")