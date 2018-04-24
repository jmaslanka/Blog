from django.forms import ModelForm
from django.utils.translation import gettext as _


class ArticleAdminForm(ModelForm):
    def clean_similar(self):
        if len(self.cleaned_data['similar']) > 3:
            msg = _('You cannot put more than 3 similar articles.')
            self.add_error('similar', msg)
