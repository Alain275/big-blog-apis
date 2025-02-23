from rest_framework_simplejwt.views import (TokenRefreshView)
from django.urls import path
from api import views as api_view
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("token/", api_view.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("register/", api_view.RegisterView.as_view(), name='register'),
    path("user/profile/<user_id>/", api_view.ProfileView.as_view(), name='profile'),
    # post endpoint
    path('post/category/list/',api_view.CategoryListAPIView.as_view()),
    path('post/category/posts/<category_slug>/',api_view.PostCategoryListAPIView.as_view()),
    path('post/lists/',api_view.PostListAPIView.as_view()),
    path('post/detail/<slug>/',api_view.PostDetailAPIView.as_view()),
    path('post/like-post/',api_view.LikePostAPIView.as_view()),
    path('post/comment-post/',api_view.PostCommentAPIView.as_view()),
    path('post/bookmark-post/',api_view.BookmarkPostAPIView.as_view()),
    # dashbord-staff
    path('author/dashboard/stats/<user_id>/',api_view.DashboardStatsView.as_view()), 
    path('author/dashboard/reply-commet/',api_view.DashboardReplyCommentAPIView.as_view()),
    path('author/dashboard/noti-mark-seen/',api_view.DashboardMarkNotificationseen.as_view()),
    path('author/dashboard/noti-list/<user_id>/',api_view.DashboardNotificationLists.as_view()),
    path('author/dashboard/comment-list/<user_id>/',api_view.DashboardCommentList.as_view()),
    path('author/dashboard/post-create/',api_view.DashboardPostCreateAPIView.as_view()),
    path('author/dashboard/post-detail/<user_id>/<post_id>/', api_view.DashboardPostEditAPIView.as_view())
   
]

