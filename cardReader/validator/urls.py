from django.conf.urls import include, url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
# router.register(r'creditCard', views.CreditCardViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^r/', include(router.urls)),
    # url('validate/', include('rest_framework.urls', namespace='rest_framework'))
	url(r'validcc', views.CreditCardView.as_view()),
]