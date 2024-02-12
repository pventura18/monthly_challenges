from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template.loader import render_to_string

montyly_chanllenges = {
    'january': 'Eat no meat for 30 days!',
    'fabruary': 'Walk for at least 20 minutes every day!',
    'march': 'Learn Django for at least 20 minutes every day!',
    'april': 'Eat no meat for 30 days!',
    'may': 'Walk for at least 20 minutes every day!',
    'june': 'Learn Django for at least 20 minutes every day!',
    'july': 'Eat no meat for 30 days!',
    'august': 'Walk for at least 20 minutes every day!',
    'september': 'Learn Django for at least 20 minutes every day!',
    'october': 'Eat no meat for 30 days!',
    'november': 'Walk for at least 20 minutes every day!',
    'december': None,
}

def index(request):
    list_items = ""
    months = list(montyly_chanllenges.keys())
    
    return render(request, "challenges/index.html", {
        "months": months
    })

def montyly_chanllenge(request, month):
    try:
        challenge_text = montyly_chanllenges[month]
    except:
        return HttpResponseNotFound("This month is not supported!")
    return render(request,"challenges/challenge.html", {
        "text": challenge_text,
        "month_name": month
    })

def montyly_chanllenge_number(request, month):
    try:
        redirect_month = list(montyly_chanllenges.keys())[month - 1]
        redirect_path = reverse("month-challenge", args=[redirect_month])
    except:
        raise Http404()
    return HttpResponseRedirect(redirect_path)