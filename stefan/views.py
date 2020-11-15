from django.views.generic import TemplateView


class EstonianIdCardView(TemplateView):
    template_name = 'eeidcard.html'
