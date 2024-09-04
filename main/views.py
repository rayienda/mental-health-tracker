from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2306172735',
        'name': 'Rayienda',
        'class': 'PBP KKI'
    }

    return render(request, "main.html", context)