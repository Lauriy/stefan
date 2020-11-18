from django.views.generic import TemplateView


class EstonianIdCardView(TemplateView):
    template_name = 'eeidcard.html'


class HomeView(TemplateView):
    template_name = 'index.html'

class VoteView():
    pass