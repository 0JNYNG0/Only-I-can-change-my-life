from django.forms import ModelForm

from profileapp.models import Profile


# ModelForm 은 Model 을 그대로 Form 으로 바꿔줄 수 있는 기능
# Account 와 같은 중요한 정보는 Django 에서 Form 을 제공해 주지만
# Profile 등 정보는 따로 제공 해주지 않고, 코드를 모두 작성 하기 양이 많기 때문에
# ModelForm 이라는 것을 사용해 만들 수 있다
class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message']
