from django.urls import path
from  .views import  all_todos_view,category_view, todo_detail_view, tag_view


app_name = 'todo'



urlpatterns = [
    # all todos
    path('', all_todos_view, name='all_todos_view'),
    path('category/<slug:category_slug>/', category_view, name='category_view'),
    path('tag/<slug:tag_slug>/', tag_view, name='tag_view'),


    
    path('<slug:category_slug>/<int:id>/', todo_detail_view, name='todo_detail_view'), # todo detail

    
]
# Compare this snippet from page/views.py:
