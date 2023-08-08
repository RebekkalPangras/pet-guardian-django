from django.shortcuts import render, redirect
from django.views import View
from .models import LostPetReport, Pet
from .forms import LostPetReportForm

class SinglePageView(View):
    template_name = 'single_page.html'

    def get(self, request):
        pets = Pet.objects.filter(owner__isnull=False)
        form = LostPetReportForm()
        context = {'pets': pets, 'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = LostPetReportForm(request.POST)
        if form.is_valid():
            pet = Pet.objects.create(
                pet_type=form.cleaned_data['pet_type'],
                age=form.cleaned_data['age'],
                name=form.cleaned_data['name'],
                breed=form.cleaned_data['breed'],
                sex=form.cleaned_data['sex'],
                color=form.cleaned_data['color'],
                owner=form.cleaned_data['reported_by']
            )
            lost_pet_report = LostPetReport(
                reported_by=form.cleaned_data['reported_by'],
                pet=pet,
                report_date=form.cleaned_data['report_date'],
                last_seen_location=form.cleaned_data['last_seen_location'],
                description=form.cleaned_data['description']
            )
            lost_pet_report.save()
            
            return redirect('single_page')
        pets = Pet.objects.filter(owner__isnull=False, lostpetreport__is_found=False)
        context = {'pets': pets, 'form': form}
        return render(request, self.template_name, context)
