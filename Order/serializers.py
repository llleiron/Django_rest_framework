from rest_framework import serializers
from Customer.models import Customer
from Employee.models import Employee
from Shipper.models import Shipper 
from Order.models import Order 
class OrderCreateSerializer(serializers.ModelSerializer):

    customer_id = serializers.IntegerField()
    employee_id = serializers.IntegerField()
    shipper_id = serializers.IntegerField()
    

    class Meta:
        model = Order
        fields = (
            'customer_id',
            'employee_id',
            'shipper_id',
            'orderDate'
        )

    def create(self, validated_data):

        customer_id = validated_data['customer_id']
        employee_id = validated_data['employee_id']
        shipper_id = validated_data['shipper_id']

        try:
            customer = Customer.objects.get(pk=customer_id)
        except Customer.DoesNotExist:
            raise serializers.ValidationError('Customer does not exist, please enter correct customer id')
        
        try:
            employee = Employee.objects.get(pk=employee_id)
        except Employee.DoesNotExist:
            raise serializers.ValidationError('Employee does not exist, please enter correct customer id')
        try:
            shipper = Shipper.objects.get(pk=shipper_id)
        except Shipper.DoesNotExist:
            raise serializers.ValidationError('Shipper does not exist, please enter correct customer id')

        order = Order(
            customer=customer,
            employee=employee,
            shipper=shipper
        )
        order.save()
        return order

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
