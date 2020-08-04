from types import MappingProxyType

PAGINATION_CLASS: str = 'rest_framework.pagination.LimitOffsetPagination'

REST_FRAMEWORK_SETTINGS: MappingProxyType = MappingProxyType({
    'DEFAULT_AUTHENTICATION_CLASSES': (),
    'DEFAULT_FILTER_BACKENDS': (),
    'DEFAULT_PAGINATION_CLASS': PAGINATION_CLASS, 'PAGE_SIZE': 8
})
