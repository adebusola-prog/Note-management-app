from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages 
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import UserProfileForm, NoteForm
from django.db.models import Q

def home(request):
   context={}
   return render(request, 'noteapp/home.html', context)

def registerPage(request):
   form =UserCreationForm

   if request.method=="POST":
      form=UserCreationForm(request.POST)
      if form.is_valid():
         user = form.save(commit=False) #it's like freezing, you want to be able to access the user
         user.username=user.username
         user.save()
         login(request, user)
         return redirect('home')
      else:
         messages.error(request,  "An error occured during registration")
   
   return render(request, 'noteapp/signup.html', {'form': form})


# Update profile (including uploading profile picture)
@login_required
def profile(request):
   user_profile=UserProfile.objects.filter(username=request.user.id)
   context={'user_profile': user_profile}
   return render(request, 'noteapp/profile.html', context)

@login_required
def notes(request):
   q= request.GET.get('q', '')
   notes=Note.objects.filter(is_delete=False).filter(user_profile__username=request.user.id).filter(
      Q(title__icontains=q)|Q(text__icontains=q)
      # |
      # Q(kategory__name__icontains=q)
      )
   context={'notes':notes, 'q': q}
   return render(request, 'noteapp/notes.html', context)


@login_required
def detail_notes(request, pk):
   detail_note=get_object_or_404(Note, id=pk)
   context={'detail_note': detail_note}
   return render(request, 'noteapp/detail_notes.html', context)


# @login_required()
# def userupdate(request):
#    user_profile=UserProfile.objects.get(username=request.user.id)
#    form = UserProfileForm(instance=user_profile)

#    if request.method == "POST":
#       form =  UserProfileForm(request.POST, instance=user_profile)
#       if form.is_valid():
#          form.save()
#          return redirect('my_profile')

#    context = {"form": form }
#    return render(request, "noteapp/user_update_form.html", context)

@login_required()
def userupdate(request):
   user_profile=UserProfile.objects.get(username=request.user.id)
   form = UserProfileForm(request.POST, request.FILES, instance=user_profile)

   if request.method == "POST":
      form =  UserProfileForm(request.POST, request.FILES, instance=user_profile)
      if form.is_valid():
         updated_user= form.save(commit=False)
         updated_user.profile_pics = form.cleaned_data["profile_pics"]
         updated_user.save()
         return redirect('my_profile')
   
   elif request.method == "GET": 
      form = UserProfileForm(instance=user_profile)
      context = {"form": form }
      return render(request, "noteapp/user_update_form.html", context)


@login_required
def note_create(request):
   user_profile=UserProfile.objects.get(username=request.user.id)
   form=NoteForm()

   if request.method== "POST":
      form= NoteForm(request.POST, request.FILES)
      if form.is_valid():
         create_form= form.save(commit=False)
         create_form.user_profile= user_profile
         create_form.save()
         return redirect('notes')

   else:
      form=NoteForm()
   context={'form': form, 'user_profile':user_profile} 
   return render(request, 'noteapp/note_create.html', context)

@login_required()
def note_update(request, pk):
   
   note= Note.objects.get(id=pk)
   form = NoteForm(instance=note)
   
   if request.method == "POST":
      form=NoteForm(request.POST, instance=note)
      if form.is_valid():
         form.save()
         return redirect('notes')

   context={'note':note, 'form':form}
   return render(request, 'noteapp/user_update_form.html', context)


@login_required()
def note_delete(request, pk):
   note= get_object_or_404(Note, id=pk)

   if request.method == "POST":
      note.is_delete=True
      note.save()

      return redirect('notes')

   context= {'note': note}
   return render(request, 'noteapp/note_delete.html', context)


@login_required
def trash_notes(request):
   trash_note=Note.objects.filter(is_delete=True).filter(user_profile__username=request.user.id)
   context={'trash_note': trash_note}
   
   return render(request, 'noteapp/trash_note.html', context)


@login_required
def restore_note(request, pk):
   restore_note=get_object_or_404(Note, id=pk)

   if request.method =="POST":
      restore_note.is_delete=False
      restore_note.save()

      return redirect('notes')

   context={'restore_note': restore_note}
   return render(request, 'noteapp/restore.html', context)

@login_required
def delete_note(request, pk):
   delete_note_perm=get_object_or_404(Note, id=pk)

   if request.method =="POST":
      delete_note_perm.delete()
      return redirect('notes')

   context={'delete_note_perm': delete_note_perm}
   return render(request, 'noteapp/permanent_delete.html', context)


@login_required
def pinned_note(request):
   pinned_note=Note.objects.filter(user_profile__username=request.user.id).filter(is_pin=True)
   context={'pinned_note': pinned_note}
   return render(request, 'noteapp/pinned_note.html', context)

@login_required
def category_note(request, pk):
   category= Category.objects.filter(id=pk).first()

   return render(request, 'noteapp/category_note.html', {'category': category})

@login_required
def category_list(request):
   categories= Category.objects.all()

   return render(request, 'noteapp/category.html', {'categories': categories})

@login_required
def share_note(request):
   context={'share_note': 'You can share your note to family and friends here'}

   return render(request, 'noteapp/share_note.html', context)