from django.http import Http404


# from django.shortcuts import render, get_object_or_404, redirect

class AdminAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("شما اجازه دسترسی به صفحه را ندارید")
