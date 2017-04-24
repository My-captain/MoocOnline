# _*_ encoding:utf-8_*_
# __author__ = 'Mr.Robot'


# 导入正则表达式模块

import re

from django import forms

from operation.models import UserAsk


class UserAskForm(forms.ModelForm):
    """
    验证手机号码是否合法
    """
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    # Form作为表单验证,允许自定义验证函数,当调用is_valid()函数时,系统自动调用此函数
    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p =re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            # 若不合法应抛出异常,而非普通字符串
            raise forms.ValidationError(u"所填手机号是假的,被我检测出来了哈哈哈哈哈哈哈哈哈", code="mobile_invalid")