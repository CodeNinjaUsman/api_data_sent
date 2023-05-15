from django.contrib import admin
from django.urls import path
from base.views import (
    DataSentCreateView, ObtainToken, UserCreateView, UserResetIPView,
    ChangeUserStatus,RemoveDataSentOBJ,RemoveDataSentOBJ_ID
)

# Register your URLs here.
urlpatterns = [
    path('admin/', admin.site.urls),
    # Endpoint for sending data
    path('api/data/', DataSentCreateView.as_view(), name='send_data'),
    # Endpoint for obtaining a token
    path('api/obtain_token/', ObtainToken.as_view(), name='obtain_token'),
    # Endpoint for creating a user
    path('api/user_create/', UserCreateView.as_view(), name='create_user'),
    # Endpoint for resetting a user's IP address
    path('api/ip_reset/', UserResetIPView.as_view(), name='ip_reset'),
    # Endpoint for changing a user's status
    path('api/change_user_status/', ChangeUserStatus.as_view(), name='change_user_status'),
    # Endpoint for deleting objects of data_sent for a user
    path('api/delete_data/', RemoveDataSentOBJ.as_view(), name='delete_data'),
    # Endpoint for deleting objects of data_sent for a user by id
    path('api/delete_data_id/', RemoveDataSentOBJ_ID.as_view(), name='delete_data_id')
]
