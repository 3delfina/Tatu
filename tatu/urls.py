from django.conf.urls import url
from tatu import views

#PAGES TO BE CREATED. 

#contact-us

#create-account


#login/profile/uploads
#login/profile/favourites
#artists
#artists/artist-page
#artists/artist-page/rate-this-artist


urlpatterns = [
    url(r'^$', views.index, name='index'),  # home page
    #url(r'^about/$', views.about, name='about'),
    url(r'^contact-us/$', views.contact, name='contact'),
    url(r'^faq/$', views.faq, name='faq'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^artists/$', views.artists, name='artists'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^tattoos/$', views.tattoos, name='tattoos'),
    url(r'^upload/$', views.user_post, name='upload'),
    url(r'^success/$', views.successView, name='success'),
    url(r'^test/$', views.submit_comment, name='test'),
    url(r'^tattoos/watercolour/$', views.watercolour, name='water'),
    url(r'^tattoos/traditional/$', views.traditional, name='tattoos'),
    url(r'^tattoos/realism/$', views.realism, name='tattoos'),
    url(r'^tattoos/tribal/$', views.tribal, name='tattoos'),
    url(r'^tattoos/dotwork/$', views.dotwork, name='tattoos'),
    url(r'^tattoos/geometric/$', views.geometric, name='tattoos'),
    url(r'^tattoos/japanese/$', views.japanese, name='tattoos'),
    url(r'^tattoos/lettering/$', views.lettering, name='tattoos'),
    url(r'^tattoos/blackwork/$', views.blackwork, name='tattoos'),

]
