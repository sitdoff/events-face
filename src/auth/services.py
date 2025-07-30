from rest_framework_simplejwt.tokens import AccessToken, RefreshToken

from src.auth.serializer import RegisterSerializer


class UserService:
    """
    Сервис для работы с пользователями
    """

    serializer_class = RegisterSerializer

    def create_user(self, **kwargs):
        """
        Создаёт пользователя используя сериалайзер
        """
        serializer = self.serializer_class(data=kwargs)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return user


class TokenService:
    """
    Сервис для работы с токенами
    """

    @staticmethod
    def create_tokens(user) -> dict[str, str]:
        """
        Создаёт access и refresh токены для пользователя
        """
        refresh = TokenService.get_refresh_token(user)
        access = TokenService.get_access_token(user)
        return {"access": str(access), "refresh": str(refresh)}

    @staticmethod
    def get_refresh_token(user) -> RefreshToken:
        """
        Создаёт refresh токен
        """
        return RefreshToken.for_user(user)

    @staticmethod
    def get_access_token(user) -> AccessToken:
        """
        Создаёт access_token
        """
        return TokenService.get_refresh_token(user).access_token

    @staticmethod
    def refresh_to_blacklist(refresh_token: str) -> None:
        """
        Помещает refresh токен в черный список
        """
        token = RefreshToken(refresh_token)
        token.blacklist()
