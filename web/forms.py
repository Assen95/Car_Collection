from django import forms

from exam.web.models import Profile, Car


class ProfileBaseForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('username', 'email', 'age', 'password')


class ProfileCreateForm(ProfileBaseForm):
        widgets = {
            'password': forms.(
                attrs={
                    'placeholder': '******',
                    'autocomplete': 'off',
                    'data-toggle': 'password',
                },
            ),
        },

        #def clean(self):
            #cleaned_data = super(ProfileCreateForm, self.clean())
            #username = cleaned_data.get('username')

            #if len(username) < 2:
                #raise forms.ValidationError('The username must be a minimum of 2 chars')


class ProfileEditForm(ProfileBaseForm):
    pass


class ProfileDeleteForm(ProfileBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__hidden_fields()

    def save(self, commit=True):
        if commit:
            Car.objects.all().delete()
            self.instance.delete()
        return self.instance

    def __hidden_fields(self):
        for _, field in self.fields.items():
            field.widget=forms.HiddenInput()


class CarBaseForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ('type', 'model_car', 'year', 'image_url', 'price')


class CarCreateForm(CarBaseForm):
    pass


class CarEditForm(CarBaseForm):
    pass


class CarDeleteForm(CarBaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__set_disabled_fields()

    def save(self, commit=True):
        if commit:
            self.instance.delete()

        return self.instance

    def __set_disabled_fields(self):
        for _, field in self.fields.items():
            field.widget.attrs['readonly'] = 'readonly'