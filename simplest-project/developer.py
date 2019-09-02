# a standalone basic django app from scratch

# step 1: create our views
# 
# inspect incoming HTTP request
# then query or construct the data for response. usually the index.py
from django.http import HttpResponse
def index(request):
    return HttpResponse('developer')

# step 2: setup urls
# 
# associate the view index with a URL pattern. usually the setup.py
from django.conf.urls import url
urlpatterns = (
    url(r'^$', index),
)

# step 3: setup settings
# 
# run in debug mode. usually the settings.py
from django.conf import settings
settings.configure(
    DEBUG=True,
    SECRET_KEY='anonproductionsecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
)

# the main. usually manage.py. 
# 
# run with: python3.7 developer.py runserver
import sys
if __name__ == "__main__":
    from django.core.management import execute_from_command_line
    execute_from_command_line(sys.argv)
