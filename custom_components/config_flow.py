import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import HomeAssistant
from .const import DOMAIN

CONFIG_SCHEMA = vol.Schema(
    {vol.Required("api_url"): str}
)

class BCPChargerConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="BCP Charger", data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=CONFIG_SCHEMA
        )
