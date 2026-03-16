from typing import Any
from synapse.module_api import ModuleApi
import aiohttp

class WelcomeModule:
    def __init__(self, config: Any, api: ModuleApi):
        self.api = api
        self.config = config
        with open(self.config['path']) as f:
            self.content = f.read()
        api.register_account_validity_callbacks(
            on_user_registration=self.on_user_registration
        )

    async def on_user_registration(self, user: str) -> None:
        try:
            payload = {
                        "user_id": f"{user}",
                        "content": {
                            "msgtype": "m.text",
                            "format": "org.matrix.custom.html",
                            "body": f"{self.content}",
                            "formatted_body": f"{self.content}"
                        }
                    }
            async with aiohttp.ClientSession() as session:
                response = await session.post(
                url="http://localhost:8008/_synapse/admin/v1/send_server_notice",
                headers={
                    "Authorization": f"Bearer {self.config['token']}",
                    "Content-Type": "application/json"},
                json=payload
                )
                print(response.status)
                data = await response.json()
                print(data)
        except Exception as e:
            print(e)