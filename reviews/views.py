from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View
from django.views.generic.base import TemplateView # E' PIU' SPECIFICA
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView, CreateView, DeleteView
from django.urls import reverse

# Create your views here.

# AL POSTO DELLE FUNZIONI POSSIAMO USARE ANCHE LE CLASSI
# class ReviewView(View):
#     def get(self, request):
#         form = ReviewForm()
#         return render(request, "reviews/review.html", {
#             "form": form
#         })

#      def post(self, request):
    #     form = ReviewForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponseRedirect("/thank-you")
    #     return render(request, "reviews/review.html", {
    #         "form": form
    #     })
        
# class ReviewView(FormView):
#     form_class = ReviewForm
#     template_name = "reviews/review.html"
#     success_url = "thank-you"
    
#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)
        

# CREATEVIEW SALVA DIRETTAMENTE I DATI NEL DB
class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "thank-you"
    
class ReviewDelete(DeleteView):
    model = Review
    template_name = "reviews/review_list.html"
    
    def get_success_url(self):
        return reverse('review_list')  
        
# -------------------------
                
# def review(request):
#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             # QUESTO SI UTILIZZA QUANDO VOGLIO MODIFICARE QUALCOSA
#             # exist_data = Review.objects.get(pk=1)
#             # review = ReviewForm(request.POST, instance=exist_data)
            
#             # POSSO CHIAMARE DIRETTAMENTE form.save() PERCHE' IN FORMS STO USANDO MODELFORM E NON FORM, SENNO' NON L'AVREI POTUTO CHIAMARE DIRETTAMENTE
#             form.save()
#             # review = Review(username_form = form.cleaned_data["username_form"], review_text = form.cleaned_data["review_text"], rating = form.cleaned_data["rating"])
#             # review.save()
#             return HttpResponseRedirect("/thank-you")
#     else:
#         form = ReviewForm()
        
#     return render(request, "reviews/review.html", {
#         "form": form
#     })

class ThankYou(TemplateView):
    # template_name E' UN NOME DI PROPRIETA' èREVISTO DA DJANGO
    template_name = "reviews/thank_you.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This work"
        return context
    

# def thank_you(request):
#     return render(request, "reviews/thank_you.html")

#-------------------------------------

# class ReviewsListView(TemplateView):
#     template_name = "reviews/review_list.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         reviews = Review.objects.all()
#         context["reviews"] = reviews 
#         return context

# IN QUESTO CASO UTILIZZIAMO LA VISTA ListView CHE E' PIU' ADATTA PER LE LISTE
class ReviewsListView(ListView):
     template_name = "reviews/review_list.html"
     model = Review
     context_object_name = "reviews"
     
     #RESTITUISCE LE REVIEWS SOLO DI QUELLI CHE HANNO UN RATING MAGGIORE DI 3
    #  def get_queryset(self):
    #     base_query = super().get_queryset()
    #     data = base_query.filter(rating__gt=3)
    #     return data
     
     
#--------------------------------------  
 
    
# class SingleReviewView(TemplateView):
#     template_name = "reviews/single_review.html"
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         review_id = kwargs["id"]
#         selected_review = Review.objects.get(pk = review_id)
#         context["reviews"] = selected_review
#         return context
    

class SingleReviewView(DetailView):
    template_name = "reviews/single_review.html"
    # NELL'HTML PRENDO I DATI SCRIVENDO review IN MINUSCOLO OPPURE USO object NELL'HTML
    model = Review
    
#------------------------------