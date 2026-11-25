from lanxang.core.context import LanxangContext
from lanxang.config import load_config
from lanxang.events import EventBus
from lanxang.intelligence.context import LanxangEnvironmentContext
from lanxang.listeners import DatabaseListener


class LanxangRuntime:
    """
    Central runtime object.
    """

    def __init__(self):

        self.context = LanxangContext()

        self.context.config = (
            load_config().model_dump()
        )

        self.environment = LanxangEnvironmentContext()

        self.events = EventBus()

        DatabaseListener().register(self.events)


    def get_context(self):

        return self.context


    def get_environment(self):

        return self.environment
