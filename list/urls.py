from django.urls import path
from .views import (
    ItemListView,
    ItemDetailView,
    ItemUpdateView,
    ItemCreateView,
    ItemDeleteView,
    )

urlpatterns = [
    path('', ItemListView.as_view(), name='home'),
    path('item/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path('item/<int:pk>/edit', ItemUpdateView.as_view(), name='item_edit'),
    path('item/new/', ItemCreateView.as_view(), name='item_new'),
    path('item/<int:pk>/delete/', ItemDeleteView.as_view(), name='item_delete')
]