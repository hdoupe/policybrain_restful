from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from taxbrainrest import views

urlpatterns = [
    url(r'^taxbrainrest/$', views.TaxBrainStaticModelInputList.as_view()),
    url(r'^taxbrainrest/(?P<pk>[0-9]+)/$', views.TaxBrainStaticModelInputDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
