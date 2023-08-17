from django.shortcuts import render, HttpResponse

author = {'Имя' : 'Иван',
          'Фамилия':'Иванов'

 }



# Create your views here.
def home(request):
    text = """<h1>"Изучаем django"</h1>
              <strong>Автор</strong>: <i>Усачева Л.В.  + Катя Галкина</i>
           """
    return HttpResponse(text)

def about(request):
    result = f"""
            <b>Имя:</b> <b>{author['Имя']}<b><br>
            <strong>Фамилия:</strong> <b>{author['Фамилия']}<b><br>
    """
    return HttpResponse(result)
