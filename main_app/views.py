from django.shortcuts import render

finches = [
{'name': 'Peep', 'breed': 'Zebra Finch', 'description': 'Tiny and energetic, with distinctive black and white stripes', 'age': .4},
{'name': 'Wings', 'breed': 'Bengalese Finch', 'description': 'Quiet and calm, with a striking chestnut plumage', 'age': 3},
{'name': 'Chirpy', 'breed': 'Gouldian Finch', 'description': 'Colorful and vibrant, with a striking mix of green, yellow, and red feathers', 'age': 2},
{'name': 'Song', 'breed': 'European Goldfinch', 'description': 'Distinguished by the red face and a melodious song', 'age': 5},
{'name': 'Feather', 'breed': 'Star Finch', 'description': 'Small and adorable, known for their red face and green body', 'age': 4},
]


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def finches_index(request):
    return render(request, 'finches/index.html', {
        'finches': finches,
    })
