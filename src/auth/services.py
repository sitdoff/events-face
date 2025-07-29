from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from src.auth.serializer import RegisterSerializer


class UserService:
    serializer_class = RegisterSerializer

    def create_user(self, **kwargs):
        serializer = self.serializer_class(data=kwargs)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return user


class TokenService:
    @staticmethod
    def create_tokens(user) -> dict[str, str]:
        refresh = TokenService.get_refresh_token(user)
        access = TokenService.get_access_token(user)
        return {"access": str(access), "refresh": str(refresh)}

    @staticmethod
    def get_refresh_token(user) -> RefreshToken:
        return RefreshToken.for_user(user)

    @staticmethod
    def get_access_token(user) -> AccessToken:
        return TokenService.get_refresh_token(user).access_token
