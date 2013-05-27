# Django-Mailwhimp

Django-Mailwhimp is a django application for interacting with MailChimp.

## Setup

    INSTALLED_APPS += ('slowstagram',)

    Then add your key and name to the
    Each application you want to use you'll need to setup in the django admin.

### Instagram Middleware

    MIDDLEWARE_CLASSES += ('slowstagram.middelware.InstagramApplicationMiddleware',)

The `instagram` middleware matches your request path with the Facebook
applications paths and loads that application. If there's more than one
application with the same path it will pick the most exact match (i.e. the
longest matching URL.) and set `instagram` on the `request`.

    def my_fancy_view(request):
        request.instagram.request('pancakes')
