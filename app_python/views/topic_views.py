from django.shortcuts import render, redirect, get_object_or_404
from ..models import Topic, TopicComment
from ..forms.topic_form import TopicForm
from django.views import generic
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required, permission_required


class Topics(generic.TemplateView):

    def __init__(self, **kwargs):
        super().__init__(kwargs)
        self.FILES = None
        self.method = None
        self.POST = None

    def topic_list(request):
        topics = Topic.objects.all()
        return render(request, 'pages/topics/index.html', {'topics': topics})

    def search(request):
        if request.method == "POST":
            query = request.POST['search']
            topics = Topic.objects.filter(title__icontains=query)
            return render(request, 'pages/topics/search.html', {'topics': topics})
        topics = Topic.objects.all()
        return render(request, 'pages/topics/search.html', {'topics': topics})

    def details(self, id):
        if self.method == "POST":
            comment = self.POST['comment']
            user = self.user
            topic = get_object_or_404(Topic, pk=id)
            
            topic_comment = TopicComment(comment=comment, user=user, topic=topic)
            topic_comment.save()

            return redirect('details_topic', id=id)

        topic = get_object_or_404(Topic, pk=id)
        return render(self, 'pages/topics/details.html', {'topic': topic, 'comments': topic.topiccomment_set.all()})


    @login_required
    def add(self):
        if self.method == "POST":
            title = self.POST['title']
            description = self.POST['description']
            owner = self.user

            topic = Topic(title=title, description=description, owner=owner)
            topic.save()

            return redirect('index_topics')

        return render(self, 'pages/topics/new.html')

    @login_required
    def delete(self, id):
        Topic.objects.filter(pk=id).delete()
        messages.success(self, "Le topic à bien été supprimée.")
        return redirect('index_topics')

