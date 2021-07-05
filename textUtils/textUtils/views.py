# I created this file  - Ashok

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # params ={'name':'harry' , 'place':'USA'}
    return render(request, 'index.html')
    # return HttpResponse("Home")


def analyse(request):
    # get the text
    djText = (request.POST.get('text', 'default'))
    # check checkboxes value
    removePunc = (request.POST.get('removePunc', 'off'))
    fullCaps = (request.POST.get('fullCaps', 'off'))
    newLineRemover = (request.POST.get('newLineRemover', 'off'))
    extraSpaceRemover = (request.POST.get('extraSpaceRemover', 'off'))
    charCount = (request.POST.get('charCount', 'off'))

    # check what condition
    if removePunc == 'on':
        analysed = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djText:
            if char not in punctuations:
                analysed += char
        params = {'purpose': 'Remove Punctuations', 'analysed_text': analysed}
        djText = analysed
        # return render(request, 'analyse.html', params)
    if fullCaps == 'on':
        analysed = ""
        for char in djText:
            analysed += char.upper()
        params = {'purpose': 'Convert to UPPERCASE', 'analysed_text': analysed}
        djText = analysed
        # return render(request, 'analyse.html', params)
    if newLineRemover == 'on':
        analysed = ""
        for char in djText:
            if char != '\n' and char != '\r':
                analysed += char
        params = {'purpose': 'Remove New Line', 'analysed_text': analysed}
        djText = analysed
        # return render(request, 'analyse.html', params)
    if extraSpaceRemover == 'on':
        analysed = ""
        for index, char in enumerate(djText):
            if djText[index] == " " and djText[index + 1] == " ":
                pass
            else:
                analysed += char

        params = {'purpose': 'Extra Space remover', 'analysed_text': analysed}
        djText = analysed
        # return render(request, 'analyse.html', params)

    if charCount == 'on':
        cnt = 0
        for char in djText:
            cnt += 1

        params = {'purpose': 'Character Count', 'analysed_text': cnt}

    if removePunc == 'off' and newLineRemover == 'off' and extraSpaceRemover == 'off' and fullCaps == 'off' and charCount == 'off':
        return HttpResponse(djText)

    return render(request, 'analyse.html', params)


def ex1(request):
    return render(request, 'ex1.html')


def about(request):
    return render(request, 'about.html')

# def removePunc(request):
#     #get the text
#     djText = (request.GET.get('text','default'))
#     print(djText)
#     #Analyse the text
#     return HttpResponse('''<h1>Remove Punctuation</h1> <a href = '/'> Back </a> ''')
#
# def capFirst(request):
#     return HttpResponse('''<h1>Capitalise First</h1> <a href = '/'> Back </a> ''')
#
# def newLineRemove(request):
#     return HttpResponse('''<h1>New Line Remover</h1> <a href = '/'> Back </a> ''')
#
# def spaceRemove(request):
#     return HttpResponse('''<h1>Space Remover</h1> <a href = '/'> Back </a> ''')
#
# def charCount(request):
#     return HttpResponse('''<h1>Character Count</h1> <a href = '/'> Back </a> ''')
