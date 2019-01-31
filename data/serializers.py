from rest_framework import serializers
from .models import DataSet


class TagSerializerField(serializers.ListField):
    child = serializers.CharField()

    def to_representation(self, data):
        return data.values_list('name', flat=True)


class DataSetSerializer(serializers.ModelSerializer):
    labels = TagSerializerField()

    class Meta:
        model = DataSet
        fields = '__all__'
