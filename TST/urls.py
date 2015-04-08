from django.conf.urls import include, patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin
from TST.views import logout_page
from api import views


# urlpatterns = [  
#     #api
#     url(r'^webapi/v1/questions/$', views.QuestionCollection.as_view()),
#     url(r'^webapi/v1/questions/(?P<pk>[0-9]+)$', views.QuestionMember.as_view()),
# ]
# 
# urlpatterns = format_suffix_patterns(urlpatterns)
# 
# urlpatterns += [
#     # Examples:
#     # url(r'^$', 'TST.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
# 
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^$', 'api.views.home'),
#     url(r'^login/', 'django.contrib.auth.views.login'),
#     (r'^logout/$', logout_page),
# ]

# urlpatterns = patterns('',
#     #api
#     url(r'^webapi/v1/questions/$', views.QuestionCollection.as_view()),
#     url(r'^webapi/v1/questions/(?P<pk>[0-9]+)$', views.QuestionMember.as_view()),
#     url(r'^users/$', views.UserList.as_view()),
#     url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
#          
#     
# )
# urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns = format_suffix_patterns([
    url(r'^$', views.api_root),
    url(r'^webapi/v1/questions/$', views.QuestionCollection.as_view(), name='question-collection'),
    url(r'^webapi/v1/questions/(?P<pk>[0-9]+)$', views.QuestionMember.as_view(), name='question-member'),
    url(r'^users/$', views.UserList.as_view(),name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(),name='user-detail'),
    
    
])

urlpatterns += patterns('',
     # Examples:
     # url(r'^$', 'TST.views.home', name='home'),
     # url(r'^blog/', include('blog.urls')),
 
     url(r'^admin/', include(admin.site.urls)),
     
     url(r'^login/', include('rest_framework.urls', namespace='rest_framework')),
     (r'^logout/$', 'TST.views.logout_page'),


)