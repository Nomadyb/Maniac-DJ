from todo.models import TodoCategory, TodoTag
from page.models import Page


def global_todo_categories_context(request):
    categories = TodoCategory.objects.filter(is_active=True)
    return dict(
        global_todo_categories=TodoCategory.objects.filter(is_active=True)
        
    )



def global_page_context(request):
    pages = Page.objects.filter(is_active=True)
    return dict(
        global_pages=Page.objects.filter(is_active=True)
        
    )
