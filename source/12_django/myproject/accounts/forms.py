from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Profile

class SignupForm(UserCreationForm):
  phone_number = forms.CharField(label="전화", max_length=20,
                                help_text="전화번호는 필수입력이 아닙니다",
                                required=False)
  address      = forms.CharField(label="주소", max_length=100,
                                help_text="주소는 필수입력이 아닙니다",
                                required=False)
  class Meta(UserCreationForm.Meta):
    fields = UserCreationForm.Meta.fields + ('email',)

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['username'].help_text = "아이디(문자, 숫자, @.-_)를 입력하세요"
    self.fields['password1'].help_text = "2자 이상의 안전한 비밀번호를 입력하세요"
    self.fields['password2'].help_text = "동일한 비밀번호를 입력하세요"
    self.fields['email'].help_text = "이메일은 필수 입력이 아닙니다"

  def save(self, commit=True):
    user = super().save() # auth_user테이블에 저장(username, password)
    profile = Profile(user=user,
                      phone_number=self.cleaned_data.get("phone_number"),
                      address = self.cleaned_data.get("address")
              )
    profile.save() # accounts_profile 테이블에 저장(user_id, phone_number, address)
    return profile