from django.contrib.auth.password_validation import validate_password
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User,Profile,Notification ,Bookmark ,Post,Comment,Category     



class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)  

        token['full_name'] = user.profile.full_name   
        token['username'] = user.username   
        token['email'] = user.email
        return token
    

class RegisterSerializer(serializers.ModelSerializer):   
    password = serializers.CharField(   
        write_only=True, 
        required=True, 
        validators=[validate_password]
    )   
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User 
        fields = ['email', 'full_name', 'password', 'password2']

    def validate(self, attrs):
        # Ensure that password and password2 match
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields do not match"})
        return attrs

    def create(self, validated_data):
        # Remove password2 as it's not needed beyond validation
        validated_data.pop('password2')

        email = validated_data.get('email')
        full_name = validated_data.get('full_name')
        password = validated_data.get('password')

        # Derive username from email
        try:
            email_username, domain = email.split("@")
        except ValueError:
            raise serializers.ValidationError({"email": "Invalid email format"})

        # Create the user
        user = User.objects.create(
            username=email_username,
            email=email,
            full_name=full_name  # Ensure your User model has a 'full_name' field
        )

        # Set the password using set_password to hash it
        user.set_password(password)
        user.save()

        return user
class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model=Profile  
        fields = "__all__"  


class CategorySerializer(serializers.ModelSerializer):
    def get_post_count(self,category):

        return category.post.count()

    class Meta: 
        model = Category
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model=Comment  
        fields = "__all__"  


    def __init__(self,*args,**kwargs):
        super(CommentSerializer,self).__init__(*args,**kwargs)
        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post  
        fields = "__all__"  


    def __init__(self,*args,**kwargs):
        super(PostSerializer,self).__init__(*args,**kwargs)
        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1  

class   BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model=Bookmark  
        fields = "__all__"  


    def __init__(self,*args,**kwargs):
        super(BookmarkSerializer,self).__init__(*args,**kwargs)
        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1 

class   NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=Notification  
        fields = "__all__"  


    def __init__(self,*args,**kwargs):
        super(NotificationSerializer,self).__init__(*args,**kwargs)
        request = self.context.get("request")
        if request and request.method == "POST":
            self.Meta.depth = 0
        else:
            self.Meta.depth = 1  


class  AuthorSerializer(serializers.Serializer):
    views = serializers.IntegerField(default=0)
    posts = serializers.IntegerField(default=0)
    likes = serializers.IntegerField(default=0)
    bookmarks = serializers.IntegerField(default=0)   




