import graphene
from graphene_django import DjangoObjectType

from user.models import User, Profile, Follow


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = (
            "id",
            "first_name",
            "last_name",
            "username",
            "email",
            "password",
            "display_name",
            "country",
            "is_superuser",
            "is_staff",
            "is_active",
            "date_joined",
        )


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = ("id", "bio", "url", "picture")


class FollowType(DjangoObjectType):
    class Meta:
        model = Follow
        fields = ("id", "user_id", "follower_id", "followed_at")


class Query(graphene.ObjectType):
    allUsers = graphene.List(UserType)
    allFollow = graphene.List(ProfileType)

    def resolve_all_users(root, info):
        return User.objects.all()


schema = graphene.Schema(query=Query)
