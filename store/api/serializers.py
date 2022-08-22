from rest_framework.serializers import ModelSerializer
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers
from api.models import Product, Order

class ProductSerializer(ModelSerializer):
      class Meta:
            model = Product
            fields = '__all__'

class OrderSerializer(ModelSerializer):
      
      class Meta:
            model = Order
            fields = '__all__'
      
      def to_representation(self, instance):
            rep = super().to_representation(instance)
            rep["products"] = ProductSerializer(instance.products.all(), many=True).data
            return rep

class StatSerializer(serializers.Serializer):
      metric_choice =( 
      ("price", "price"), 
      ("count", "count"), 
      )

      date_start = serializers.DateTimeField(required=True)
      date_end = serializers.DateTimeField(required=True)
      metric = serializers.ChoiceField(
                  choices = metric_choice)
      