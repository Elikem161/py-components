"""
Configuration and other constants for use when looking up
configuration values or when default values may be needed.
"""

#####
# General Names and Defaults
#

NOT_SET = 'Not Set'

DEFAULT_HOST             = 'localhost'
DEFAULT_COAP_PORT        = 5683
DEFAULT_COAP_SECURE_PORT = 5684
DEFAULT_MQTT_PORT        = 1883
DEFAULT_MQTT_SECURE_PORT = 8883
DEFAULT_RTSP_STREAM_PORT = 8554
DEFAULT_KEEP_ALIVE       = 60
DEFAULT_POLL_CYCLES      = 60
DEFAULT_VAL              = 0.0
DEFAULT_COMMAND          = 0
DEFAULT_STATUS           = 0
DEFAULT_TIMEOUT          = 5
DEFAULT_TTL              = 300
DEFAULT_QOS              = 0

# Default geographical coordinates
DEFAULT_LAT = DEFAULT_VAL
DEFAULT_LON = DEFAULT_VAL
DEFAULT_ELEVATION = DEFAULT_VAL

DEFAULT_ACTION_ID = 0
INITIAL_SEQUENCE_NUMBER = 0

DEFAULT_STREAM_FPS             = 30
DEFAULT_MIN_STREAM_FPS         = 8
DEFAULT_MAX_STREAM_FPS         = 60
DEFAULT_STREAM_FRAME_WIDTH     = 1440
DEFAULT_STREAM_FRAME_HEIGHT    = 1080
DEFAULT_MIN_MOTION_PIXELS_DIFF = 10000
DEFAULT_MAX_CACHED_FRAMES      = 10
DEFAULT_STREAM_PROTOCOL        = 'rtsp'

PRODUCT_NAME = 'PIOT'
CLOUD        = 'Cloud'
GATEWAY      = 'Gateway'
CONSTRAINED  = 'Constrained'
DEVICE       = 'Device'
SERVICE      = 'Service'

CONSTRAINED_DEVICE = CONSTRAINED + DEVICE
GATEWAY_SERVICE    = GATEWAY + SERVICE
CLOUD_SERVICE      = CLOUD + SERVICE

#####
# Property Names
#

NAME_PROP        = 'name'
DEVICE_ID_PROP   = 'deviceID'
TYPE_CATEGORY_ID_PROP = 'typeCategoryID'
TYPE_ID_PROP     = 'typeID'
TIMESTAMP_PROP   = 'timeStamp'
HAS_ERROR_PROP   = 'hasError'
STATUS_CODE_PROP = 'statusCode'
LOCATION_ID_PROP = 'locationID'
LATITUDE_PROP    = 'latitude'
LONGITUDE_PROP   = 'longitude'
ELEVATION_PROP   = 'elevation'

COMMAND_PROP     = 'command'
STATE_DATA_PROP  = 'stateData'
VALUE_PROP       = 'value'
IS_RESPONSE_PROP = 'isResponse'

CPU_UTIL_PROP    = 'cpuUtil'
DISK_UTIL_PROP   = 'diskUtil'
MEM_UTIL_PROP    = 'memUtil'

ACTION_ID_PROP             = 'actionID'
DATA_URI_PROP              = 'dataURI'
MESSAGE_PROP               = 'message'
ENCODING_NAME_PROP         = 'encodingName'
RAW_DATA_PROP              = 'rawData'
SEQUENCE_NUMBER_PROP       = 'seqNo'
USE_SEQUENCE_NUMBER_PROP   = 'useSeqNo'
SEQUENCE_NUMBER_TOTAL_PROP = 'seqNoTotal'

SEND_RESOURCE_NAME_PROP    = 'sendResourceName'
RECEIVE_RESOURCE_NAME_PROP = 'receiveResourceName'
IS_PING_PROP               = 'isPing'

#####
# Resource and Topic Names
#

ACTUATOR_CMD      = 'ActuatorCmd'
ACTUATOR_RESPONSE  = 'ActuatorResponse'
MGMT_STATUS_MSG    = 'MgmtStatusMsg'
MGMT_STATUS_CMD    = 'MgmtStatusCmd'
MEDIA_MSG          = 'MediaMsg'
SENSOR_MSG         = 'SensorMsg'
SYSTEM_PERF_MSG    = 'SystemPerfMsg'

UPDATE_NOTIFICATIONS_MSG      = 'UpdateMsg'
RESOURCE_REGISTRATION_REQUEST = 'ResourceRegRequest'

LED_ACTUATOR_NAME        = 'LedActuator'
HUMIDIFIER_ACTUATOR_NAME = 'HumidifierActuator'
HVAC_ACTUATOR_NAME       = 'HvacActuator'

HUMIDITY_SENSOR_NAME = 'HumiditySensor'
PRESSURE_SENSOR_NAME = 'PressureSensor'
TEMP_SENSOR_NAME     = 'TempSensor'
CAMERA_SENSOR_NAME   = 'CameraSensor'

COMMAND_OFF = DEFAULT_COMMAND
COMMAND_ON  = 1

DEFAULT_TYPE_ID           = 0
DEFAULT_TYPE_CATEGORY_ID  = 0
DEFAULT_ACTUATOR_TYPE     = 1001  # Example actuator type ID
DEFAULT_SENSOR_TYPE       = 1010  # Example sensor type ID

# Define device types
ENV_DEVICE_TYPE           = 1000
HUMIDITY_SENSOR_TYPE      = 1010
PRESSURE_SENSOR_TYPE      = 1011
TEMP_SENSOR_TYPE          = 1013
DISPLAY_DEVICE_TYPE       = 2000
LED_DISPLAY_ACTUATOR_TYPE = 2001
HVAC_ACTUATOR_TYPE        = 2002
HUMIDIFIER_ACTUATOR_TYPE  = 2003  
CAMERA_SENSOR_TYPE        = 3001
CAMERA_MOTION_SENSOR_TYPE = 3002
CAMERA_STREAM_SENSOR_TYPE = 3004

SYSTEM_MGMT_TYPE          = 8000
RESOURCE_MGMT_TYPE        = 8001
RESOURCE_MGMT_NAME        = 'ResourceMgmt'

SYSTEM_PERF_TYPE          = 9000
CPU_UTIL_TYPE             = 9001
DISK_UTIL_TYPE            = 9002
MEM_UTIL_TYPE             = 9003

# New Constants for SystemPerformanceData
SYSTEM_PERF_NAME = 'SystemPerformanceData'  # Name for system performance data
CPU_UTIL_NAME  = 'DeviceCpuUtil'
DISK_UTIL_NAME = 'DeviceDiskUtil'
MEM_UTIL_NAME  = 'DeviceMemUtil'

#####
# Typical topic naming conventions
#

# for CDA to GDA communications
CDA_UPDATE_NOTIFICATIONS_MSG_RESOURCE = f"{PRODUCT_NAME}/{CONSTRAINED_DEVICE}/{UPDATE_NOTIFICATIONS_MSG}"
CDA_ACTUATOR_CMD_MSG_RESOURCE         = f"{PRODUCT_NAME}/{CONSTRAINED_DEVICE}/{ACTUATOR_CMD}"
CDA_ACTUATOR_RESPONSE_MSG_RESOURCE    = f"{PRODUCT_NAME}/{CONSTRAINED_DEVICE}/{ACTUATOR_RESPONSE}"
CDA_MGMT_STATUS_MSG_RESOURCE          = f"{PRODUCT_NAME}/{CONSTRAINED_DEVICE}/{MGMT_STATUS_MSG}"
CDA_MGMT_CMD_MSG_RESOURCE             = f"{PRODUCT_NAME}/{CONSTRAINED_DEVICE}/{MGMT_STATUS_CMD}"
CDA_MEDIA_DATA_MSG_RESOURCE           = f"{PRODUCT_NAME}/{CONSTRAINED_DEVICE}/{MEDIA_MSG}"
CDA_REGISTRATION_REQUEST_RESOURCE     = f"{PRODUCT_NAME}/{CONSTRAINED_DEVICE}/{RESOURCE_REGISTRATION_REQUEST}"
CDA_SENSOR_DATA_MSG_RESOURCE          = f"{PRODUCT_NAME}/{CONSTRAINED_DEVICE}/{SENSOR_MSG}"
CDA_SYSTEM_PERF_MSG_RESOURCE          = f"{PRODUCT_NAME}/{CONSTRAINED_DEVICE}/{SYSTEM_PERF_MSG}"

#####
# Configuration Sections, Keys and Defaults
#

# Set the following paths to absolute paths as needed
DEFAULT_CONFIG_FILE_NAME = '/absolute/path/to/your/PiotConfig.props'  # Update this path
DEFAULT_CRED_FILE_NAME   = '/absolute/path/to/your/PiotCred.props'    # Update this path

TEST_GDA_DATA_PATH_KEY = 'testGdaDataPath'
TEST_CDA_DATA_PATH_KEY = 'testCdaDataPath'

LOCAL   = 'Local'
MQTT    = 'Mqtt'
COAP    = 'Coap'
OPCUA   = 'Opcua'
SMTP    = 'Smtp'

DEVICE_ID_KEY          = 'deviceID'
DEVICE_LOCATION_ID_KEY = 'deviceLocationID'

CLOUD_GATEWAY_SERVICE = f"{CLOUD}.{GATEWAY_SERVICE}"
COAP_GATEWAY_SERVICE  = f"{COAP}.{GATEWAY_SERVICE}"
MQTT_GATEWAY_SERVICE  = f"{MQTT}.{GATEWAY_SERVICE}"
OPCUA_GATEWAY_SERVICE = f"{OPCUA}.{GATEWAY_SERVICE}"
SMTP_GATEWAY_SERVICE  = f"{SMTP}.{GATEWAY_SERVICE}"

CRED_SECTION = "Credentials"

FROM_ADDRESS_KEY     = 'fromAddr'
TO_ADDRESS_KEY       = 'toAddr'
TO_MEDIA_ADDRESS_KEY = 'toMediaAddr'
TO_TXT_ADDRESS_KEY   = 'toTxtAddr'

HOST_KEY             = 'host'
PORT_KEY             = 'port'
SECURE_PORT_KEY      = 'securePort'

ROOT_CERT_ALIAS = 'root'

KEY_STORE_CLIENT_IDENTITY_KEY = 'keyStoreClientIdentity'
KEY_STORE_SERVER_IDENTITY_KEY = 'keyStoreServerIdentity'

KEY_STORE_FILE_KEY    = 'keyStoreFile'
KEY_STORE_AUTH_KEY    = 'keyStoreAuth'
TRUST_STORE_FILE_KEY  = 'trustStoreFile'
TRUST_STORE_ALIAS_KEY  = 'trustStoreAlias'
TRUST_STORE_AUTH_KEY   = 'trustStoreAuth'
USER_NAME_TOKEN_KEY   = 'userToken'
USER_AUTH_TOKEN_KEY   = 'authToken'
API_TOKEN_KEY         = 'apiToken'

CERT_FILE_KEY        = 'certFile'
CRED_FILE_KEY        = 'credFile'
ENABLE_AUTH_KEY      = 'enableAuth'
ENABLE_CRYPT_KEY     = 'enableCrypt'
ENABLE_SIMULATOR_KEY = 'enableSimulator'
ENABLE_EMULATOR_KEY  = 'enableEmulator'
ENABLE_SENSE_HAT_KEY = 'enableSenseHAT'
ENABLE_LOGGING_KEY    = 'enableLogging'
USE_WEB_ACCESS_KEY    = 'useWebAccess'
POLL_CYCLES_KEY       = 'pollCycleSecs'
KEEP_ALIVE_KEY        = 'keepAlive'
DEFAULT_QOS_KEY       = 'defaultQos'

ENABLE_MQTT_CLIENT_KEY = 'enableMqttClient'
ENABLE_COAP_CLIENT_KEY = 'enableCoapClient'
ENABLE_COAP_SERVER_KEY = 'enableCoapServer'

ENABLE_SYSTEM_PERF_KEY = 'enableSystemPerformance'
ENABLE_SENSING_KEY     = 'enableSensing'
