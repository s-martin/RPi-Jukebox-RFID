#!/usr/bin/env python3
# Implementation of PN532 reader.

import logging

from py532lib.i2c import *
from py532lib.mifare import *

logger = logging.getLogger(__name__)


class Pn532Reader:
    def __init__(self):
        pn532 = Pn532_i2c()
        self.device = Mifare()
        self.device.SAMconfigure()
        self.device.set_max_retries(MIFARE_WAIT_FOR_ENTRY)

    def readCard(self):
        return str(+int('0x' + self.device.scan_field().hex(), 0))

    def cleanup(self):
        # Not sure if something needs to be done here.
        logger.debug("PN532Reader clean up.")
