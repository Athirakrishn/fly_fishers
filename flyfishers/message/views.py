from django.shortcuts import render

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from flyfishers import settings

from PIL import Image
import pytesseract as t
# from college import settings
# C:\Program Files\Tesseract-OCR\tesseract.exe
# t.pytesseract.tesseract_cmd = r'C:\Users\rashi\AppData\Local\Tesseract-OCR\tesseract.exe'

import openai
openai.api_key = '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'

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=prompt,
        max_tokens=100,
        temperature=0.7,
        n=1,
        stop=None,
        timeout=10,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    if 'choices' in response and len(response['choices']) > 0:
        return response['choices'][0]['text'].strip()
    else:
        return None

# @csrf_exempt

def chatload(request):
    return render(request, 'message/chat.html')

def up(request):
    # if request.method=="POST" :
    vv=request.GET.get('cmsg')
    print(vv,'hello')

    greet=['hai','hi','hello','hii']
    if vv in greet:
        ans='hello'
    else:
        ans = chat_with_gpt(vv)


    print(ans)
    context = {
                 "cresp": ans,
            }
    return JsonResponse(context)
