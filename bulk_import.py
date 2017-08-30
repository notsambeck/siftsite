import os
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'siftsite.settings')
django.setup()

from labeller.models import Image


def import_all_images(label, source, directory='.'):
    '''import whole directory;
    label=1 for images; label=0 for simulations
    ex: for batch of cifar images:
    from directory:
    >>> import_all_images(1, 'cifar')
    None
    '''
    all_files = os.listdir(directory)
    input('warning; will import up to {} files.'.format(len(all_files)))
    for f in all_files:
        if f[-4:] == '.png':
            im = Image(filename=f, source=source, correct_label=label)
            im.save()
