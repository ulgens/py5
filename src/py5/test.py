from pathlib import Path

from .sketch import Sketch


class RendererTest(Sketch):

    def __init__(self, renderer, renderer_name):
        super().__init__()
        self.renderer = renderer
        self.renderer_name = renderer_name

    def settings(self):
        self.size(150, 150, self.renderer)

    def setup(self):
        self.text_align(self.CENTER, self.CENTER)
        self.text_size(20)
        self.image_mode(self.CENTER)
        self.fill(24)

        self.logo = self.load_image(
            Path(__file__).parent.parent / "py5_tools/resources/logo-64x64.png"
        )

    def draw(self):
        self.background(240)
        self.image(self.logo, self.width / 2, 50)
        self.text("testing " + self.renderer_name, self.width / 2, 125)

        if self.frame_count == 60:
            self.exit_sketch()


def test_java2d():
    test = RendererTest(Sketch.JAVA2D, "JAVA2D")
    test.run_sketch()


def test_fx2d():
    test = RendererTest(Sketch.FX2D, "FX2D")
    test.run_sketch()


def test_p2d():
    test = RendererTest(Sketch.P2D, "P2D")
    test.run_sketch()


def test_p3d():
    test = RendererTest(Sketch.P3D, "P3D")
    test.run_sketch()


class TestInteractivity(Sketch):

    def __init__(self, renderer, renderer_name):
        super().__init__()
        self.renderer = renderer
        self.renderer_name = renderer_name

    def settings(self):
        self.size(250, 250, self.renderer)

    def setup(self):
        self.rect_mode(self.CENTER)

    def draw(self):
        self.rect(self.mouse_x, self.mouse_y, 10, 10)

    def key_pressed(self):
        self.println("key =", self.key)


def test_interactivity_java2d():
    test = TestInteractivity(Sketch.JAVA2D, "JAVA2D")
    test.run_sketch()


def test_interactivity_fx2d():
    test = TestInteractivity(Sketch.FX2D, "FX2D")
    test.run_sketch()


def test_interactivity_p2d():
    test = TestInteractivity(Sketch.P2D, "P2D")
    test.run_sketch()


def test_interactivity_p3d():
    test = TestInteractivity(Sketch.P3D, "P3D")
    test.run_sketch()
