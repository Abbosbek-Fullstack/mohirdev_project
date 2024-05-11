from django.urls import path
from django.contrib import admin
from .views import (news_list, news_detail, homePageView, ContactPageView,
                    HomePageView, localNewsView, foreignNewsView, technologyNewsView, SportNewsView,
                    NewsUpdateView, NewsDeleteView, NewsCreateView, admin_page_view,
                    SearchResultsList, TrendingNewsView, )

urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/', news_list, name='all_news_list'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),
    path('news/<slug:news>/', news_detail, name="news_detail_page"),
    path('news/<slug>/edit/', NewsUpdateView.as_view(), name='news_update'),
    path('news/<slug>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('local/', localNewsView.as_view(), name='local_news_page'),
    path('foreign/', foreignNewsView.as_view(), name='foreign_news_page'),
    path('technology/', technologyNewsView.as_view(), name='technology_news_page'),
    path('sport/', SportNewsView.as_view(), name='sport_news_page'),
    path('trend/', TrendingNewsView.as_view(), name='trending_news_page'),
    path('adminpage/', admin_page_view, name='admin_page'),
    path('searchresult/', SearchResultsList.as_view(), name='search_results'),
]