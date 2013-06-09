from django.db import models, IntegrityError
from mailsnake import MailSnake


class Application(models.Model):
    label = models.CharField(max_length=100)
    key = models.CharField(max_length=36)

    def request(self, command, **kwargs):
        ms = MailSnake(self.key)
        try:
            return getattr(ms, command)(**kwargs)
        except AttributeError:
            raise ValueError("That's not a valid mailchimp command")

    def load_campaigns(self, filters=None):
        if not filters:
            filters = {}
        response = self.request('campaigns', filters=filters)
        for campaign_data in response['data']:
            # @todo could do a single bulk create if we filter out existing
            # ones.
            try:
                Campaign.objects.create(
                    list_id=campaign_data['list_id'],
                    id=campaign_data['id'],
                    title=campaign_data['title'],
                    create_time=campaign_data['create_time'],
                    send_time=campaign_data['send_time']
                )
            except IntegrityError:
                pass

    def load_lists(self):
        response = self.request('lists')
        for mail_list in response['data']:
            try:
                self.list_set.create(
                    id=mail_list['id'],
                    name=mail_list['name'],
                    default_from_name=mail_list['default_from_name'],
                    default_from_email=mail_list['default_from_email'],
                    default_subject=mail_list['default_subject'],
                )
            except IntegrityError:
                pass


    def __unicode__(self):
        return self.label


class List(models.Model):
    application = models.ForeignKey(Application)
    id = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=100)
    default_from_name = models.CharField(max_length=100)
    default_from_email = models.EmailField()
    default_subject = models.CharField(max_length=100)

    def load_campaigns(self, filters=None):
        filters = dict((filters or {}), list_id= self.id)
        self.application.load_campaigns(filters)

    def subscribe(self, email, merge_vars=None, email_type='html',
                  double_optin=True, update_existing=False,
                  replace_interests=True, send_welcome=False):
        self.application.request('listSubscribe',
                                 email_address=email,
                                 id=self.pk,
                                 merge_vars=merge_vars,
                                 email_type=email_type,
                                 double_optin=double_optin,
                                 update_existing=update_existing,
                                 replace_interests=replace_interests,
                                 send_welcome=send_welcome)

    def create_campaign(self, content, options=None, campaign_type='regular'):
        """ Setup a remote campaign, returns a Campaign model. """
        options = dict({'subject': self.default_subject,
                        'from_email': self.default_from_email,
                        'from_name': self.default_from_name}, **(options or {}))

        if not content:
            raise ValueError
        send_options = dict({'list_id': self.pk}, **options)
        campaign_id = self.application.request('campaignCreate',
                                               type=campaign_type,
                                               options=send_options,
                                               content=content)
        # We could skip loading the campaign from mailchimp since we should have
        # all the data. However it's easier to just push data to mailchimp and
        # then load back how mailchimp sees it, rather than attempting to
        # match it on our end by parsing send_options.
        self.application.load_campaigns(filters={'campaign_id': campaign_id})
        return Campaign.objects.get(pk=campaign_id)

    def __unicode__(self):
        return self.name


class Campaign(models.Model):
    list = models.ForeignKey(List)
    id = models.CharField(max_length=30, primary_key=True)
    title = models.CharField(max_length=200)
    create_time = models.DateTimeField()
    send_time = models.DateTimeField(blank=True, null=True)

    def test_send(self, emails):
        application = self.list.application
        print application.request('campaignSendTest',
                                  cid=self.pk,
                                  test_emails=emails)

    def __unicode__(self):
        return self.title