from lanxang.core.runtime import LanxangRuntime


class LanxangApplication:
    """
    Main Lanxang application container.
    """

    def __init__(self):

        self.runtime = LanxangRuntime()


application = LanxangApplication()
