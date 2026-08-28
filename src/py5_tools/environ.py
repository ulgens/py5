class Environment:
    def __init__(self):
        try:
            # be aware that __IPYTHON__ and get_ipython() are inserted into the
            # user namespace late in the kernel startup process
            __IPYTHON__  # type: ignore
            from ipykernel.zmqshell import ZMQInteractiveShell

            self.in_ipython_session = True
            self.ipython_shell = get_ipython()  # type: ignore
            self.in_jupyter_zmq_shell = isinstance(
                self.ipython_shell, ZMQInteractiveShell
            )
        except Exception:
            self.in_ipython_session = False
            self.ipython_shell = None
            self.in_jupyter_zmq_shell = False
