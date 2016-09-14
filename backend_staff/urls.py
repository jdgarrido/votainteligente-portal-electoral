
from django.conf.urls import patterns, url
from backend_staff.views import (
    IndexView,
    PopularProposalCommentsView,
    ModeratePopularProposalView,
    AcceptPopularProposalView,
    RejectPopularProposalView,
    AddContactAndSendMailView,
    AllCommitmentsView,
)

urlpatterns = patterns('',
    url(r'^$',
        IndexView.as_view(),
        name='index'),
    url(r'^popular_proposal_comments/(?P<pk>[-\w]+)/?$',
        PopularProposalCommentsView.as_view(),
        name='popular_proposal_comments'),
    url(r'^moderate_popular_proposal/(?P<pk>[-\w]+)/?$',
        ModeratePopularProposalView.as_view(),
        name='moderate_proposal'),
    url(r'^accept_popular_proposal/(?P<pk>[-\w]+)/?$',
        AcceptPopularProposalView.as_view(),
        name='accept_proposal'),
    url(r'^reject_popular_proposal/(?P<pk>[-\w]+)/?$',
        RejectPopularProposalView.as_view(),
        name='reject_proposal'),
    url(r'^add_contact_and_sen_mail/(?P<pk>[-\w]+)/?$',
        AddContactAndSendMailView.as_view(),
        name='add_contact_and_send_mail'),
    url(r'^all_commitments/?$',
        AllCommitmentsView.as_view(),
        name='all_commitments'),
    
)
