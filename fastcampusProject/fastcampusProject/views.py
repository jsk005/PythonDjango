from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from accounts.decorators import login_required
import logging
from accounts.models import User

@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        user_id = self.request.session.get('user')
        if user_id:
            user = User.objects.get(pk=user_id)
            logging.warning(user.username)
            context = super(HomeView, self).get_context_data(**kwargs)
            context['user'] = user
            return context

