

class Intents:
    GUILDS = (1 << 0)
    GUILD_MEMBERS = (1 << 1)
    GUILD_BANS = (1 << 2)
    GUILD_EMOJIS_AND_STICKERS = (1 << 3)
    GUILD_INTEGRATIONS = (1 << 4)
    GUILD_WEBHOOKS = (1 << 5)
    GUILD_INVITES = (1 << 6)
    GUILD_VOICE_STATES = (1 << 7)
    GUILD_PRESENCES = (1 << 8)
    GUILD_MESSAGES = (1 << 9)
    GUILD_MESSAGE_REACTIONS = (1 << 10)
    GUILD_MESSAGE_TYPING = (1 << 11)
    DIRECT_MESSAGES = (1 << 12)
    DIRECT_MESSAGE_REACTIONS = (1 << 13)
    DIRECT_MESSAGE_TYPING = (1 << 14)
    MESSAGE_CONTENT = (1 << 15)
    GUILD_SCHEDULED_EVENTS = (1 << 16)


class Event:
    # GUILDS (1 << 0)
    GUILD_CREATE = 'GUILD_CREATE'
    GUILD_UPDATE = 'GUILD_UPDATE'
    GUILD_DELETE = 'GUILD_DELETE'
    GUILD_ROLE_CREATE = 'GUILD_ROLE_CREATE'
    GUILD_ROLE_UPDATE = 'GUILD_ROLE_UPDATE'
    GUILD_ROLE_DELETE = 'GUILD_ROLE_DELETE'
    CHANNEL_CREATE = 'CHANNEL_CREATE'
    CHANNEL_UPDATE = 'CHANNEL_UPDATE'
    CHANNEL_DELETE = 'CHANNEL_DELETE'
    CHANNEL_PINS_UPDATE = 'CHANNEL_PINS_UPDATE'
    THREAD_CREATE = 'THREAD_CREATE'
    THREAD_UPDATE = 'THREAD_UPDATE'
    THREAD_DELETE = 'THREAD_DELETE'
    THREAD_LIST_SYNC = 'THREAD_LIST_SYNC'
    THREAD_MEMBER_UPDATE = 'THREAD_MEMBER_UPDATE'
    THREAD_MEMBERS_UPDATE = 'THREAD_MEMBERS_UPDATE'
    STAGE_INSTANCE_CREATE = 'STAGE_INSTANCE_CREATE'
    STAGE_INSTANCE_UPDATE = 'STAGE_INSTANCE_UPDATE'
    STAGE_INSTANCE_DELETE = 'STAGE_INSTANCE_DELETE'

    # GUILD_MEMBERS (1 << 1) 
    GUILD_MEMBER_ADD = 'GUILD_MEMBER_ADD'
    GUILD_MEMBER_UPDATE = 'GUILD_MEMBER_UPDATE'
    GUILD_MEMBER_REMOVE = 'GUILD_MEMBER_REMOVE'
    THREAD_MEMBERS_UPDATE = 'THREAD_MEMBERS_UPDATE' 

    # GUILD_MODERATION (1 << 2)
    GUILD_AUDIT_LOG_ENTRY_CREATE = 'GUILD_AUDIT_LOG_ENTRY_CREATE'
    GUILD_BAN_ADD = 'GUILD_BAN_ADD'
    GUILD_BAN_REMOVE = 'GUILD_BAN_REMOVE'

    # GUILD_EMOJIS_AND_STICKERS (1 << 3)
    GUILD_EMOJIS_UPDATE = 'GUILD_EMOJIS_UPDATE'
    GUILD_STICKERS_UPDATE = 'GUILD_STICKERS_UPDATE'

    # GUILD_INTEGRATIONS (1 << 4)
    GUILD_INTEGRATIONS_UPDATE = 'GUILD_INTEGRATIONS_UPDATE'
    INTEGRATION_CREATE = 'INTEGRATION_CREATE'
    INTEGRATION_UPDATE = 'INTEGRATION_UPDATE'
    INTEGRATION_DELETE = 'INTEGRATION_DELETE'

    # GUILD_WEBHOOKS (1 << 5)
    WEBHOOKS_UPDATE = 'WEBHOOKS_UPDATE'

    # GUILD_INVITES (1 << 6)
    INVITE_CREATE = 'INVITE_CREATE'
    INVITE_DELETE = 'INVITE_DELETE'

    # GUILD_VOICE_STATES (1 << 7)
    VOICE_STATE_UPDATE = 'VOICE_STATE_UPDATE'
    VOICE_SERVER_UPDATE = 'VOICE_SERVER_UPDATE'

    # GUILD_PRESENCES (1 << 8) **
    PRESENCE_UPDATE = 'PRESENCE_UPDATE'

    # GUILD_MESSAGES (1 << 9)
    MESSAGE_CREATE = 'MESSAGE_CREATE'
    MESSAGE_UPDATE = 'MESSAGE_UPDATE'
    MESSAGE_DELETE = 'MESSAGE_DELETE'
    MESSAGE_DELETE_BULK = 'MESSAGE_DELETE_BULK'

    # GUILD_MESSAGE_REACTIONS (1 << 10)
    MESSAGE_REACTION_ADD = 'MESSAGE_REACTION_ADD'
    MESSAGE_REACTION_REMOVE = 'MESSAGE_REACTION_REMOVE'
    MESSAGE_REACTION_REMOVE_ALL = 'MESSAGE_REACTION_REMOVE_ALL'
    MESSAGE_REACTION_REMOVE_EMOJI = 'MESSAGE_REACTION_REMOVE_EMOJI'

    # GUILD_MESSAGE_TYPING (1 << 11)
    TYPING_START = 'TYPING_START'

    # DIRECT_MESSAGES (1 << 12)
    MESSAGE_CREATE = 'MESSAGE_CREATE'
    MESSAGE_UPDATE = 'MESSAGE_UPDATE'
    MESSAGE_DELETE = 'MESSAGE_DELETE'
    CHANNEL_PINS_UPDATE = 'CHANNEL_PINS_UPDATE'

    # DIRECT_MESSAGE_REACTIONS (1 << 13)
    MESSAGE_REACTION_ADD = 'MESSAGE_REACTION_ADD'
    MESSAGE_REACTION_REMOVE = 'MESSAGE_REACTION_REMOVE'
    MESSAGE_REACTION_REMOVE_ALL = 'MESSAGE_REACTION_REMOVE_ALL'
    MESSAGE_REACTION_REMOVE_EMOJI = 'MESSAGE_REACTION_REMOVE_EMOJI'

    # DIRECT_MESSAGE_TYPING (1 << 14)
    TYPING_START = 'TYPING_START'

    # MESSAGE_CONTENT (1 << 15) ***

    # GUILD_SCHEDULED_EVENTS (1 << 16)
    GUILD_SCHEDULED_EVENT_CREATE = 'GUILD_SCHEDULED_EVENT_CREATE'
    GUILD_SCHEDULED_EVENT_UPDATE = 'GUILD_SCHEDULED_EVENT_UPDATE'
    GUILD_SCHEDULED_EVENT_DELETE = 'GUILD_SCHEDULED_EVENT_DELETE'
    GUILD_SCHEDULED_EVENT_USER_ADD = 'GUILD_SCHEDULED_EVENT_USER_ADD'
    GUILD_SCHEDULED_EVENT_USER_REMOVE = 'GUILD_SCHEDULED_EVENT_USER_REMOVE'

    # AUTO_MODERATION_CONFIGURATION (1 << 20)
    AUTO_MODERATION_RULE_CREATE = 'AUTO_MODERATION_RULE_CREATE'
    AUTO_MODERATION_RULE_UPDATE = 'AUTO_MODERATION_RULE_UPDATE'
    AUTO_MODERATION_RULE_DELETE = 'AUTO_MODERATION_RULE_DELETE'

    # AUTO_MODERATION_EXECUTION (1 << 21)
    AUTO_MODERATION_ACTION_EXECUTION = 'AUTO_MODERATION_ACTION_EXECUTION'

    # UTILS
    READY = 'READY'