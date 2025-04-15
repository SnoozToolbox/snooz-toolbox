PLATFORM_NAME = None
LINUX_DISTRIBUTION = None
APPLICATION_CONTEXT = None

def get():
    return PLATFORM_NAME, LINUX_DISTRIBUTION, APPLICATION_CONTEXT

def restore(platform_name, linux_distribution, application_context):
    global PLATFORM_NAME, LINUX_DISTRIBUTION, APPLICATION_CONTEXT
    PLATFORM_NAME = platform_name
    LINUX_DISTRIBUTION = linux_distribution
    APPLICATION_CONTEXT = application_context