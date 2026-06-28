from django.shortcuts import render

from .models import Topic


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
