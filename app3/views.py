from django.shortcuts import render
from .models import quizmodel, Students
# Create your views here.

# def table_feed(request):
#     if request.method == 'POST':

def quiz(request):
    if request.method == 'POST':
        questions = quizmodel.objects.all()
        score, wrong, right = 0, 0, 0
        for q in questions:
            if q.ans == request.POST.get(q.question):
                score += 2 # put variable marks fetched from marks field q.marks
                right += 1
            else:
                wrong += 1
        name = request.user.username
        s = Students.objects.create(name = name, score = score, right=right, wrong = wrong)
        context = {
            'score' : score, 
            'correct' : right, 
            'incorrect' : wrong, 
            
        }

        return render(request,'result.html',context)#note in post method we are rendering not redirecting
    else:
        questions=quizmodel.objects.all()
        context = {
            'questions':questions
        }
        return render(request,'quiz.html',context)
            