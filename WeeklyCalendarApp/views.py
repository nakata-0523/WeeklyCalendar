from django.shortcuts import render
from django.views.generic import TemplateView
from .mixins import WeekCalendarMixin

# Create your views here.
class WeekCalendar(WeekCalendarMixin, TemplateView):
    template_name = 'week.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_week_calendar()
        context.update(calendar_context)
        return context