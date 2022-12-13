from django.forms import ModelForm
from .models import UserProfile, Note

class UserProfileForm(ModelForm):
   class Meta:
      model = UserProfile
      fields= '__all__'
      exclude= ['username']

class NoteForm(ModelForm):
   class Meta:
      model = Note
      fields= '__all__'
      exclude= ['user_profile']
      