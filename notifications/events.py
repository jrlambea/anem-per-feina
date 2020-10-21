from .providers.telegram import Telegram
from .providers.twitter import Twitter
from .settings import IS_ENABLED
from .tasks import dispatch_event

EVENT_NEW_JOB = "new_job"

EVENTS = {
    EVENT_NEW_JOB: (Twitter.code, Telegram.code),
}

# Event decorator for be used in models
def event_dispatcher(event_name: str):
    def decorator(cls):
        def save(self, *args, **kwargs):
            is_new = not self.pk
            save._original(self, *args, **kwargs)
            if is_new and IS_ENABLED:
                dispatch_event.delay(event_name, self.__class__.__name__, self.pk)

        save._original = cls.save
        cls.save = save
        return cls

    return decorator
