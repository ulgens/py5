import sys

from . import environ as _environ


class _DefaultPrintlnStream:
    def __init__(self):
        pass

    def print(self, text, end="\n", stderr=False, flush=False):
        print(text, end=end, file=sys.stderr if stderr else sys.stdout, flush=flush)

    def shutdown(self):
        pass


class _DisplayPubPrintlnStream:
    def __init__(self):
        try:
            self.display_pub = _environ.Environment().ipython_shell.display_pub
            self.parent_header = self.display_pub.parent_header
        except:
            self.display_pub = None
            self.parent_header = None

    def print(self, text, end="\n", stderr=False, flush=False):
        if self.display_pub is None or self.parent_header is None:
            print(text, end=end, file=sys.stderr if stderr else sys.stdout, flush=flush)
        else:
            content = dict(name="stderr" if stderr else "stdout", text=text + end)
            msg = self.display_pub.session.msg(
                "stream", content, parent=self.parent_header
            )
            self.display_pub.session.send(
                self.display_pub.pub_socket, msg, ident=b"stream"
            )

    def shutdown(self):
        pass


class _WidgetPrintlnStream:
    def __init__(self):
        try:
            import ipywidgets as widgets
            from IPython.display import display

            self.out = widgets.Output(layout=dict(max_height="200px", overflow="auto"))
            display(self.out)
        except:
            self.out = None

    def print(self, text, end="\n", stderr=False, flush=False):
        if self.out is None:
            print(text, end=end, file=sys.stderr if stderr else sys.stdout, flush=flush)
        else:
            if stderr:
                self.out.append_stderr(text + end)
            else:
                self.out.append_stdout(text + end)

    def shutdown(self):
        pass


class _PrintlnFileStream:

    def __init__(self, filename):
        self.filename = filename
        self.f = None

    def print(self, text, end="\n", stderr=False, flush=False):
        if self.f is None:
            self.f = open(self.filename, "w")

        print(text, end=end, file=self.f, flush=flush)

    def shutdown(self):
        if self.f is not None:
            self.f.close()
