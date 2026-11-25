from collections import defaultdict

from lanxang.events.event import LanxangEvent


class EventBus:
    """
    Publish/subscribe event bus.
    """

    def __init__(self):

        self._subscribers = defaultdict(list)


    def subscribe(
        self,
        event_type,
        callback
    ):

        self._subscribers[event_type].append(
            callback
        )


    def publish(
        self,
        event: LanxangEvent
    ):

        listeners = (
            self._subscribers.get(
                event.event_type,
                []
            )
            +
            self._subscribers.get(
                "*",
                []
            )
        )

        for callback in listeners:

            callback(event)
