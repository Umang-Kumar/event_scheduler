from django.shortcuts import render, redirect
from django.views import generic, View
from django.http import JsonResponse
from django.urls import reverse


from .models import *
from .forms import *


# Create your views here.
class IndexView(generic.ListView):
    model = EventCreation
    template_name = 'backend/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['events'] = EventCreation.objects.filter(is_active=True)
        return context


class CreateEventView(generic.CreateView):
    model = EventCreation
    template_name = 'backend/create_event.html'

    def get(self, request):
        form = EventCreationForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = EventCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        return render(request, self.template_name, {'form': form})
    

class EventDetailView(generic.DetailView):
    model = EventCreation
    template_name = 'backend/event_detail.html'
    slug_field = 'link'
    slug_url_kwarg = 'link'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['available_slots'] = self.object.available_slots()
        return context

    def post(self, request, *args, **kwargs):
        event = self.get_object()
        available_slots = event.available_slots()

        if available_slots > 0:
            # Get the selected slot data from the POST request
            start_time = request.POST.get('start_time')
            end_time = request.POST.get('end_time')

            # Check if the slot is already booked
            if event.is_slot_booked(start_time, end_time):
                # Handle the case when the slot is already booked
                print("Slot is already booked.")
            else:
                # Book the slot
                event.booked_slots += 1
                event.save()

                # Create a BookedSlot instance
                booked_slot = BookedSlot(event=event, start_time=start_time, end_time=end_time)
                booked_slot.save()

                return redirect(reverse('backend:event-detail', args=[event.link]))
        else:
            # Handle the case when no available slots are left
            print("No more available slots.")

        return render(request, self.template_name, {'object': event, 'available_slots': available_slots})


class EventBookedSlotsView(View):
    def get(self, request, link):
        try:
            event = EventCreation.objects.get(link=link)
            booked_slots = BookedSlot.objects.filter(event=event)

            booked_slots_data = []
            for slot in booked_slots:
                booked_slots_data.append({
                    'start_time': slot.start_time.isoformat(),
                    'end_time': slot.end_time.isoformat(),
                })

            return JsonResponse({'booked_slots': booked_slots_data})

        except EventCreation.DoesNotExist:
            return JsonResponse({'error': 'Event not found'}, status=404)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
