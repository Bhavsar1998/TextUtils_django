#I have created this file = Himanshu
from argparse import ArgumentDefaultsHelpFormatter
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

#basic/ render and pass template
def index(request):
    paramsVariable = {"name": "Himanshu", "city": "indore"}
    return render(request,     'index.html',          paramsVariable) #accessed from MyTemplate directory
                # arg1      arg2 - template arg3(optional)- context dictionary

# def home(request):
#     return HttpResponse("My Django textutils App")

# # def display1txt(request):
# #     file = open("E:/projects/Django/textUtils/textUtils/one.txt", "r")
# #     content = file.read()
# #     return HttpResponse(content)

# #laying pipeline for textUtils !!
# def removePunctuation(request):
#     #Get the text
#     gotText = request.GET.get('text', 'defaultValue')
#     print(gotText)
    
#     #analyze the text
#     # ...
#     return HttpResponse("removePunctuations <br><a href = '/'>Back button</a>")

# def capitalizeFirst(request):
#     return HttpResponse("capitalizeFirst <br><a href = '/'>Back button</a>")

# def removeSpace(request):
#     return HttpResponse("removeSpace <br><a href = '/'>Back button</a>")

# def removeNewLine(request):
#     return HttpResponse("removeNewLine <br><a href = '/'>Back button</a>")

# def charCount(request):
#     return HttpResponse("charCount <br><a href = '/'>Back button</a>")

#analyze backend code
def analyze(request):
    #Get text eneterd in Text Area
    textFromTextArea = request.POST.get('text', 'default')

    #Check checkbox value
    removePunctuationCheck = request.POST.get('removePunctuation', "off")
    upperCase = request.POST.get('upperCase', "off")
    removeExtraSpace = request.POST.get('removeExtraSpace', "off")
    charCount = request.POST.get('charCount', "off")

    if charCount == "off" and removeExtraSpace == "off" and removePunctuationCheck == "off" and upperCase == "off":
        # return HttpResponse("No Checkbox selected !")
        return render(request, 'alertRed.html')

    if removePunctuationCheck == "on":
        analyzedText = ""
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in textFromTextArea:
            if char not in punctuations:
                analyzedText += char
        params = {'purpose': "Remove Punctuations", 'analyzedText' : analyzedText}
        textFromTextArea = analyzedText
        # return render(request, 'analyze.html', params)
    
    if upperCase == "on":
        analyzedText = ""
        for char in textFromTextArea:
            analyzedText += char.upper()
        params = {'purpose': "UPPER CASE", 'analyzedText' : analyzedText}
        textFromTextArea = analyzedText
        # return render(request, 'analyze.html', params)

    if removeExtraSpace == "on":
        analyzedText = ""
        for index, char in enumerate(textFromTextArea):
            if not(textFromTextArea[index] == " " and textFromTextArea[index+1] == " "):
                analyzedText += char
        params = {'purpose': "Remove Extra Space", 'analyzedText' : analyzedText}
        textFromTextArea = analyzedText
        # return render(request, 'analyze.html', params)

    if charCount == "on": 
        #char count is length of string here
        params = {'purpose': "Character count", 'analyzedText' : len(textFromTextArea)}
        # return render(request, 'analyze.html', params)
    return render(request, 'analyze.html', params)

def about(request):
    return HttpResponse("This is a Text Utils App. Here you can analyze your text as per your choice of operation.")

def contactUs(request):
    return HttpResponse("Please mail us @textUtilsOrg.in")
    