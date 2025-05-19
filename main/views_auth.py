from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
import json
from .serializers import UserProfileSerializer


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    data = json.loads(request.body)
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return Response({'error': 'Всі поля обовʼязкові'}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Користувач з таким логіном вже існує'}, status=400)

    user = User.objects.create_user(username=username, email=email, password=password)
    tokens = get_tokens_for_user(user)
    return Response({'message': 'Реєстрація успішна!', 'tokens': tokens}, status=201)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    user = User.objects.filter(username=username).first()
    if user and user.check_password(password):
        tokens = get_tokens_for_user(user)
        return Response({'message': 'Вхід успішний!', 'tokens': tokens}, status=200)
    return Response({'error': 'Невірний логін або пароль.'}, status=400)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user

    if request.method == 'GET':
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserProfileSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Профіль оновлено успішно!', 'profile': serializer.data})
        return Response(serializer.errors, status=400)