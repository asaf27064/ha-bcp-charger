from homeassistant.components.switch import SwitchEntity
from .charger import BCPCharger
from .const import DOMAIN

async def async_setup_entry(hass, entry, async_add_entities):
    api_url = entry.data["api_url"]
    charger = BCPCharger(api_url)
    async_add_entities([BCPChargerSwitch(charger)])

class BCPChargerSwitch(SwitchEntity):
    def __init__(self, charger):
        self.charger = charger
        self._is_on = False

    async def async_turn_on(self):
        if self.charger.start_charging():
            self._is_on = True

    async def async_turn_off(self):
        if self.charger.stop_charging():
            self._is_on = False

    @property
    def name(self):
        return "BCP Charger"
    
    @property
    def is_on(self):
        return self._is_on
