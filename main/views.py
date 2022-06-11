from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from main.models import *
from location.models import *
from property.models import *
from comments.models import *
from django.contrib import messages
from django.http import HttpResponse
from .process import html_to_pdf
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


# Create your views here.
class Home(View):
    template_name = 'index.html'
    def get(self,request):
        herosectiondata = Property.objects.all()
        comments = Comment.objects.all()
        context = {
            'data': herosectiondata,
            'comments': comments,
        }
        return render(request, self.template_name,context)


class AboutView(TemplateView):
    template_name = 'about.html'


class AgentsView(View):
    template_name = 'agents.html'


class PropertyGridView(TemplateView):
    template_name = 'property.html'


class PropertyListView(TemplateView):
    template_name = 'profile.html'


class PropertyDetailView(View):
    template_name = 'property-details.html'
    def get(self,request,id):
        detail = Property.objects.filter(id=id)
        comments = Comment.objects.filter(post__id=id)
        count = len(comments)
        no = [count]
        print(no)
        context  = {
            'details':detail,
            'comments':comments,
            'count':no,
        }
        return render(request,self.template_name,context)
    def post(self,request,id):
        if request.method == 'POST':
            name = request.POST.get('name','')
            email = request.POST.get('email','')
            website = request.POST.get('website','')
            message = request.POST.get('message','')
            post = Property.objects.get(id=request.POST.get('property_id'))
            comment = Comment(name=name,email=email,website=website,body=message,post=post)
            comment.save()
            return redirect('home')
            messages.success(request,'Comment post Successfully!')
class PropertySubmitView(TemplateView):
    template_name = 'property-submit.html'


class ContactView(View):
    def get(self, request):
        return render(request, 'contact.html')

    def post(self, request):
        if request.method == 'POST':
            form = request.POST.dict()
            sender = form.get("email")
            name = form.get("name")
            number = form.get("number")
            postcode = form.get("postcode")
            subject = "Message from contact us form"
            message = 'FROM : ' + form.get("name") + ' \nMessage : ' + form.get("message")
            # email_from = settings.EMAIL_HOST_USER
            # recipient_list = ['taimoor98.th@gmail.com',sender,]
            # send_mail( subject, message, email_from, recipient_list )
            messages.success(request, "Message sent sucessfully")
            Contact.objects.create(name=name, email=sender, phone_number=number, message=form.get("message"))

        return redirect('contact')

# class ConingsoonView(View):
#     template_name = 'comingsoon.html'

#     def get(self, request):
#         return render(request, self.template_name)

#     def post(self, request):
#         if request.method == 'POST':
#             form = request.POST.dict()
#             email = form.get("email")
#             Subscriber.objects.get_or_create(email=email)
#             messages.success(request, "The Subscriber has been successfully added")

#         return redirect('comingsoon')


# class AboutView(TemplateView):
#     template_name= 'about.html'

# class BuilderHomeView(View):
#     template_name= 'builderhome.html'

#     def get(self, request):
#         # province = Province.objects.all().values_list("province", flat=True)
#         # city = City.objects.all().values_list("city", flat=True)
#         province = Province.objects.all()
#         city = City.objects.all()
#         payload = {
#             "province": province,
#             "city": city,
#         }
#         print(payload)
#         return render(request, self.template_name, payload)


# class Registration(TemplateView):
#     template_name = 'signin.html'
#     def post(self, request):
#         if request.method=="POST":
#         # Get the post parameters
#             user=request.POST['name']
#             email=request.POST['email']
#             pass1=request.POST['pswd1']
#             pass2=request.POST['pswd2']

#             # check for errorneous input
#             # check for errorneous input
#             if len(user)<5:
#                 messages.error(request, " Your user name must be under 10 characters")
#                 return redirect('registration')
#             if User.objects.filter(username=user):
#                 messages.error(request, " user already exist")
#                 return redirect('registration')
#             if not user.isalnum():
#                 messages.error(request, " User name should only contain letters and numbers")
#                 return redirect('registration')
#             if (pass1!= pass2):
#                 messages.error(request, " Passwords do not match")
#                 return redirect('registration')
#             # Create the user
#             myuser = User.objects.create_user(username=user,email=email,password=pass1)
#             myuser.save()
#             messages.success(request, " Your BKRE account has been successfully created")
#         return redirect("registration")

# class Login(TemplateView):
#     template_name = 'login.html'
#     def post(self,request):
#         if request.method=="POST":
#                 # Get the post parameters
#             loginusername=request.POST['username']
#             loginpassword=request.POST['password']
#             loginemail=request.POST['email']
#             user=authenticate(username= loginusername, password= loginpassword)
#             if user is not None:
#                 login(request,user)
#                 messages.success(request, "Successfully Logged In")
#                 return redirect('home')
#             else:
#                 messages.error(request, "Invalid credentials! Please try again")
#                 return redirect("login")

# class forgetpassword(TemplateView):
#     template_name = 'Frget-pswd.html'
# Creating a class based view
class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        # getting the template
        pdf = html_to_pdf('property-details.html')

        # rendering the template
        return HttpResponse(pdf, content_type='application/pdf')