from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipe_view(request, dish):
    recipe = DATA.get(dish)
    context = {
        'title': f'Рецепт для {dish}',
        'recipe': recipe,
    }

    params = request.GET
    servings = params.get('servings')
    if servings and servings.isdigit():
        context['recipe'] = {k: v * int(servings) for k, v in recipe.items()}

    return render(request, 'calculator/index.html', context)
