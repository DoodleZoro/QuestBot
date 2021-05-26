from django.shortcuts import render
import wolframalpha
import wikipedia
import webbrowser

def index(request):
    return render(request, 'questbot/index.htm')


def bot_search(request):
    query = request.GET.get('query')

    try:
        client = wolframalpha.Client("UW4YWT-7QPYW2G5JA")
        re = client.query(query)
        an = next(re.results).text
        return render(request, 'questbot/index.htm', {'an': an, 'query': query})

            
    except Exception:
        try:
            an = wikipedia.summary(query, sentences=10)
            return render(request, 'questbot/index.htm', {'an': an, 'query': query})


        except Exception:
            an = "Sorry, Nothing found"
            return render(request, 'questbot/index.htm', {'an': an, 'query': query})