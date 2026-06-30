from django.shortcuts import render , redirect

from .models import Topic , Entry

from .forms import TopicForm, EntryForm


def index(request):
    """The Home page for Learning Log."""
    return render(request, 'Learning_Logs/index.html')


def topics(request):
    """Show all the topics"""
    topics = Topic.objects.order_by("date_added")
    context = {'topics': topics}
    return render(request, 'Learning_Logs/topics.html', context)


def topic(request, topic_id):
    """Show a single topic and all its entries."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'Learning_Logs/topic.html', context)

def new_topic(request):
    """Add a new topic"""
    if request.method != 'POST':
        # no data has been submitted -> blank form
        form = TopicForm()
        context = {'form': form}
        return render(request, 'Learning_Logs/new_topic.html', context)

    # POST data submitted; process data.
    form = TopicForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('Learning_Logs:topics')

    # Display a blank or individual form.
    context = {'form': form}
    return render(request, 'Learning_Logs/new_topic.html', context)


def new_entry(request , topic_id):
    """Add a new entry for a particular topic."""
    topic = Topic.objects.get(id = topic_id)

    if request.method != 'POST':
        # No dta submitted create a blank form.
        form = EntryForm()
    else:
        #POST data submitted process Data.
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('Learning_Logs:topic', topic_id=topic_id)
        
    # Display a blank or invalid form
    context = {'topic' : topic , 'form' : form}
    return render (request , 'Learning_Logs/new_entry.html' , context)


def edit_entry(request , entry_id):
    """Edit an exixsting entry."""
    entry = Entry.objects.get(id = entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # initial request: pre-fill form with the current entry.
        form = EntryForm(instance = entry)
    else:
        # Post data submitted: process data.
        form = EntryForm(instance = entry , data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('Learning_Logs:topic' , topic_id = topic.id)
        
    context = {'entry' : entry , 'topic': topic , 'form' : form}
    return render(request , 'Learning_Logs/edit_entry.html' , context)
