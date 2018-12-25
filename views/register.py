from urllib.parse import quote

import settings
from utils.backend import register_token
from views.base.api import APIView


class RegisterHandler(APIView):

    def get(self, *args, **kwargs):
        token, created = register_token()

        if not token:
            return

        url = '{}/projects/register/{}'.format(settings.WEB_BASE_URL, token.token)
        query_string = 'referrer={}'.format(quote(self.request.full_url().encode('utf8')))
        self.redirect('%s?%s' % (url, query_string))
