from os import environ as env

from hypercorn import Config as HypercornConfig

from server.config.exceptions import NoPortFoundError


class Config(HypercornConfig):
    """
    Summary
    -------
    the config class for the server
    """
    if not (WINGMAN_PORT := env.get('WINGMAN_PORT', 3997)):
        if not isinstance(WINGMAN_PORT, int):
            raise NoPortFoundError

    _bind = [f"0.0.0.0:{WINGMAN_PORT}"]
    access_log_format = '%(s)s "%(R)s" %(h)s "%(a)s"'
    accesslog = '-'
