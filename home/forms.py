from .models import Comments
from .models import Reservation
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ('body',)

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ('name', 'surname', 'goods_products', 'foods_products', 'time', 'email', 'message')