from django.urls import path
from todolist.views import *

app_name = 'todolist'

urlpatterns = [
    path("", show_todolist, name="show_todolist"),
    path("register/", register, name="register"),
    path("login/", login_user, name="login"),
    path("logout/", logout_user, name="logout"),
    path("create_todolist/", create_todolist, name="create_todolist"),
    path("delete_todolist/<int:id>", delete_todolist, name="delete_todolist"),
    path("update_todolist/<int:id>", update_todolist, name="update_todolist"),
    path("json/", get_todo_json, name="get_todo_json"),
    path("add/", add_todo_json, name="add_todo_json"),
]