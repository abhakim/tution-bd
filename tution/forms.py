from django import forms
from .models import Contact, Post,PostFile
from .fields import ListTextWidget

class ContactForm(forms.ModelForm):
    name=forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your name'}),label='Your Name')
    class Meta:
        model=Contact
        fields='__all__'
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].label='Your Name:'
        self.fields['name'].initial='Your name'
        self.fields['phone'].initial='+8801'

    def clean_name(self):
        value=self.cleaned_data.get('name')
        num_of_w=value.split(' ')
        if len(num_of_w) > 3:
            self.add_error('name','Name can not be maximum 3 words.')
        else:
            return value
class ContactFormtwo(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        exclude=['user','id','slug','created_at','likes','views']
        widgets={
            'class_in':forms.CheckboxSelectMultiple(attrs={
                'multiple':True,
            }),
              'subject':forms.CheckboxSelectMultiple(attrs={
                'multiple':True,
              }),
        }
    def __init__(self,*args, **kwargs):
        _district_set=kwargs.pop('district_set',None)
        super(PostForm,self).__init__(*args,**kwargs)
        self.fields['district'].widget=ListTextWidget(data_list=_district_set, name='district-set')
class FileModelForm(forms.ModelForm):
    class Meta:
        model=PostFile
        fields=['image']