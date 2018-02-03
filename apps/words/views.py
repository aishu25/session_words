from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

# Create your views here.
def index(request):
	
	return render(request,'words/index.html')

def process(request):
	word = request.POST['words']
	color = request.POST['color']
	
	if request.POST.get('big') == "fontbig": #big is "name" given in form &"fontbig" is value in form
		big = "on"
	else:
		big = "off"

	new_word = {'word' : word, # 'word' is used variable and 'word' has to be in jinja 
				'color' : color,
				'big' : big,
				'created_at' :"- added on " + datetime.now().strftime("%m-%d-%Y-%H:%M %p")	
				}

	if "word_list" not in request.session:
		request.session["word_list"] = [new_word]
	else: 
		saved_list = request.session["word_list"]
		saved_list.append(new_word)
		request.session['word_list'] = saved_list

	return redirect('/')

def clear(request):
	for key in request.session.keys():
		del request.session[key]
	return redirect('/')
