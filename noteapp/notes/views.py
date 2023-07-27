from django.utils import timezone
from django.shortcuts import render, redirect
from .models import Note
from .forms import NoteForm


# Create your views here.


def index(request, note_id=None):
    if request.method == "POST":
        form = NoteForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.time_of_posting = timezone.now()
            note.save()
            form = NoteForm()
    else:
        form = NoteForm()

    all_notes = Note.objects.all()
    context = {"form": form, "note_list": all_notes}
    return render(request, "index.html", context)


def delete(request, note_id):
    obj = Note.objects.get(id=note_id)
    obj.delete()
    return redirect("/")
