from django.shortcuts import render
from django import http

from project_first_app import models


def owner(request: http.HttpRequest, owner_id: int) -> http.HttpResponse:
    try:
        owner_model = models.Owner.objects.get(id=owner_id)
    except models.Owner.DoesNotExist:
        raise http.Http404("Owner does not exist")
    return render(request, "owner.html", {"owner": owner_model})
