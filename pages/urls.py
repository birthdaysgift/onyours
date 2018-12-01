from django.urls import path

from .views import EditView, PageView, SendFriendRequestView, \
    AcceptFriendRequestView, DenyFriendRequestView, RemoveFriendView, \
    CancelFriendRequestView, FriendsListView, DeletePostView, \
    PhotosListView, AddNewPhotoView, DetailPhotoView,\
    DeletePhotoView, VideosListView, AddNewVideoView, DetailVideoView, \
    DeleteVideoView, LikePostView, DislikePostView

app_name = "pages"

urlpatterns = [
    path("<str:username>/", PageView.as_view(), name="page"),
    path("<str:username>/edit/", EditView.as_view(), name="edit"),
    path("<str:username>/delete_post/<int:post_id>/", DeletePostView.as_view(),
         name="delete_post"),
    path('<str:username>/like_post/<int:post_id>/', LikePostView.as_view(),
         name='like_post'),
    path('<str:username>/dislike_post/<int:post_id>/', DislikePostView.as_view(),
         name='dislike_post'),
    path("<str:username>/send_friend_request/", SendFriendRequestView.as_view(),
         name="send_friend_request"),
    path("<str:username>/reset_friend_request/",
         CancelFriendRequestView.as_view(), name="cancel_friend_request"),
    path("<str:username>/accept_friend_request/",
         AcceptFriendRequestView.as_view(), name="accept_friend_request"),
    path("<str:username>/deny_friend_request/", DenyFriendRequestView.as_view(),
         name="deny_friend_request"),
    path("<str:username>/remove_friend/", RemoveFriendView.as_view(),
         name="remove_friend"),
    path("<str:username>/friends/", FriendsListView.as_view(), name="friends"),
    path('<str:username>/photos/<int:photo_id>/', DetailPhotoView.as_view(),
         name='detail_photo'),
    path("<str:username>/photos/", PhotosListView.as_view(), name="photos"),
    path("<str:username>/add_new_photo/", AddNewPhotoView.as_view(),
         name="add_new_photo"),
    path("<str:username>/delete_photo/<int:userphoto_id>/",
         DeletePhotoView.as_view(),
         name="delete_photo"),

    path('<str:username>/videos/<int:video_id>/', DetailVideoView.as_view(),
         name='detail_video'),
    path("<str:username>/videos/", VideosListView.as_view(), name="videos"),
    path("<str:username>/add_new_video/", AddNewVideoView.as_view(),
         name="add_new_video"),
    path("<str:username>/delete_video/<int:uservideo>/",
         DeleteVideoView.as_view(),
         name="delete_video")
]
