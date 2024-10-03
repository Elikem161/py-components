import logging
import unittest

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.data.ActuatorData import ActuatorData


class ActuatorDataTest(unittest.TestCase):
    """
    This test case class contains very basic unit tests for
    ActuatorData. It should not be considered complete,
    but serve as a starting point for the student implementing
    additional functionality within their Programming the IoT
    environment.
    """
    
    DEFAULT_NAME = "ActuatorDataFooBar"
    DEFAULT_STATE_DATA = "{state: None}"
    DEFAULT_VALUE = 15.2
    
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info("Testing ActuatorData class...")

    def setUp(self):
        pass

    def tearDown(self):
        pass
    
    def testDefaultValues(self):
        ad = ActuatorData()
        
        self.assertEqual(ad.getCommand(), ConfigConst.DEFAULT_COMMAND)
        self.assertEqual(ad.getStatusCode(), ConfigConst.DEFAULT_STATUS)
        
        logging.info("Actuator data as string: %s", ad)

    def testParameterUpdates(self):
        ad = self._createTestActuatorData()
        
        self.assertEqual(ad.getName(), self.DEFAULT_NAME)
        self.assertEqual(ad.getCommand(), ConfigConst.COMMAND_ON)
        self.assertEqual(ad.getStateData(), self.DEFAULT_STATE_DATA)
        self.assertEqual(ad.getValue(), self.DEFAULT_VALUE)

    def testFullUpdate(self):
        ad = ActuatorData()
        ad2 = self._createTestActuatorData()
        
        ad.updateData(ad2)
        
        self.assertEqual(ad.getCommand(), ConfigConst.COMMAND_ON)
        self.assertEqual(ad.getStateData(), self.DEFAULT_STATE_DATA)
        self.assertEqual(ad.getValue(), self.DEFAULT_VALUE)
        
    def _createTestActuatorData(self):
        ad = ActuatorData()
        
        ad.setName(self.DEFAULT_NAME)
        ad.setCommand(ConfigConst.COMMAND_ON)
        ad.setStateData(self.DEFAULT_STATE_DATA)
        ad.setValue(self.DEFAULT_VALUE)
        
        logging.info("Actuator data as string: %s", ad)
        
        return ad

if __name__ == "__main__":
    unittest.main()
