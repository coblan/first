<<<<<<< HEAD
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    import gevent
    from gevent import monkey
    monkey.patch_all()   
    
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
=======
#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
>>>>>>> bed9c449cb869d6caf8eff06ea7143c7f1aab9af
