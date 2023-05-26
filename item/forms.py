from django import forms

#local imports
from .models import Item

INPUT_CLASSES = 'w-full py-4 px-6 rounded-xl border'

class NewItemForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Not selected"

    class Meta:
        model = Item
        fields = ('category', 'name', 'description', 'price', 'image')

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
 
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),           
            
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        } 


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'description', 'price', 'image', 'is_sold')

        widgets = {
            'name': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),

            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            }),
 
            'price': forms.NumberInput(attrs={
                'class': INPUT_CLASSES
            }),           
            
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            })
        } 