from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Portfolio


class PortfolioView(generic.ListView):
    template_name = 'portfolio/portfolio_index.html'
    context_object_name = 'latest_portfolio_list'

    def get_queryset(self):
        """
        Return the last five published portfolio (not including those set to be
        published in the future).
        """
        return Portfolio.objects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')[:5]


class DetailView(generic.DetailView):
    model = Portfolio
    template_name = 'portfolio/portfolio_detail.html'

    def get_queryset(self):
        """
        Excludes any posts that aren't published yet.
        """
        return Portfolio.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Portfolio
    template_name = 'portfolio/porfolio_results.html'