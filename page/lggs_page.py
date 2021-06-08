from poium import Page, Element,Elements

class LggsPage(Page):
    #登录用例page元素
    loginUser_input=Element(xpath='/html/body/app-root/login-container/div/div[1]/form/div[1]/mat-form-field/div/div[1]/div/input',describe='登录用户名输入框')
    loginPasswd_input = Element(xpath='/html/body/app-root/login-container/div/div[1]/form/div[2]/mat-form-field/div/div[1]/div/input', describe='登录密码输入框')
    login_button=Element(xpath='/html/body/app-root/login-container/div/div[1]/form/div[3]/button[1]',describe='登录按钮')
    user_span=Element(xpath='/html/body/app-root/div[1]/tool-bar-container/mat-toolbar/nav/ul/button[2]/span',describe='用户名称')
    login_span=Element(xpath='/html/body/app-root/login-container/div/div[1]/div',describe='登录标题')
    logOut_button=Element(xpath='/html/body/div[2]/div[2]/div/div/div/button[2]',describe='退出登录按钮')

    #冷箱管理用例page元素
    empManage_span=Element(xpath='/html/body/app-root/div[2]/mat-sidenav-container/mat-sidenav/div/navigation-list-container/div/div[4]/div/mat-nav-list/div[1]/a/div/span',describe='冷箱管理菜单名称')
    inputEmp_button=Element(xpath='/html/body/app-root/div[2]/mat-sidenav-container/mat-sidenav-content/div/refrigerator-container/div/div[2]/div[1]/div[2]/button[1]/span',describe='录入冷箱按钮')
    clientId_input=Element(xpath='/html/body/app-root/div[2]/mat-sidenav-container/mat-sidenav-content/div/refrigerator-entry-container/div/div[2]/mat-form-field[1]/div/div[1]/div/input',describe='冷箱标识码输入框')
    empNum_select=Element(xpath='/html/body/app-root/div[2]/mat-sidenav-container/mat-sidenav-content/div/refrigerator-entry-container/div/div[2]/mat-form-field[2]/div/div[1]/div/mat-select',describe='冷箱型号下拉框')
    empNum_option=Element(xpath='/html/body/div[2]/div[2]/div/div/div/mat-option',describe='冷箱型号下拉选项')
    Bluetooth_input=Element(xpath='/html/body/app-root/div[2]/mat-sidenav-container/mat-sidenav-content/div/refrigerator-entry-container/div/div[2]/mat-form-field[3]/div/div[1]/div/input',describe='蓝牙输入框')
    calendar_button=Element(xpath='/html/body/app-root/div[2]/mat-sidenav-container/mat-sidenav-content/div/refrigerator-entry-container/div/div[2]/mat-form-field[4]/div/div[1]/div[2]/mat-datepicker-toggle/button',describe='日期控件按钮')
    calendar_select=Element(xpath='/html/body/div[2]/div[2]/div/mat-datepicker-content/mat-calendar/div/mat-month-view/table/tbody/tr[2]/td[2]/div[1]',describe='选择日期')
    productNum_input=Element(xpath='/html/body/app-root/div[2]/mat-sidenav-container/mat-sidenav-content/div/refrigerator-entry-container/div/div[2]/mat-form-field[5]/div/div[1]/div/input',describe='生产批号输入框')
    productHome_input=Element(xpath='/html/body/app-root/div[2]/mat-sidenav-container/mat-sidenav-content/div/refrigerator-entry-container/div/div[2]/mat-form-field[6]/div/div[1]/div/input',describe='生产厂家输入框')
    version_input=Element(xpath='/html/body/app-root/div[2]/mat-sidenav-container/mat-sidenav-content/div/refrigerator-entry-container/div/div[2]/mat-form-field[7]/div/div[1]/div/input',describe='固件版本输入框')
    yunyJg_select=Element(xpath='/html/body/app-root/div[2]/mat-sidenav-container/mat-sidenav-content/div/refrigerator-entry-container/div/div[2]/mat-form-field[8]/div/div[1]/div/mat-select',describe='所属运营机构选择')
    yunyJg_option=Element(xpath='/html/body/div[2]/div[2]/div/div/div/mat-option[16]',describe='下拉菜单选择 自动化测试运营机构 选项')
    addEmp_button=Element(xpath='/html/body/app-root/div[2]/mat-sidenav-container/mat-sidenav-content/div/refrigerator-entry-container/div/div[2]/div/button[1]',describe='录入冷箱按钮')
    emp_local=Element(xpath='/html/body/app-root/div[2]/mat-sidenav-container/mat-sidenav-content/div/refrigerator-container/div/div[2]/div[2]/table-component/div/table/tbody/tr[1]/td[2]',describe='冷箱录入后在冷箱列表冷箱码显示位置')