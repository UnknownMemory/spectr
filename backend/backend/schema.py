import graphene
from graphene_django import DjangoObjectType

from user.models import User, Profile, Follow


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = "__all__"


class FollowType(DjangoObjectType):
    class Meta:
        model = Follow
        fields = "__all__"


class Query(graphene.ObjectType):
    user = graphene.Field(UserType, user_id=graphene.Int())
    profile = graphene.Field(UserType, user_id=graphene.Int())
    followings = graphene.Field(FollowType, user_id=graphene.Int())

    def resolve_user(root, info, user_id):
        return User.objects.get(id=user_id)

    def resolve_profile(root, info, user_id):
        return Profile.objects.get(id=user_id)

    def resolve_followings(root, info, user_id):
        return Profile.objects.get(user_id=user_id)


schema = graphene.Schema(query=Query)
