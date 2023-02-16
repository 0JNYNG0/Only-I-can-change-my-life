from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile


# Create your views here.


class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/create.html'

    # form 변수에 우리가 입력한 fields 값들이 들어 있다(fields 는 forms.py에 정의 되어 있음)
    def form_valid(self, form):
        temp_profile = form.save(commit=False)  # 임시 저장된 정보
        # commit=False 를 넣어 실제로 form.save() 저장 하지 않고 변수에 잠시 저장 해둔다.
        temp_profile.user = self.request.user  # 누락된 정보 user 를 프로필 정보에 넣어 준다
        temp_profile.save()  # 여기서 최종적으로 해당 프로필 정보를 save 저장 한다
        return super().form_valid(form)


@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')
class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'profileapp/update.html'
