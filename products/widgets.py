from django.forms.widgets import ClearableFileInput
from django.utils.translation import gettext_lazy


class CustomClearableFileInput(ClearableFileInput):
    """Customize django image upload"""
    clear_checkbox_label = gettext_lazy('Remove')
    initial_text = gettext_lazy('Current Image')
    input_text = gettext_lazy('')
    template_name = (
        'products/custom_widget_templates/custom_clearable_file_input.html'
    )
