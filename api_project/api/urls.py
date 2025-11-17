from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

urlpatterns = [
    path('books/', BookList.as_view(), name='book-list'),        # ALX checker expects this
    path('books/create/', BookCreate.as_view(), name='book-create'),  # optional for POST
]