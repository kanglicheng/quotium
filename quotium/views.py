from requests.exceptions import HTTPError

from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.utils import timezone
from django.views.generic import (TemplateView,ListView,
                                  DetailView,CreateView,
                                  UpdateView,DeleteView)

from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import PropertyData, QuoteRecord
from .forms import SubmissionForm
from .utils import post_property_data


# Create your views here.
class AboutView(TemplateView):
    template_name = 'quotium/about.html'


class QuoteListView(ListView):
    model = QuoteRecord

    def get_queryset(self):
        return QuoteRecord.objects.select_related('property_data'
                                                  ).filter(created_at__lte=timezone.now()).order_by('-created_at')


class CreateSubmissionView(CreateView):

    form_class = SubmissionForm

    model = PropertyData

    success_url = '/success'

    def form_valid(self, form):
        # save PropertyData
        try:
            with transaction.atomic():
                property_data = form.save()
                price = post_property_data(property_data)
                QuoteRecord.objects.create(property_data=property_data,
                                           monthly_estimate=price)
  
            return render(self.request, 'quotium/success.html', {'price': price})
        except HTTPError as er:
            print('Error occurs when invoking API, due to %s' % er)
            return HttpResponse("something went wrong here, please go back %s", er)
        except Exception as er:
            print('Error occurs %s', er)
            return HttpResponse("something went wrong here, please go back %s", er)


    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


class SubmissionSuccessView(TemplateView):

    template_name = 'quotium/success.html'

