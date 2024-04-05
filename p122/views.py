from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


   #return HttpResponse('''<h1>login page1</h1>
   # <a href="https://www.facebook.com/">facebook login</a>,<h1>login page2</h1>
    #<a href="https://www.instagram.com/">instagram login</a>,<h1>login page3</h1>
    #<a href="https://www.whatsapp.com/">whatsapp login</a>,<h1>login page4</h1>
   # <a href="https://www.snapchat.com/">snapchat login</a>''')

def analyze(request):
    djtext = (request.POST.get('text','default'))
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
   # charactercount = request.POST.get('charactercount','off')
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed =""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        djtext = analyzed
        params={'purpose':"Removing Punctuations",'analyzed_text':analyzed}

        #return render(request,'analyze.html',params)
    if (fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': "Change to Uppercase", 'analyzed_text': analyzed}
        djtext =analyzed
        #return render(request, 'analyze.html', params)

    if(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': "Extra Space Remover", 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    #if (charactercount == "on"):
        #analyzed =("no of characters:" +str(len(djtext)))
       # params = {'purpose': "Character count", 'analyzed_text': analyzed}
       # djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char
            else:
                print("no")
        print("pre",analyzed)
        params = {'purpose': "New Line Remover", 'analyzed_text': analyzed}

    if(removepunc != "on" and newlineremover == "on" and extraspaceremover=="on" and fullcaps == "on"):
        return HttpResponse("Please select any operation and try again")

    return render(request, 'analyze.html', params)
