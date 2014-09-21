from pritunl.constants import *
from pritunl.exceptions import *
from pritunl.descriptors import *
from pritunl.settings_group import SettingsGroup

class SettingsApp(SettingsGroup):
    group = 'app'
    fields = {
        'key_link_timeout': 86400,
        'password_len_limit': 128,
        'public_ip_server': 'http://ip.pritunl.com/json',
        'notification_server': 'http://ip.pritunl.com/notification',
        'update_check_rate': 3600,
        'session_timeout': 86400,
        'log_entry_limit': 50,
        'rate_limit_sleep': 0.5,
        'short_url_length': 5,
        'http_request_timeout': 10,
        'request_queue_size': 512,
        'static_cache_time': 43200,
        'auth_time_window': 300,
        'auth_limiter_ttl': 60,
        'auth_limiter_count_max': 30,
    }