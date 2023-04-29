from rest_framework import serializers
from .models import StudentInfo
class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentInfo
        fields = ['name',
                  'roll',
                  'city',
                  ]
