from homeassistant.helpers.entity import Entity
from .charger import BCPCharger
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    api_url = entry.data["api_url"]
    charger = BCPCharger(api_url)
    async_add_entities([BCPChargerSensor(charger)])

class BCPChargerSensor(Entity):
    def __init__(self, charger):
        self.charger = charger
        self._state = "Unknown"

    async def async_update(self):
        data = self.charger.get_status()
        self._state = "Charging" if data["state"] == 6 else "Not Charging"

    @property
    def name(self):
        return "BCP Charger Status"

    @property
    def state(self):
        return self._state
