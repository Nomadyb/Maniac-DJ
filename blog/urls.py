from blog.views import all_post_view, category_view, tag_view, post_detail_view
from django.urls import path
from page.views import  page_view  


# app_name = 'blog'

# urlpatterns = [

        
#     path('<slug:page_slug>/', page_view,name='page_view'),

    


#     # path('', all_todos_view, name='all_todos_view'),
#     # path('category/<slug:category_slug>/', category_view, name='category_view'),
#     # path('tag/<slug:tag_slug>/', tag_view, name='tag_view'),



#     # path('<slug:category_slug>/<int:id>/', todo_detail_view,
#     #      name='todo_detail_view'),  # todo detail

    


# ]


app_name = 'blog'

urlpatterns = [
    path('', all_post_view, name='all_post_view'),
    path('category/<slug:category_slug>/', category_view, name='category_view'),
    path('tag/<slug:tag_slug>/', tag_view, name='tag_view'),

    path('category/<slug:category_slug>/<slug:post_slug>/',
         post_detail_view, name='post_detail_view'),
]
