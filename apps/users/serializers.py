from rest_framework import serializers
from django.contrib.auth import get_user_model

from apps.users.models import UserContact, WorkExperience, Education, Skills, Premium
from apps.posts.serializer import PostSerializer, PostFavoritesSerializer


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'last_login', 'username',
                'first_name', 'last_name', 'email',
                'date_joined', 'profile_image', 'is_premium')

class PremiumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premium
        fields = ('id', 'user', 'start', 'end')

class WorkExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkExperience
        fields = ('user', 'name', 'type_of_employment',
                    'name_company', 'location', 'job_type',
                    'date_start', 'date_end', 'description')

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Education
        fields = ('user', 'educational_institution', 'degree',
        'specialization', 'date_start', 'date_end')

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ('user', 'skill', )

class UserDetailSerializer(serializers.ModelSerializer):
    #posts - посты пользователя
    users_post = PostSerializer(read_only=True, many=True)
    count_posts = serializers.SerializerMethodField(read_only=True)
    #favorites - избранные пользователя
    favorites = PostFavoritesSerializer(read_only=True, many=True)
    count_favorites = serializers.SerializerMethodField(read_only=True)
    #work_experience - опыт работы
    users_work_experience = WorkExperienceSerializer(read_only=True, many=True)
    #education - образование
    users_education = EducationSerializer(read_only=True, many=True)
    #skills - навыки
    users_skill = SkillsSerializer(read_only=True, many=True)

    class Meta:
        model = User 
        fields = ('id', 'last_login', 'username',
                'first_name', 'last_name', 'email',
                'date_joined', 'profile_image', 'is_premium',
                'users_post', 'count_posts', 'favorites', 
                'count_favorites', 'users_work_experience',
                'users_education', 'users_skill'
                )

    def get_count_posts(self, instance):
        return instance.users_post.all().count()

    def get_count_favorites(self, instance):
        return instance.favorites.all().count()

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 
                    'email','profile_image', 'is_premium')

class UserContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserContact
        fields = ('from_user', 'to_user', 'is_contact')

    def validate(self, attrs):
        if attrs['from_user'] == attrs['to_user']:
            raise serializers.ValidationError({"error": "Нельзя в контакты самому себе"})
        return attrs

class UserRegisterSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        max_length=255, write_only=True
    )
    email = serializers.CharField(
        max_length=255, write_only=True
    )
    phone_number = serializers.CharField(
        max_length=255, write_only=True
    )
    age = serializers.IntegerField(
        write_only=True
    )
    password = serializers.CharField(
        max_length=255, write_only=True
    )
    password2 = serializers.CharField(
        max_length=255, write_only=True
    )

    class Meta:
        model = User 
        fields = ('username', 'email', 'phone_number', 'age', 'user_or_organization', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Пароли отличаются"})
        if '+996' not in attrs['phone_number']:
            raise serializers.ValidationError({"phone_number": "Напишите номер с +996"})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            user_or_organization=validated_data['user_or_organization']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ChangePasswordSerializer(serializers.Serializer):
    model = User

    old_password = serializers.CharField(
        max_length=255, required=True
    )
    new_password = serializers.CharField(
        max_length=255, required=True
    )