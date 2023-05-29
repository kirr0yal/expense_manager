from django.urls import path
from app.views import *
from app.views_auth import *

urlpatterns = [
    path('', index, name='index'),
    path('register/', registration, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('account/', account, name='account'),
    path('account/<str:transaction_type>/', account, name='account_filtered'),
    path('create/', create_view, name='create'),
    path('delete/<int:transaction_id>', delete_view, name='delete'),
    path('edit/<int:transaction_id>', edit_view, name='edit'),
    path('add10/', add10, name='add10')
]