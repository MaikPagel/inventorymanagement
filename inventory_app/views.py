from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import ItemForm
from django.db import IntegrityError
from django.core.paginator import Paginator
from django.db.models import Q

@login_required
def my_inventory(request):
    # GET-Parameter
    search_query = request.GET.get('q', '')
    category_filter = request.GET.get('category', '')
    per_page = request.GET.get('per_page', 25)
    try:
        per_page = int(per_page)
    except ValueError:
        per_page = 25

    # Queryset filtern
    items_qs = Item.objects.filter(owner=request.user)
    if search_query:
        items_qs = items_qs.filter(
            Q(name__icontains=search_query) |
            Q(description__icontains=search_query)
        )
    if category_filter:
        items_qs = items_qs.filter(category=category_filter)

    # Paginator
    paginator = Paginator(items_qs, per_page)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Query-String ohne 'page' bauen (wird an Links gehängt)
    params = request.GET.copy()
    if 'page' in params:
        params.pop('page')
    query_params = params.urlencode()  # z.B. "q=apfel&per_page=25&category=Essen"

    # Kategorien für Dropdown
    categories = Item.objects.filter(owner=request.user).values_list('category', flat=True).distinct()

    return render(request, 'inventory_app/my_inventory.html', {
        'page_obj': page_obj,
        'search_query': search_query,
        'per_page': per_page,
        'categories': categories,
        'category_filter': category_filter,
        'query_params': query_params,
    })

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def edit_inventory(request):
    # Alle Items des aktuellen Users
    items = Item.objects.filter(owner=request.user)
    form = ItemForm()

    # Alle vorhandenen Kategorien des Users sammeln
    categories = Item.objects.filter(owner=request.user).values_list('category', flat=True).distinct()

    if request.method == 'POST':
        # Neues Item hinzufügen
        if 'add_item' in request.POST:
            form = ItemForm(request.POST)
            form.instance.owner = request.user
            if form.is_valid():
                # Prüfen, ob neue Kategorie angegeben wurde
                new_cat = form.cleaned_data.get('new_category')
                if new_cat:
                    form.instance.category = new_cat
                try:
                    form.save()
                    return redirect('edit_inventory')
                except IntegrityError:
                    form.add_error('name', 'Du hast bereits ein Item mit diesem Namen.')

        # Bestehendes Item bearbeiten
        elif 'edit_item' in request.POST:
            item_id = request.POST.get('item_id')
            item = get_object_or_404(Item, id=item_id, owner=request.user)
            form = ItemForm(request.POST, instance=item)
            form.instance.owner = request.user
            if form.is_valid():
                # Neue Kategorie beim Bearbeiten ebenfalls prüfen
                new_cat = form.cleaned_data.get('new_category')
                if new_cat:
                    form.instance.category = new_cat
                try:
                    form.save()
                    return redirect('edit_inventory')
                except IntegrityError:
                    form.add_error('name', 'Du hast bereits ein Item mit diesem Namen.')

        # Item löschen
        elif 'delete_item' in request.POST:
            item_id = request.POST.get('item_id')
            item = get_object_or_404(Item, id=item_id, owner=request.user)
            item.delete()
            return redirect('edit_inventory')

    return render(request, 'inventory_app/edit_inventory.html', {
        'items': items,
        'form': form,
        'categories': categories,  # Kategorien an Template übergeben
    })

