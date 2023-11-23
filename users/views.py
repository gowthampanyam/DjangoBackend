from django.shortcuts import render

# Create your views here.
def signup(request):
    if request.method == 'POST':
        payload = json.loads(request.body)

        first_name = payload.get('first_name', '')
        last_name = payload.get('last_name', '')
        email = payload.get('email', '')
        password = payload.get('password', '')
        confirm_password = payload.get('confirm_password', '')
        organisation = payload.get('tenant', None)
        user_type = payload.get('user_type', None)
        org_code = payload.get('org_code', None)
        redirect=payload.get('next', None) 