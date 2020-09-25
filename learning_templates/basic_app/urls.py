from django.conf.urls import url
from basic_app import views

# TEMPLATE TAGGING
app_name = 'basic_app' # dit laat template tagging toe

# we hebben hier dus al domeinnaam.com/basic_app
urlpatterns = [
    url(r'^relative/$',views.relative,name='relative'), # /$ zegt gelijk wat erachter komt
    # dus: domeinnaam.com/basic_app/relative
    url(r'^other/$',views.other,name="other"),
    # dus: domeinnaam.com/basic_app/other
]

