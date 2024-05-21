from rest_framework.authentication import TokenAuthentication as BaseTokenAuth

class TokenAuthentication(BaseTokenAuth):
    keyword = 'bearer'

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ]
}