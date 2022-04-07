from django.shortcuts import redirect

from recipes_app.accounts.models import Profile


class RedirectToCreateProfile:
    def dispatch(self, request, *args, **kwargs):
        profile = Profile.objects.filter(user_id=request.user.id)
        if not profile and not request.user.is_superuser:
            return redirect('create profile')
        return super().dispatch(request, *args, **kwargs)