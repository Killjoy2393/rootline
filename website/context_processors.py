from .forms import ContactFormModelForm

def contact_form_processor(request):
    return {'contact_form': ContactFormModelForm()}