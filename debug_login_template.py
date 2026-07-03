import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LL_project.settings')
import django
django.setup()
from django.template.loader import render_to_string, get_template
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpRequest
req = HttpRequest()
req.user = None
for name in ['registration/login.html', 'Learning_Logs/base.html']:
    try:
        t = get_template(name)
        print('TEMPLATE', name, '=>', t.origin.name)
        print('SOURCE', getattr(getattr(t, 'template', None), 'source', None)[:300])
    except Exception as e:
        print('ERR', name, type(e).__name__, e)

html = render_to_string('registration/login.html', {'form': AuthenticationForm()}, request=req)
print('LEN', len(html))
print(repr(html))
