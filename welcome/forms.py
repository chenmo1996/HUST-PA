from django import forms
from django.utils.translation import ugettext_lazy

from .models import Group1,Group2,Room

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Field, ButtonHolder, Submit
from crispy_forms.bootstrap import Tab, TabHolder, AppendedText, InlineRadios
from captcha.fields import CaptchaField


class WelcomeForm(forms.Form):
    name = forms.CharField(
        label='姓名',
        required=True,
        max_length=16,
    )

    sex = forms.ChoiceField(
        choices=((1, '男'), (0, '女'),(2,'其他')),
        label='性别',
        required=True,
    )

    tel = forms.CharField(
        label='手机号码',
        required=True,
        max_length=11,
    )

    email = forms.CharField(
        label='qq或者微信',
        required=False,
        max_length=64,
    )

    college = forms.CharField(
        label='专业-年级',
        required=True,
        max_length=64,
    )
    dormitory = forms.ChoiceField(
        choices=(('韵苑', '韵苑'), ('沁苑', '沁苑'),('紫菘','紫菘')),
        label='寝室住址',
        required=True,
    )
    group1 = forms.ModelChoiceField(
        label='报名哪次活动（如果两个活动都报请分别报名）',
        queryset=Group1.objects.all(),
        empty_label=None,
        required=True,
    )
    group2 = forms.ModelChoiceField(
        label='报名项目',
        queryset=Group2.objects.all(),
        empty_label=None,
        required=True,
    )
    room = forms.ModelChoiceField(
        label='是否摄协成员（也欢迎非摄协成员来玩）',
        queryset=Room.objects.all(),
        empty_label=None,
        required=True,
    )
    introduction = forms.CharField(
        label='报名信息',
        widget=forms.Textarea(),
        required=True,
        max_length=2000,
    )
    captcha = CaptchaField(
        label='验证码',
        required=True,
    )

    def __init__(self, *args, **kwargs):
        super(WelcomeForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.field_class = 'form-horizontal'
        self.helper.form_method = 'post'
        self.helper.form_id = 'welcome_form'
        self.helper.attrs = {'onsubmit': 'disable_button()'}
        self.helper.layout = Layout(
            Fieldset(
                '请填写以下表格',
                TabHolder(
                    Tab(
                        '报名信息',
                        AppendedText('name', '''<span class="glyphicon glyphicon-user"></span>''',
                                     placeholder='填写你的姓名'),
                        InlineRadios('sex'),
                        AppendedText('tel', '''<span class="glyphicon glyphicon-phone"></span>''',
                                     placeholder='填写你的手机号码'),
                        AppendedText('email', '''<span class="glyphicon glyphicon-envelope"></span>''',
                                     placeholder='选填，请输入qq或者微信号'),
                        AppendedText('college', '''<span class="glyphicon glyphicon-book"></span>''',
                                     placeholder='“专业 年级数字”，如“软件工程15”'),
                        InlineRadios('dormitory'),
                        InlineRadios('group1'),
                        InlineRadios('group2'),
                        InlineRadios('room'),
                        Field('introduction', placeholder='摄影师:说说你的拍摄水平拍摄风格以及拍摄要求。/模特:说说你对摄影师的要求，以及希望的风格，希望拍摄的地点，以及对摄影协会的要求。'),
                        Field('captcha'),
                    )
                ),
            ),
            ButtonHolder(
                Submit('submit', '提交', css_class='button white'),
            ),
        )
        if 'error_messages' not in kwargs:
            kwargs['error_messages'] = {}
        kwargs['error_messages'].update({'required': ugettext_lazy('不能为空哦~')})

    def clean_name(self):
        name = self.cleaned_data['name']
        for char in name:
            if char < u'\u4e00' or char > u'\u9fa5':
                raise forms.ValidationError('我读书少，这不是中文吧……')
        return name

    def clean_tel(self):
        tel = self.cleaned_data['tel']
        try:
            int(tel)
        except ValueError:
            raise forms.ValidationError('你确定这是手机号……')
        if len(tel) != 11:
            raise forms.ValidationError('手机号码应该是11位吧……')
        else:
            return tel

    # def clean_college(self):
    #     college = self.cleaned_data['college']
    #     try:
    #         major, grade = college.split('-')
    #     except ValueError:
    #         pass
    #     if grade not in ('14', '15', '16'):
    #         return college
    #     else:
    #         return college

    # def clean_dormitory(self):
    #     dormitory = self.cleaned_data['dormitory']
    #     try:
    #         dor, house, code = dormitory.split('-')
    #     except ValueError:
    #         raise forms.ValidationError('你的格式没填对吧?')
    #     try:
    #         int(house)
    #         int(code)
    #     except ValueError:
    #         raise forms.ValidationError('按照格式填咯，注意宿舍楼和寝室号要求是纯数字哦')
    #     return dormitory
