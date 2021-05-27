from django.shortcuts import render
from django.views import static

# Globals:
from SkyrimDB.settings import BASE_DIR
HTML_ROOT = BASE_DIR / 'static'


def serve(request, path='index.html'):
    return static.serve(request, path, document_root=HTML_ROOT)