from todo.models import TodoCategory, TodoTag


def global_todo_categories_context(request):
    categories = TodoCategory.objects.filter(is_active=True)
    return dict(
        global_todo_categories=TodoCategory.objects.filter(is_active=True)
        
    )


