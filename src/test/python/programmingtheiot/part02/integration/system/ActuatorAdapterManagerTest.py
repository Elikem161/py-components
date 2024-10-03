import logging
import unittest

import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.cda.system.ActuatorAdapterManager import ActuatorAdapterManager
from programmingtheiot.common.DefaultDataMessageListener import DefaultDataMessageListener
from programmingtheiot.data.ActuatorData import ActuatorData

class ActuatorAdapterManagerTest(unittest.TestCase):
    """
    This test case class contains very basic unit tests for
    ActuatorAdapterManager. It should not be considered complete,
    but serve as a starting point for the student implementing
    additional functionality within their Programming the IoT
    environment.
    """
    
    @classmethod
    def setUpClass(cls):
        logging.basicConfig(format='%(asctime)s:%(module)s:%(levelname)s:%(message)s', level=logging.DEBUG)
        logging.info("Testing ActuatorAdapterManager class...")
        
        cls.defaultMsgListener = DefaultDataMessageListener()
        cls.actuatorAdapterMgr = ActuatorAdapterManager()
        cls.actuatorAdapterMgr.setDataMessageListener(cls.defaultMsgListener)

    def testSendActuatorCommand(self):
        # Create ActuatorData
        actuatorData = ActuatorData(typeID=ConfigConst.HUMIDIFIER_ACTUATOR_TYPE, locationID='constraineddevice001')
        actuatorData.setResponseFlag(False)  # Ensure it’s not a response
        actuatorData.setValue(50.0)  # Set a value if needed

        # Send command
        response = self.actuatorAdapterMgr.sendActuatorCommand(actuatorData)

        # Assert response and log it
        self.assertIsNotNone(response)
        logging.info("Response from actuator command: %s", response)

    def testHumidifierSimulation(self):
        ad = ActuatorData(typeID=ConfigConst.HUMIDIFIER_ACTUATOR_TYPE)
        ad.setValue(50.0)
        
        ad.setCommand(ConfigConst.COMMAND_ON)
        self.actuatorAdapterMgr.sendActuatorCommand(ad)
        
        ad.setCommand(ConfigConst.COMMAND_OFF)
        self.actuatorAdapterMgr.sendActuatorCommand(ad)

    def testHvacSimulation(self):
        ad = ActuatorData(typeID=ConfigConst.HVAC_ACTUATOR_TYPE)
        ad.setValue(22.5)
        
        ad.setCommand(ConfigConst.COMMAND_ON)
        self.actuatorAdapterMgr.sendActuatorCommand(ad)
        
        ad.setCommand(ConfigConst.COMMAND_OFF)
        self.actuatorAdapterMgr.sendActuatorCommand(ad)

if __name__ == "__main__":
    unittest.main()
