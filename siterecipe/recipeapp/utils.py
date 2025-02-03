menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить рецепт', 'url_name': 'add_recipe'},
    # {'title': 'Войти', 'url_name': 'login'},
]


class DataMixin:
    title_page = None
    category_selected = None
    extra_context = {}

    def __init__(self):
        if self.title_page:
            self.extra_context['title'] = self.title_page

        if self.category_selected is not None:
            self.extra_context['category_selected'] = self.category_selected

        # if 'menu' not in self.extra_context:
        #     self.extra_context['menu'] = menu

    def get_mixin_context(self, context, **kwargs):
        # context['menu'] = menu
        context['recipe_selected'] = None
        context.update(kwargs)
        return context
