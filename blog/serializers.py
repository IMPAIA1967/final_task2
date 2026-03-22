from datetime import date
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from blog.models import User, Post, Comment


# Валидатор пароля
def validate_password(value):
    if len(value) < 8:
        raise ValidationError("Пароль должен быть не менее 8 символов")
    if not any(char.isdigit() for char in value):
        raise ValidationError("Пароль должен содержать цифры")
    return value


# Валидатор email
def validate_email(value):
    allowed_domains = ['mail.ru', 'yandex.ru']
    domain = value.split('@')[-1]
    if domain not in allowed_domains:
        raise ValidationError("Разрешены только домены: mail.ru, yandex.ru")
    return value


# Валидатор возраста
def validate_author_age(value):
    if value.birth_date:
        today = date.today()
        age = today.year - value.birth_date.year
        if age < 18:
            raise ValidationError("Автор должен быть старше 18 лет")
    return value


# Валидатор запрещённых слов
def validate_forbidden_words(value):
    forbidden_words = ['ерунда', 'глупость', 'чепуха']
    for word in forbidden_words:
        if word in value.lower():
            raise ValidationError(f'Заголовок содержит запрещённое слово: {word}')
    return value


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    email = serializers.EmailField(validators=[validate_email])

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['id', 'date_joined', 'date_updated']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
