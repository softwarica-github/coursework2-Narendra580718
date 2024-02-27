import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
import socket
import tkinter as tk
from cw2 import IDS_GUI

class TestIDS_GUI(unittest.TestCase):
    def setUp(self):
        # Create a mock tkinter master object
        self.master = tk.Tk()
        self.mock_socket = MagicMock()

    def tearDown(self):
        # Destroy the mock tkinter master object after each test
        self.master.destroy()

    def test_detect_intrusion_with_intrusion_keywords(self):
        gui = IDS_GUI(self.master)
        data_with_intrusion = "This is a hack attempt"
        self.assertTrue(gui.detect_intrusion(data_with_intrusion))

    def test_detect_intrusion_without_intrusion_keywords(self):
        gui = IDS_GUI(self.master)
        data_without_intrusion = "This is a regular message"
        self.assertFalse(gui.detect_intrusion(data_without_intrusion))

    @patch('socket.socket')
    def test_stop_server(self, mock_socket):
        mock_socket.return_value = self.mock_socket
        gui = IDS_GUI(self.master)
        gui.server_socket = mock_socket
        gui.stop_server()
        gui.server_socket.close.assert_called_once()

if __name__ == '__main__':
    unittest.main()
