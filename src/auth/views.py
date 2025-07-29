from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.exceptions import TokenError

from src.auth.services import TokenService, UserService


class RegisterView(generics.CreateAPIView):
    def post(self, request: Request, *args, **kwargs):
        user_service = UserService()
        user = user_service.create_user(**request.data)

        token_service = TokenService()
        tokens = token_service.create_tokens(user)

        return Response(
            {
                "message": "User created successfully",
                "access_token": tokens.get("access"),
                "refresh_token": tokens.get("refresh"),
            },
            status=status.HTTP_201_CREATED,
        )


class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        token_service = TokenService()
        try:
            token_service.refresh_to_blacklist(request.data["refresh"])
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except KeyError:
            return Response(
                {"error": "Refresh token is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except TokenError:
            return Response(
                {"error": "Invalid or exceptas token"},
                status=status.HTTP_400_BAD_REQUEST,
            )
