from django.shortcuts import render, HttpResponseRedirect, reverse
from ghostpost_app.models import BR_Post
from ghostpost_app.forms import BR_PostForm

# Create your views here.


def index(request):
    my_posts = BR_Post.objects.filter().order_by('-id')
    return render(request, "index.html", {"posts": my_posts})


def new_post_form_view(request):
    if request.method == "POST":
        form = BR_PostForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            BR_Post.objects.create(
                title=data.get('title'),
                boast_roast=data.get("boast_roast"),
                up_field=data.get("up_field"),
                down_field=data.get("down_field"),
            )
            return HttpResponseRedirect(reverse("homepage"))

    form = BR_PostForm()
    return render(request, "newpost.html", {"form": form})

# Sohail went over this a bit during study hall, played around with calling and documentation to fill in the rest on my own though.
# HTTP_REFERER was referenced in Slack by Christopher


def upvote_view(request, post_id):
    post = BR_Post.objects.get(id=post_id)
    post.up_field = post.up_field + 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def downvote_view(request, post_id):
    post = BR_Post.objects.get(id=post_id)
    post.down_field = post.down_field + 1
    post.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def votes_view(request):
    votes = sorted(BR_Post.objects.all(), key=lambda votes: votes.votes)[::-1]
    return render(request, "votes.html", {"votes": votes})


def boasts_view(request):
    boast_post = BR_Post.objects.filter(boast_roast=True).order_by('-id')
    return render(request, "boasts.html", {"boast_posts": boast_post})


def roasts_view(request):
    roast_post = BR_Post.objects.filter(boast_roast=False).order_by('-id')
    return render(request, "roasts.html", {"roast_posts": roast_post})
