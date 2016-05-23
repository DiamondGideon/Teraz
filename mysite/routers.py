from mysite.viewSet import *
# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'usersprofiles', UserProfileViewSet)
router.register(r'users', UserViewSet)
router.register(r'posts',PostViewSet)
router.register(r'category',CategoryViewSet)
router.register(r'bet',BetViewSet)
router.register(r'bucket',BucketViewSet)