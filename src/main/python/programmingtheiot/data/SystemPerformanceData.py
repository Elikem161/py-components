import programmingtheiot.common.ConfigConst as ConfigConst
from programmingtheiot.data.BaseIotData import BaseIotData

class SystemPerformanceData(BaseIotData):
    """
    Shell representation of class for student implementation.
    """
    DEFAULT_VAL = ConfigConst.DEFAULT_VAL  # Use DEFAULT_VAL from ConfigConst
    
    def __init__(self, d=None):
        super(SystemPerformanceData, self).__init__(name=ConfigConst.SYSTEM_PERF_NAME, typeID=ConfigConst.SYSTEM_PERF_TYPE, d=d)
        
        self.cpuUtil = self.DEFAULT_VAL
        self.memUtil = self.DEFAULT_VAL
    
    def getCpuUtilization(self):
        return self.cpuUtil
    
    def getDiskUtilization(self):
        pass
    
    def getMemoryUtilization(self):
        return self.memUtil
    
    def setCpuUtilization(self, cpuUtil):
        self.cpuUtil = cpuUtil
        self.updateTimeStamp()
    
    def setDiskUtilization(self, diskUtil):
        pass
    
    def setMemoryUtilization(self, memUtil):
        self.memUtil = memUtil
        self.updateTimeStamp()
    
    def _handleUpdateData(self, data):
        if data and isinstance(data, SystemPerformanceData):
            self.cpuUtil = data.getCpuUtilization()
            self.memUtil = data.getMemoryUtilization()
