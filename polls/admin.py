from django.contrib import admin
from models import PollSubject, Poll, Vote

admin.site.register(PollSubject)
admin.site.register(Poll)
admin.site.register(Vote)