import unittest
from huobz_cellular.src.bluetooth_comm import BluetoothCommunication
import logging

class TestBluetoothCommunication(unittest.TestCase):
    def test_initialization(self):
        bt_comm = BluetoothCommunication()
        self.assertEqual(bt_comm.devices, [])

    def test_list_devices_without_scan(self):
        bt_comm = BluetoothCommunication()
        with self.assertLogs('huobz_cellular.src.bluetooth_comm', level='INFO') as log:
            bt_comm.list_devices()
            self.assertIn("No devices found. Please scan first.", log.output[0])

if __name__ == "__main__":
    unittest.main()
