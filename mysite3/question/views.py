from django.shortcuts import render_to_response
from question.models import Question
from django.template import RequestContext
from question.forms import QuestionForm
from django.utils import timezone
from django.shortcuts import render_to_response, redirect

def index(request):
        questions = Question.objects.all()
        return render_to_response('index.html',{'questions': questions})

def question_detail(request, question_id):
        question = Question.objects.get(pk=question_id)
        return render_to_response('question_detail.html',{'question': question})
    
def question_create(request):
        if request.method == 'POST':
                form = QuestionForm(request.POST)
                if form.is_valid():
                        question = Question(subject=form.cleaned_data['subject'], publication_date=timezone.now())
                        question.save()
                        return redirect('/questions')
        else:
                form = QuestionForm()
        return render_to_response('question_create.html',{'form': form}, context_instance=RequestContext(request))    