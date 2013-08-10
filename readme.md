# Django-Mailwhimp

Django-Mailwhimp is a django application for interacting with MailChimp.

## Installation

    INSTALLED_APPS = (
        ...,
        'mailwhimp',
    )

## Usage

Add you app key to application in the admin and select "Load lists" from the
admin actions to refresh the lists from mailchimp.

The models arguments map onto the mailchimp API with the difference that a
campaign knows which list it belongs to so it takes care of some arguments.

Create a html campaign rendered from a template:

    mailchimp_list = List.objects.get(name='newsletter')
    content = render_to_string('newsletter/newsletter_detail.html', {
        'newsletter': newsletter
    })
    campaign = mailchimp_list.create_campaign(content={'html': content})

Test send:

    campaign.test_send(emails=[request.user.email])

Actual send:

    campaign.send()

# Contributing

Clone it and set it up editable in your env.

    make develop

Apply patches.

    make test

Watch tests pass, send pull request.