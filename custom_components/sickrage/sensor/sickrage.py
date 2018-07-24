"""
This will connect the Sickrage platform to Homeassistant, showing stats and switches from Sickrage.
"""
import logging
from datetime import timedelta

import requests

from homeassistant.const import CONF_API_KEY, CONF_HOST
from homeassistant.helpers.entity import Entity

requests.packages.urllib3.disable_warnings()

SCAN_INTERVAL = timedelta(minutes=5)
DOMAIN = 'sickrage'

__version__ = '0.0.2'

ICON = 'progress-download'
COMPONENT_AUTHOR = 'swetoast'
COMPONENT_NAME = 'Sickrage'
COMPONENT_REPO = 'https://github.com/custom-components/sickrage'

TIMEOUT = 10

ATTR_TOTAL = 'Total Episodes'
ATTR_ACTIVE = 'Active Shows'
ATTR_DOWNLOADED = 'Downloaded Episodes'
ATTR_SHOWS = 'Total Shows'
ATTR_SNATCHED = 'Snatched Episodes'

_LOGGER = logging.getLogger(__name__)

def setup_platform(hass, config, add_devices_callback, discovery_info=None):
    """Set up the Sickrage device platform."""
    dev = []
    host = config[DOMAIN][CONF_HOST]
    api = config[DOMAIN][CONF_API_KEY]
    dev.append(SickrageSensor('Sickrage total shows', 'show', host, api))
    dev.append(SickrageSensor('Sickrage active shows', 'show', host, api))
    dev.append(SickrageSensor('Sickrage downloaded episodes', 'ep', host, api))
    dev.append(SickrageSensor('Sickrage total episodes', 'ep', host, api))
    add_devices_callback(dev, True)
    return

def call_api(host, api, cmd):
    """Place docstring here"""
    fetchurl = host + '/' + api + '/?cmd=' + cmd
    result = requests.get(fetchurl, timeout=5, verify=False).json()
    return result

class SickrageSensor(Entity):
    """Place docstring here"""
    def __init__(self, name, source, host, api):
        self._source = source
        self._state = None
        self._name = name
        self._host = host
        self._api = api
        self._description = None
        self.update()

    def update(self):
        """Place docstring here"""
        if self._source == 'active_show':
            result = call_api(self._host, self._api, 'shows.stats')
            self._state = (str(result['data']['shows_active']))
        elif self._source == 'total_shows':
            result = call_api(self._host, self._api, 'shows.stats')
            self.state = (str(result['data']['shows_total']))
        elif self._source == 'episodes_downloaded':
            result = call_api(self._host, self._api, 'shows.stats')
            self._state = (str(result['data']['ep_downloaded']))
        elif self._source == 'episodes_total':
            result = call_api(self._host, self._api, 'shows.stats')
            self._state = (str(result['data']['ep_total']))
        elif self._source == 'ep_snatched':
            result = call_api(self._host, self._api, 'shows.stats')
            self._state = (str(result['data']['ep_snatched']))

    @property
    def name(self):
        """Place docstring here"""
        return self._name

    @property
    def state(self):
        """Place docstring here"""
        return self._state

    @property
    def icon(self):
        """Place docstring here"""
        return ICON

    @property
    def device_state_attributes(self):
        """Place docstring here"""
        return
