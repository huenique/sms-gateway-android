import asyncio
import copy
import subprocess

SMS_API = list[str] | None


class Termux:
    """Interface to Termux API"""

    sms_api: SMS_API

    def __init__(self, sms_api: SMS_API = None):
        self.sms_api = sms_api

    async def send_sms(
        self, number: str, message: str
    ) -> subprocess.CompletedProcess[str]:
        """Send an SMS message to a specified number.

        Args:
            number: The phone number to send the message to.
            message: The message to send.

        Raises:
            RuntimeError: The Termux SMS API is not available.
        """
        if self.sms_api is None:
            raise RuntimeError("Termux SMS API is not available")

        command = copy.deepcopy(self.sms_api)
        command.append(number)
        command.append(message)

        loop = asyncio.get_running_loop()

        proc = await loop.run_in_executor(None, subprocess.run, command)
        proc.check_returncode()

        return proc

    @classmethod
    def create(cls, sms_api: SMS_API = None) -> "Termux":
        return cls(sms_api)
