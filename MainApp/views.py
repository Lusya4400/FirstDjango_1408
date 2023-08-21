from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render 
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist



# items = [
#    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
#    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
#    {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
#    {"id": 7, "name": "Картофель фри" ,"quantity":0},
#    {"id": 8, "name": "Кепка" ,"quantity":124},
# ]


# Create your views here.
def home(request):
#    text = """<h1>"Изучаем django"</h1>
#              <strong>Автор</strong>: <i>Усачева Л.В.  + Катя Галкина</i>
#           """
#    return HttpResponse(text)
    context = {
         "name" : "Петров Петр Петрович",
         "email" : "my_mail@mail.ru"
    }
    return render(request, "index.html", context)

def about(request):
    author = {'Имя' : 'Иван',
          'Отчество' : 'Петрович',
          'Фамилия':'Иванов',
          'телефон': '8-923-600-01-02',
          'email' : 'vasya@mail.ru'
        }
    result = f"""
            <header>
            <a href ='/'> Home </a> / <a href ='/items'> Items </a> / <a href ='/about'> About </a><br><br>
            </header>
            Имя: <b>{author['Имя']}</b><br>
            Отчество: <b>{author['Отчество']}</b><br>
            Фамилия: <b>{author['Фамилия']}</b><br>
            Телефон: <b>{author['телефон']}</b><br>
            email: <b>{author['email']}</b><br><br>
    """
    return HttpResponse(result)

def get_item(request, item_id):
    try:
        item = Item.objects.get(pk = item_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Товар с id {item_id} не найден!")        
    # for item in items:
    #     if item['id'] == item_id:
    #         context = {
    #         "item" : item
    #         }
    #         result = f"""
    #         Название товара: <b>{item['name']}</b><br>
    #         Количество: <b>{item['quantity']}</b><br>
    #         <p><a href="/item"</a> Назад, к списку товаров </p>
    #         """
    #         return HttpResponse(result)
    #        return render(request, 'item_page.html', context)
    #return HttpResponseNotFound(f"Товар с id {id} не найден!")
    else:
        context = {
                "item" : item
                }
        return render(request, 'item_page.html', context)

def get_items(request):
#    result = "<h2>Список товаров</h2><ol>"
#    for item in items:
#            result += f"""
#            <li><a href="/item/{item['id']}">{item['name']}</a></li>
#            """
#    result += '</ol>'
#    return HttpResponse(result)
    # context = {
    #     "items" : items
    # }
    context = {
        "items" : Item.objects.all()
    }
    return render(request, "items_list.html", context)