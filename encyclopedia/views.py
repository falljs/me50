from django.shortcuts import render, redirect
from django.contrib import messages
from .util import save_entry, list_entries, get_entry
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    content = util.get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {
            "message": "The requested page was not found."
        })
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": content
    })

def search(request):
    query = request.GET.get("q", "")
    entries = util.list_entries()

    # Vérifier si la requête correspond exactement à une entrée existante
    if query.lower() in [entry.lower() for entry in entries]:
        return redirect("entry", title=query)

    # Filtrer les entrées qui contiennent la requête comme sous-chaîne
    matching_entries = [entry for entry in entries if query.lower() in entry.lower()]

    return render(request, "encyclopedia/search.html", {
        "query": query,
        "matching_entries": matching_entries
    })

def create_entry(request):
    if request.method == "POST":
        title = request.POST.get("title")
        content = request.POST.get("content")
        entries = list_entries()

        if title in entries:
            messages.error(request, "Une entrée avec ce titre existe déjà.")
        else:
            save_entry(title, content)
            return redirect("entry", title=title)

    return render(request, "encyclopedia/create_entry.html")

def edit_entry(request, title):
    content = get_entry(title)
    if content is None:
        return render(request, "encyclopedia/error.html", {"message": "Page not found"})
    
    if request.method == "POST":
        new_content = request.POST["content"]
        if new_content:
            save_entry(title, new_content)
            return redirect("entry", title=title)
        else:
            messages.error(request, "Content cannot be empty.")
    
    return render(request, "encyclopedia/edit_entry.html", {"title": title, "content": content})


def random_entry(request):
    entries = list_entries()
    if entries:
        random_entry = random.choice(entries)
        return redirect('entry', title=random_entry)
    else:
        # Gérer le cas où il n'y a pas d'entrées disponibles
        return redirect('index')
