#!/usr/bin/env python3
# Implementation of RC522 reader.

import RPi.GPIO as GPIO
import logging

import pirc522

logger = logging.getLogger(__name__)


class Rc522Reader(object):
    def __init__(self):
        self.device = pirc522.RFID()

    def readCard(self):
        # Scan for cards
        self.device.wait_for_tag()
        (error, tag_type) = self.device.request()

        if not error:
            logger.info("Card detected.")
            # Perform anti-collision detection to find card uid
            (error, uid) = self.device.anticoll()
            if not error:
                card_id = ''.join((str(x) for x in uid))
                logger.info(card_id)
                return card_id
        logger.debug("No Device ID found.")
        return None

    @staticmethod
    def cleanup():
        GPIO.cleanup()
