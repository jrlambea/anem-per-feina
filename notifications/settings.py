from django.conf import settings

PROJECT_NOTIFICATIONS = getattr(settings, "NOTIFICATIONS", {})

# The project notification settings is merged with the module settings.
# TODO: Add a settings example in readme
NOTIFICATIONS = {
    **{
        "telegram": {
            "enabled": False,
        },
        "twitter": {
            "enabled": False,
        },
    },
    **PROJECT_NOTIFICATIONS,
}

IS_ENABLED = any([provider["enabled"] for provider in NOTIFICATIONS.values()])
