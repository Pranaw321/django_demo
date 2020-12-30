from django.http import JsonResponse


def login(self):
    data = {
        "token": str(self),
        "msg": "Login success"
    }
    return JsonResponse(data, safe=False)
