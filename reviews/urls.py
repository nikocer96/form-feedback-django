from django.urls import path
from . import views

urlpatterns = [
    path("", views.ReviewView.as_view()),
    path("thank-you", views.ThankYou.as_view()),
    path("reviews", views.ReviewsListView.as_view(), name="review_list"),
    # VA pk SE STIAMO USANDO DetailView
    path("reviews/favorite", views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>", views.SingleReviewView.as_view(), name="review_single"),
    path("reviews/delete/<int:pk>", views.ReviewDelete.as_view(), name="review_delete")
]
