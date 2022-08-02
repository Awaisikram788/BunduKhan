from django.urls import path
from .views import *
urlpatterns = [
    path('', Home.as_view(), name="home"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('agents/', AgentsView.as_view(), name="agents"),
    path('property_grid/', PropertyGridView.as_view(), name="property-grid"),
    path('property_list/', PropertyListView.as_view(), name="property-list"),
    path('property_detail/<id>', PropertyDetailView.as_view(), name="property-detail"),
    path('property_submit/', PropertySubmitView.as_view(), name="property-submit"),
    path('pdf/', GeneratePdf.as_view()),
    # path('comingsoon/', ConingsoonView.as_view(), name="comingsoon"),
    path('about/', AboutView.as_view(), name="about"),
    path('thankyou/', ThanksView.as_view(), name="Greeting"),
    # path('builderhome/', BuilderHomeView.as_view(), name="builderhome"),
    # path('signup/', Registration.as_view(), name="registration"),
    # path('login/', Login.as_view(), name="login"),
    # path('reset/', forgetpassword.as_view(), name="forgetpassword"),
]