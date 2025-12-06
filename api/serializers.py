from rest_framework import serializers
from .models import Category,Task
from django.utils import timezone

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    class Meta:
        
        model = Task
        fields = ['id', 'name', 'description', 'status','due_date' ,'updated_at', 'created_at', 'category']


    # # object lavel  TODO Bu hammasini tekshiradi
    # def validate(self, attrs): 
    #     if attrs['due_date'] < timezone.now():
    #         raise serializers.ValidationError({'due_date':'hozirga vaqtdan keyingi vaqtni kiriting'})
    #     return super().validate(attrs)


    # field lavel TODO bu bittasini tekshiradi
    def validate_due_date(self,value):
        if value < timezone.now():
            raise serializers.ValidationError({'due_date':'hozirga vaqtdan keyingi vaqtni kiriting'})
        return value
    

class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)
    password2 = serializers.CharField(required=True)


    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password2':'password bilan mos emas'})
        return super().validate(attrs)
    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)







