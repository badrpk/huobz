import asyncio
import logging
from bleak import BleakScanner

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BluetoothCommunication:
    def __init__(self):
        self.devices = []

    async def scan_devices(self):
        logger.info("Scanning for Bluetooth devices...")
        self.devices = await BleakScanner.discover()
        for idx, device in enumerate(self.devices):
            logger.info(f"{idx + 1}. Name: {device.name}, Address: {device.address}")

    def list_devices(self):
        if not self.devices:
            logger.info("No devices found. Please scan first.")
        else:
            for idx, device in enumerate(self.devices):
                logger.info(f"{idx + 1}. Name: {device.name}, Address: {device.address}")


# Example usage
if __name__ == "__main__":
    bluetooth_comm = BluetoothCommunication()
    asyncio.run(bluetooth_comm.scan_devices())
    bluetooth_comm.list_devices()
