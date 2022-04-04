from django.shortcuts import redirect

from recipes_app.accounts.models import Profile


class RedirectToCreateProfile:
    def dispatch(self, request, *args, **kwargs):
        profiles = Profile.objects.all()
        profile = profiles.filter(user_id=request.user.id)
        if not profile:
            return redirect('create profile')
        return super().dispatch(request, *args, **kwargs)