from poium import Page, Element,Elements

class LggsPage(Page):
    loginUser_input=Element(xpath='/html/body/app-root/login-container/div/div[1]/form/div[1]/mat-form-field/div/div[1]/div/input',describe='登录用户名输入框')
    loginPasswd_input = Element(xpath='/html/body/app-root/login-container/div/div[1]/form/div[2]/mat-form-field/div/div[1]/div/input', describe='登录密码输入框')
    login_button=Element(xpath='/html/body/app-root/login-container/div/div[1]/form/div[3]/button[1]',describe='登录按钮')
    user_span=Element(xpath='/html/body/app-root/div[1]/tool-bar-container/mat-toolbar/nav/ul/button[2]/span',describe='用户名称')
    login_span=Element(xpath='/html/body/app-root/login-container/div/div[1]/div',describe='登录标题')
    logOut_button=Element(xpath='/html/body/div[2]/div[2]/div/div/div/button[2]',describe='退出登录按钮')
