from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name=serializers.CharField(max_length=200)
    roll_no=serializers.IntegerField()
    city=serializers.CharField()