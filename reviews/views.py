from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import ReviewForm
from .models import Review
from django.views import View

# Create your views here.

# AL POSTO DELLE FUNZIONI POSSIAMO USARE ANCHE LE CLASSI
class ReviewView(View):
    def get(self, request):
        form = ReviewForm()
        return render(request, "reviews/review.html", {
            "form": form
        })
        
    def post(self, request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/thank-you")
        return render(request, "reviews/review.html", {
            "form": form
        })
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


def thank_you(request):
    return render(request, "reviews/thank_you.html")