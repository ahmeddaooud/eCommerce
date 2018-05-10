import datetime

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.utils import timezone

from orders.models import Order


class SalesAjaxView(View):
    def get(self, request, *args, **kwargs):
        data = {}
        if request.user.is_staff:
            if request.GET.get('type') == 'week':
                data['labels'] = ["Mon", "Tue", "Wed", "Thurs", "Fri", "Sat", "Sun"]
                data['data'] = [123, 121, 12, 54, 78, 99, 52]
            if request.GET.get('type') == '4weeks':
                data['labels'] = ["Last week", "Two weeks ago", "Three weeks ago", "Four weeks ago"]
                data['data'] = [123, 121, 12, 54]
        return JsonResponse(data)


class SalesView(LoginRequiredMixin, TemplateView):
    template_name = 'analytics/sales.html'

    def dispatch(self, *args, **kwargs):
        user = self.request.user
        if not user.is_staff:
            return render(self.request, "400.html", {})
        return super(SalesView, self).dispatch(*args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context = super(SalesView, self).get_context_data(*args, **kwargs)
        qs = Order.objects.all().by_weeks_range(weeks_ago=10, number_of_weeks=10)
        context['today'] = qs.by_range(start_date=timezone.now().date()).get_sales_breakdown()
        context['this_week'] = qs.by_weeks_range(weeks_ago=1, number_of_weeks=1).get_sales_breakdown()
        context['last_four_weeks'] = qs.all().by_weeks_range(weeks_ago=5, number_of_weeks=4).get_sales_breakdown()
        return context
