from .default import *  # noqa


INSTALLED_APPS += [
    'debug_toolbar',
    'django_extensions',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    *MIDDLEWARE,
]

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'cachalot.panels.CachalotPanel',
]

# TEMPLATES[0]['OPTIONS']['debug'] = False

AUTH_PASSWORD_VALIDATORS = list()
