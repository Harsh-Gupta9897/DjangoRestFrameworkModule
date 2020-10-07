from django.contrib.auth.models import Group
from rest_framework.permissions import BasePermission


def _is_in_group(user, group_name):
    """
    To check that the user is in that group or not
    """
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None


def _has_group_permission(user, required_groups):
    return any([_is_in_group(user,group_name) for group_name in required_groups])


class IsAdmin(BasePermission):
    """Is Admin according to the group permissions"""
    required_groups = ['admin']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission 

    

class IsTeacherorAdmin(BasePermission):
    """Is Teacher as well as Admin to these APIs"""
    required_groups = ['admin','teacher']

    def has_permission(self, request,view):
        has_group_permission = _has_group_permission(request.user,self.required_groups)
        return request.user and has_group_permission



class IsStudentorAdminorTeacher(BasePermission):
    """
    class for access at student level
    """


    required_groups = ['admin','teacher','student']

    def has_permission(self, request, view):
        has_group_permission = _has_group_permission(request.user, self.required_groups)
        return request.user and has_group_permission

    
class AllowAny(BasePermission):
    """
    Allow any access.
    This isn't strictly required, since you could use an empty
    permission_classes list, but it's useful because it makes the intention
    more explicit.
    """

    def has_permission(self, request, view):
        
        return True





    

        


