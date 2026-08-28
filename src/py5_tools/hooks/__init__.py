from .frame_hooks import *

try:
    from .zmq_hooks import *
except:
    from .zmq_hooks_fail import *
