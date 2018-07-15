def _get_class(qualified_name):
    from jnius import autoclass
    return autoclass(qualified_name)

def _get_platform_impl():
    return _get_class('com.sun.javafx.application.PlatformImpl')

def _get_jfx_util():
    return _get_class('org.janelia.saalfeldlab.fx.util.JFXUtil')

def _get_invoke_on_jfx_application_thread():
    return _get_class('org.janelia.saalfeldlab.fx.util.InvokeOnJavaFXApplicationThread')

def _get_scene():
    return _get_class('javafx.scene.Scene')

def _get_stage():
    return _get_class('javafx.stage.Stage')

def _get_platform():
    return _get_class('javafx.application.Platform')

def _get_runnable(func = lambda : None):
    from jnius import PythonJavaClass, java_method
    class _Runnable(PythonJavaClass):
        __javainterfaces__ = ['java/lang/Runnable']
        def __init__(self):
            super(_Runnable, self).__init__()

        @java_method('()V', name='run')
        def run(self):
            func()

    return _Runnable()

def init_platform():
    import jnius
    from jnius import autoclass
    _get_jfx_util().platformImplStartup()

def start_stage(root):
    print(1)
    r = _get_runnable(lambda : _start_stage(root))
    # r = _get_runnable(lambda : print("LOLOLOLOL"))
    # print(1.1)
    jfx_application_thread = _get_invoke_on_jfx_application_thread()
    # print(dir(jfx_application_thread))
    # print(1.2)
    # try:
    jfx_application_thread.invokeAndWait(r)
    # except Exception as e:
    #     print("WTF", e)
    #     raise e
    # print(1.3)

def _start_stage(root):
    print(2)
    scene = _get_scene()(root)
    print(3)
    stage = _get_stage()()
    print(4)
    stage.setScene(scene)
    print(5)
    stage.show()
    print(6)
    