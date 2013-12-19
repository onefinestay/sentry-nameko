from django.utils.translation import ugettext as _
from sentry.interfaces import Interface
from sentry.web.helpers import render_to_string


class CallIdStack(Interface):
    attrs = ('call_id_stack',)

    def __init__(self, call_id_stack=None, **kwargs):
        self.call_id_stack = call_id_stack

    def serialize(self):
        return {
            'call_id_stack': self.call_id_stack
        }

    def get_hash(self):
        return []

    def get_search_context(self, event):
        if not self.call_id_stack:
            return {}
        return {
            'text': self.call_id_stack
        }

    def to_html(self, event, is_public=False, **kwargs):
        return render_to_string('sentry_nameko/call_id_stack.html', {
            'is_public': is_public,
            'event': event,
            'call_id_stack': self.call_id_stack
        })

    def get_slug(self):
        return 'call_id_stack'

    def get_title(self):
        return _('Call ID Stack')
