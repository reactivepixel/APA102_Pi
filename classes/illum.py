import spidev

class LEDStrand:
    def __init__(self, idleState, assignments):
        self.totalLEDs = len(assignments)
        self.idleState = idleState
        self.assignments = assignments

class Illum:
        def __init__(self, strands, brightness_float=.5 ):
            "Pass in an array where each value represents how many LEDs are in the corresponding strand , Brightness as a float"
            idleRGB_32bit = [binary_literal_from_float(brightness_float), 0, 0, 0] # bright, r, g, b 32-bit
            for strandIndex, strandCount in strands:
                self.strands[strandIndex] = LEDStrand(idleRGB_32bit, idleRGB_32bit * strandCount)
                self.strands[strandIndex].spi = spidev.SpiDev()
                self.strands[strandIndex].spi.open(0, 1) #(bus, device) - Connects to the specified SPI device, opening /dev/spidev<bus>.<device>

                # SPI Settings
                self.strands[strandIndex].spi.max_speed_hz = 80

        def binary_literal_from_float(input_float):
            max_8bit = 255
            return bin(max_8bit * input_float)



ctrl = Illum([60])
