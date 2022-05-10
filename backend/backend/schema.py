import graphene
from graphene_django import DjangoObjectType

from user.models import User, Profile, Follow


# region User
class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = "__all__"


class CreateUser(graphene.Mutation):
    user = graphene.Field(UserType)

    class Arguments:
        first_name = graphene.String(required=True)
        last_name = graphene.String(required=True)
        username = graphene.String(required=True)
        email = graphene.String(required=True)
        password = graphene.String(required=True)

    @classmethod
    def mutate(cls, root, info, first_name, last_name, username, email, password):
        user = User(
            first_name=first_name,
            last_name=last_name,
            username=username,
            display_name=username,
            email=email,
        )

        user.set_password(password)
        user.save()

        Profile.objects.create(id=user)

        return CreateUser(user=user)


# endregion

# region Profile
class ProfileType(DjangoObjectType):
    class Meta:
        model = Profile
        fields = "__all__"


# endregion

# region Follow
class FollowType(DjangoObjectType):
    class Meta:
        model = Follow
        fields = "__all__"


# endregion


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


class Mutation(graphene.ObjectType):
    create_user = CreateUser.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
