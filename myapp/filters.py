from .models import Employee
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Employee
        fields = ['name', 'pannumber', 'age','gender', 'email', 'city', ]