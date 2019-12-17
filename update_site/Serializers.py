from rest_framework import serializers
from models import Blog

class Update_SiteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Blog
        fields =('category','title','content','date','image')
