from django.shortcuts import render, redirect
from .models import User, OrderManage, Store
from .forms import UserForm, RegisterForm, OrderForm
import hashlib

# Create your views here.
'''首页展示'''
def index(request):
    pass

    return render(request, 'index.html')

'''订单展示'''
def show(request):
    user = request.session.get('user_name')
    orders = OrderManage.objects.filter(author__exact=user).all()
    for order in orders:
        pass
    return render(request, 'show.html',locals())

'''订单添加'''
def add(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        message = "请检查输入内容"
        if order_form.is_valid():
            name = Store.objects.filter(id=order_form.cleaned_data['name']).all()[0]
            num = order_form.cleaned_data['num']
            price = order_form.cleaned_data['price']
            c_time = request.POST.get('time')
            customer = order_form.cleaned_data['customer_ser']
            author = order_form.cleaned_data['author']
            detail = order_form.cleaned_data['detail']
            status = order_form.cleaned_data['status']
            # print(status)   #状态显示还是数字
        else:
            return render(request, 'add.html', locals())
        same_num_user = OrderManage.objects.filter(order_num=num)
        if same_num_user:
            message = "该订单号已经存在"
            return render(request, 'add.html', locals())
        # if request.session.user_name != author:
        #         #     message = "请核对作者"
        #         #     return render(request, 'add.html', locals())
        new_order = OrderManage()
        new_order.store_name = name
        new_order.order_num = num
        new_order.price = price
        new_order.customer_ser = customer
        new_order.author = author
        new_order.c_time = c_time
        new_order.o_detail = detail
        new_order.status = status
        new_order.save()
        return render(request, 'show.html', locals())
    order_form = OrderForm()
    return render(request, 'add.html', locals())



'''订单修改'''
def modify(request, order_id):
    user = request.session.get('user_name')
    try:
        order = OrderManage.objects.filter(id=order_id).all()[0]
        if user != order.author:
            message = "请勿修改他人订单"
            return redirect("/index/show")
    except:
        message = "订单不存在"
        return redirect('/index/show')
    order_form = OrderForm()
    if request.method == "POST":
        order.e_time = request.POST.get('e_time')
        if request.POST.get('status_name') == "制作":
            order.status = 0
        elif request.POST.get('status_name') == "测试":
            order.status = 1
        elif request.POST.get('status_name') == "退单":
            order.status = 2
        elif request.POST.get('status_name') == "完成":
            order.status = 3
        order.save()
        return redirect('/index/show')
    return render(request, 'modify.html',locals() )


'''登陆功能'''
def login(request):
    if request.session.get('is_login', None):      #禁止重复登陆
        return redirect('/index/')
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写内容"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']      # 验证成功后可以从表单对象的cleaned_data数据字典中获取表单的具体值
            password = login_form.cleaned_data['password']
        else:
            return render(request, "login.html", locals())
        try:
            user = User.objects.get(name=username)
            if user.password == hash_code(password):              # 哈希值和数据库内的值进行比对
                if user.statu == "activation":
                    request.session['is_login'] = True
                    request.session['user_id'] = user.id
                    request.session['user_name'] = user.name
                    return redirect('/index/')
                else:
                    message = "该账户尚未激活"
                return render(request, "login.html", locals())
            else:
                message = "密码不正确"
        except:
            message = "用户不存在"
        return render(request, "login.html", locals())
    login_form = UserForm()               # 对于非POST方法发送数据时，比如GET方法请求页面，返回空的表单，让用户可以填入数据；
    return render(request, "login.html", locals())      # locals()函数，它返回当前所有的本地变量字典

'''注册功能'''
def register(request):
    if request.session.get('is_login', None):
        return redirect('/index/')
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查输入的内容！"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            confirm_pwd = register_form.cleaned_data['confirm_pwd']
            email = register_form.cleaned_data['email']
        else:
            return render(request, 'register.html', locals())
        if password != confirm_pwd:
            message = "两次密码输入不一致！"
            return render(request, 'register.html', locals())
        same_email_user = User.objects.filter(email=email)
        if same_email_user:
            message = "该邮箱已被注册！"
            return render(request, 'register.html', locals())
        new_user = User()
        new_user.name = username
        new_user.password = hash_code(confirm_pwd)      #使用加密密码
        new_user.email = email
        new_user.save()
        return redirect('/login/')
    register_form = RegisterForm()
    return render(request, 'register.html', locals())

'''退出功能'''
def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/index/')
    request.session.flush()
    return redirect("/index/")

'''密码加密'''
def hash_code(s, salt='mysite'):        #加盐
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())            # update方法只接收bytes类型
    return h.hexdigest()


def login_ome(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        err_message = "账户和密码不得为空"
        if username and password:           # 账户密码都不为空
            username = username.strip()     # 通过strip()方法，将用户名前后无效的空格剪除
            try:                            # 使用try异常机制，防止数据库查询失败的异常；
                user = User.objects.get(name=username)
                if user.password == password:
                    return redirect('/index/')
                else:
                    err_message = "密码错误"
            except:
                err_message = "用户名不存在"
        return render(request, "login_1.html", {"message": err_message})
    return render(request, 'login_1.html')