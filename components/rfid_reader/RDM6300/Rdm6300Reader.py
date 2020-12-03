#!/usr/bin/env python3
# Implements RDM6300 reader.

import serial
import string
import logging


logger = logging.getLogger(__name__)


class Rdm6300Reader:
    def __init__(self):
        device = '/dev/ttyS0'
        baudrate = 9600
        ser_timeout = 0.1
        self.last_card_id = ''
        try:
            self.rfid_serial = serial.Serial(device, baudrate, timeout=ser_timeout)
        except serial.SerialException as e:
            logger.error(e)
            exit(1)

    def readCard(self):
        byte_card_id = b''

        try:
            while True:
                try:
                    read_byte = self.rfid_serial.read()

                    if read_byte == b'\x02':    # start byte
                        while read_byte != b'\x03':     # end bye
                            read_byte = self.rfid_serial.read()
                            byte_card_id += read_byte

                        card_id = byte_card_id.decode('utf-8')
                        byte_card_id = ''
                        card_id = ''.join(x for x in card_id if x in string.printable)

                        # Only return UUIDs with correct length
                        if len(card_id) == 12 and card_id != self.last_card_id:
                            self.last_card_id = card_id
                            self.rfid_serial.reset_input_buffer()
                            return self.last_card_id

                        else:   # wrong UUID length or already send that UUID last time
                            self.rfid_serial.reset_input_buffer()

                except ValueError as ve:
                    logger.errror(ve)

        except serial.SerialException as se:
            logger.error(se)

    def cleanup(self):
        self.rfid_serial.close()
