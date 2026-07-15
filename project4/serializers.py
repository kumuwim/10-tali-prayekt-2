from rest_framework.serializers import ModelSerializer
from .models import Student

class StudentSerializers(ModelSerializer):
    class Meta:
        model=Student
        fields = ["id", "name", "sur_name", "age", "descriptions"]
        read_only_fields=["id","created_at"]