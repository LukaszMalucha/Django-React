from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render

class CurrentUserView(APIView):
    def get(self, request, *args, **kwargs):
        if str(request.user) != "AnonymousUser":
            return Response({"email": request.user.email })
        else:
            return Response({"error": "Anonymous"})


def account_locked(request):
    return render(request, 'account-locked.html')