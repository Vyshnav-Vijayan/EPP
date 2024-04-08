"""
URL configuration for EPP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),

    path('head/', views.head),
    path('tbl/', views.tbl),
    path('vmb/', views.vmb),

    path('admin_logout/', views.admin_logout),
    path('health_logout/', views.health_logout),
    path('police_logout/', views.police_logout),
    path('organization_logout/', views.organization_logout),

    path('home/', views.index),
    path('admin_home/', views.admin_home),
    path('admin_menu_bar/', views.admin_menu_bar),
    path('add_account/', views.add_account),
    path('add_account2/', views.add_account2),
    path('remove_account/', views.remove_account),
    path('remove_account2/<str:id1>', views.remove_account2),
    path('update_account/', views.update_account),
    path('update_account2/<str:id1>', views.update_account2),
    path('update_account3/<str:id1>', views.update_account3),
    path('add_notification/', views.add_notification),
    path('add_notification2/', views.add_notification2),
    path('remove_notification/', views.remove_notification),
    path('remove_notification2/<str:id1>', views.remove_notification2),
    path('add_organization/', views.add_organization),
    path('add_organization2/', views.add_organization2),
    path('remove_organization/', views.remove_organization),
    path('remove_organization2/<str:id1>', views.remove_organization2),
    path('update_organization/', views.update_organization),
    path('update_organization2/<str:id1>', views.update_organization2),
    path('update_organization3/<str:id1>', views.update_organization3),
    path('verify_organization/', views.verify_organization),
    path('acceptorg/<str:id>',views.acceptorg),
    path('rejectorg/<str:id>',views.rejectorg),
    path('view_complaint/', views.view_complaint),
    path('admin_report1/',views.admin_report1),
    path('admin_report2/',views.admin_report2),

    path('public_menu_bar/', views.public_menu_bar),
    path('public_add_organization/', views.public_add_organization),
    path('public_add_organization2/', views.public_add_organization2),
    path('public_view_organization/', views.public_view_organization),
    path('public_search_organization/', views.public_search_organization),
    path('public_search_organization2/', views.public_search_organization2),
    path('public_view_notification/', views.public_view_notification),
    path('public_add_complaint/', views.public_add_complaint),
    path('public_add_complaint2/', views.public_add_complaint2),
    path('public_login/', views.public_login),
    path('public_login2/', views.public_login2),

    path('organization_home/', views.organization_home),
    path('organization_menu_bar/', views.organization_menu_bar),
    path('organization_add_visitor/', views.organization_add_visitor),
    path('organization_add_visitor2/', views.organization_add_visitor2),
    path('organization_view_visitor/', views.organization_view_visitor),
    path('organization_view_visitor2/', views.organization_view_visitor2),

    path('health_home/',views.health_home),
    path('health_menu_bar/',views.health_menu_bar),
    path('health_add_notification/', views.health_add_notification),
    path('health_add_notification2/', views.health_add_notification2),
    path('health_remove_notification/', views.health_remove_notification),
    path('health_remove_notification2/<str:id1>', views.health_remove_notification2),
    path('health_add_test_campaign/', views.health_add_test_campaign),
    path('health_add_test_campaign2/', views.health_add_test_campaign2),
    path('health_remove_test_campaign/', views.health_remove_test_campaign),
    path('health_remove_test_campaign2/<str:id1>', views.health_remove_test_campaign2),
    path('health_update_test_campaign/', views.health_update_test_campaign),
    path('health_update_test_campaign2/<str:id1>', views.health_update_test_campaign2),
    path('health_update_test_campaign3/<str:id1>', views.health_update_test_campaign3),
    path('health_search_organization/', views.health_search_organization),
    path('health_search_organization2/', views.health_search_organization2),
    path('health_search_organization3/<str:id1>', views.health_search_organization3),
    path('health_search_organization4/', views.health_search_organization4),

    path('police_home/',views.police_home),
    path('police_menu_bar/',views.police_menu_bar),
    path('police_add_notification/', views.police_add_notification),
    path('police_add_notification2/', views.police_add_notification2),
    path('police_remove_notification/', views.police_remove_notification),
    path('police_remove_notification2/<str:id1>', views.police_remove_notification2),
    path('police_search_organization/', views.police_search_organization),
    path('police_search_organization2/', views.police_search_organization2),
    path('police_search_organization3/<str:id1>', views.police_search_organization3),
    path('police_search_organization4/', views.police_search_organization4),
    path('police_view_contact_list/', views.police_view_contact_list),

    path('contactlist/<str:id1>',views.contactlist),
    path('contactlist2/<str:id1>',views.contactlist2),
]
