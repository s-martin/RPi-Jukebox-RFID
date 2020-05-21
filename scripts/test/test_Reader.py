from mock import patch, MagicMock, mock
import pytest
from Reader import Reader
import os

def mock_get_devices():
    device = MagicMock()
    device.name.return_value = "TestDevice"
    return [device]

@pytest.fixture
def reader():
    return Reader()

@mock.patch("os.listdir", mock.MagicMock(return_value="test1"))
def test1():
    assert "test1" == os.listdir()

class TestReader:

    @mock.patch("Reader.get_devices", side_effect=mock_get_devices)
    #@mock.patch("Reader.device.name", mock.MagicMock(return_value="TestDevice"))
    #@mock.patch.object(Reader, "device", mock.MagicMock(return_value="TestDevice"))
    def test_init(self, reader):
        print("TEST")
        print(reader.device.name)
        print(reader.reader)
        #reader.device.name.assert_called()
        #assert reader.device.name is "TestDevice"
