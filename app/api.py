from tastypie.resources import ModelResource
from app.models import Neumatico


class NeumaticoResource(ModelResource):
    class Meta:
        queryset = Neumatico.objects.all()
        resource_name = 'neumaticos'