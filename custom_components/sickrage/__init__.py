"""
This will connect the Sickrage platform to Homeassistant, showing stats and switches from Sickrage.
"""
import logging
import requests
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.const import (CONF_HOST, CONF_API_KEY)

from homeassistant.helpers.entity import Entity

requests.packages.urllib3.disable_warnings()

__version__ = '0.0.2'

DOMAIN = 'sickrage'
ICON = 'progress-download'
COMPONENT_AUTHOR = 'swetoast'
COMPONENT_NAME = 'Sickrage'
COMPONENT_REPO = 'https://github.com/custom-components/sickrage'

TIMEOUT = 10

CONFIG_SCHEMA = vol.Schema({
    DOMAIN: vol.Schema({
        vol.Required(CONF_HOST): cv.string,
        vol.Required(CONF_API_KEY): cv.string,
    }),
}, extra=vol.ALLOW_EXTRA)

_LOGGER = logging.getLogger(__name__)

def setup(hass, config):
    """Set up the component."""
    _LOGGER.info('Starting setup')
    _LOGGER.warning(' %s is starting, report any issues to %s',__version__, COMPONENT_REPO)
    host = config[DOMAIN][CONF_HOST]
    api = config[DOMAIN][CONF_API_KEY]
    hass.data[DOMAIN][CONF_HOST] = host
    hass.data[DOMAIN][CONF_API_KEY] = api

    def restart_sickrage_service(call):
        """Set up recuring update."""
        generic_command(host, api, 'sb.restart')
  
    def update_sickrage_service(call):
        """Set up recuring update."""
        generic_command(host, api, 'sb.update')

    def shutdown_sickrage_service(call):
        """Set up recuring update."""
        generic_command(host, api, 'sb.shutdown')

    def clearlogs_sickrage_service(call):
        """Set up recuring update."""
        generic_command(host, api, 'clear.logs')

    def clearhistory_sickrage_service(call):
        """Set up recuring update."""
        generic_command(host, api, 'clear.history')

    def forcepropersearch_sickrage_service(call):
        """Set up recuring update."""
        generic_command(host, api, 'sb.propersearch')

    def forcedailysearch_sickrage_service(call):
        """Set up recuring update."""
        generic_command(host, api, 'sb.dailysearch')

    hass.services.register(DOMAIN, 'restart', restart_sickrage_service)
    hass.services.register(DOMAIN, 'update', update_sickrage_service)
    hass.services.register(DOMAIN, 'shutdown', shutdown_sickrage_service)
    hass.services.register(DOMAIN, 'clearlogs', clearlogs_sickrage_service)
    hass.services.register(DOMAIN, 'clearhistory', clearhistory_sickrage_service)
    hass.services.register(DOMAIN, 'forcepropersearch', forcepropersearch_sickrage_service)
    hass.services.register(DOMAIN, 'forcedailysearch', forcedailysearch_sickrage_service)
    return True
  
def generic_command(host, api, command):
    fetchurl = host + '/' + api + '/?cmd=' + command
    result = requests.get(fetchurl, timeout=TIMEOUT, verify=False).json()
    print (result['result'])
