from django import template
from django.core.cache import cache
from templatetag_sugar.parser import Optional, Constant, Name, Variable
from templatetag_sugar.register import tag
import tumblr

def get_cache_key(*args):
    return 'get_tweets_%s' % ('_'.join([str(arg) for arg in args if arg]))

def get_tumblr_api(tumblrname):
    url = 'http://%s.tumblr.com/api/read' % tumblrname
    cache_key = get_cache_key(tumblrname, limit)
    
    t = cache.get(cache_key, False)
    if not t:
        t = tumblr.parse(url)
        cache.set(cache_key, t)
    return t

@tag(register, [Constant("for"), Variable(), Constant("as"), Name(),
                Optional([Constant("limit"), Variable("limit")])])
def get_tumblr_posts(context, tumblrname, limit=None):
    t = get_tumblr_api(tumblrname)
    if limit:
        t = t[0:limit]
    try:
        return t.posts
    except:
        return []