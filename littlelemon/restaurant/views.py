from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import BookingForm
from .models import Menu

# Create your views here.
def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            # Optional: Add a success message or redirect after saving
            return HttpResponse("Booking successful!")
    context = {'form': form}
    return render(request, 'book.html', context)

def menu(request):
    menu_data = Menu.objects.all()
    if not menu_data:
        return HttpResponse("No menu items available.")
    main_data = {"menu": menu_data}
    return render(request, 'menu.html', main_data)

# Add the display_menu_items view here
def display_menu_items(request, pk=None):
    if pk:
        # Retrieve the specific menu item by primary key (pk)
        menu_item = get_object_or_404(Menu, pk=pk)
    else:
        # If no pk is provided, set menu_item to an empty string
        menu_item = ""
    
    # Render the template with menu_item context
    return render(request, 'menu_item.html', {"menu_item": menu_item})
