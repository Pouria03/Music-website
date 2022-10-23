from rest_framework.permissions import BasePermission
from accounts.models import User
# 
class IsProUser(BasePermission):
    message = 'you are not a pro user!'
    def has_permission(self,request,view):
        user = request.user
        pro_users = User.objects.filter(groups__name='premium_users')
        if user in pro_users :
            return True
        else:
            return False

