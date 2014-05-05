import os
import sys
import json
import logging

import celery

from git import Git

from .exceptions import *

queue = celery.current_app

logger = logging.getLogger(__name__)


def begin_clone(node):
    logger.info('Being cloning of "{}"'.format(node.title))
    os.mkdir(node.title)
    os.chdir(node.title)

    with open('metadata.json', 'w+') as metadata:
        metadata.write(json.dumps(node['metadata']))

    clone_addons(node.addons)
    begin_clone(node.children)


def clone_addons(addons):
    for addon, blob in addons.items():
        clone_addon(addon, blob)


@queue.task(serializer='json')
def clone_addon(addon, data):
    cloner = _get_cloner(addon)
    if cloner:
        cloner(data)
    #Log error here


def _get_cloner(addon_name):
    self = sys.modules[__name__]
    return self.dict.get('_clone_{}'.format(addon_name))


def _clone_github(data):
    #Note: Use git init and git pull
    # git clone will copy the key to .git/config
    clone_url = 'https://{token}@github.com/{user}/{repo}.git'
    try:
        token = data['access_token']
        repo_name = 'github/{}'.format(data['repo'])
        user = data['user']
        url = clone_url(token=token, user=user, repo=repo)
        os.mkdir(repo_name)
        g = Git(repo_name)
        g.init()
        g.execute(['git', 'pull', url])
        logger.info('Finished cloning github addon for {}')
    except Exception:
        raise AddonCloningError('')