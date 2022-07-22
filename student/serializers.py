import datetime

import journal as journal
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
import time
from .models import Students


class StudentSerializers(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)
    student_number = serializers.IntegerField(max_value=9999999999, min_value=0,
                                              validators=[
                                                  UniqueValidator(queryset=Students.objects.all(), message="学号已存在")])
    age = serializers.IntegerField(max_value=200, min_value=0)
    cls = serializers.IntegerField(max_value=9999, min_value=100,
                                   error_messages={"max_value": "班级最大值为9999", "min_value": "班级最小值为100"})
    score = serializers.FloatField(max_value=1000, min_value=0)
    remake = serializers.CharField(help_text="备注", label="备注", max_length=200, allow_blank=True)
    create_date = serializers.DateTimeField(read_only=True)
    update_time = serializers.DateTimeField(read_only=True)

    # class Meta:
    #     model = Students
    #     fields = "__all__"
    #     read_only_fields = ("create_date", "update_date")

    def create(self, validated_data):
        student_obj = Students.objects.create(**validated_data)
        return student_obj

    def update(self, instance, validated_data):
        instance.name = validated_data["name"]
        instance.age = validated_data["age"]
        instance.student_number = validated_data["student_number"]
        instance.cls = validated_data["cls"]
        instance.score = validated_data["score"]
        instance.remake = validated_data["remake"]
        instance.save()
        return instance

    def to_representation(self, instance):
        tmp = super().to_representation(instance=instance)
        return tmp



class PatchStudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=20, required=False)
    age = serializers.IntegerField(max_value=200, min_value=0, required=False)
    cls = serializers.IntegerField(max_value=9999, min_value=100, required=False,
                                   error_messages={"max_value": "班级最大值为9999", "min_value": "班级最小值为100"})
    score = serializers.FloatField(max_value=1000, min_value=0, required=False)
    remake = serializers.CharField(required=False, help_text="备注", label="备注", max_length=200, allow_blank=True)
