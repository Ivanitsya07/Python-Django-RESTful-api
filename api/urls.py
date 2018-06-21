from django.urls import include, path, re_path
from api.resources import NoteResource

note_resource = NoteResource()

urlpatterns = [
    path('', include(note_resource.urls)),
    # path('user/', include(note_resource.urls)),
]