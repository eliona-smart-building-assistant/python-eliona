# eliona.api_client.model.mbus_agent_device_specific.MbusAgentDeviceSpecific

Specific device for MBUS agents

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict, None,  | frozendict.frozendict, NoneClass,  | Specific device for MBUS agents | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**manufacturer** | None, str,  | NoneClass, str,  |  | [optional] 
**model** | None, str,  | NoneClass, str,  |  | [optional] 
**address** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] 
**secAddress** | None, str,  | NoneClass, str,  |  | [optional] 
**raster** | None, str,  | NoneClass, str,  |  | [optional] 
**maxFail** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 4
**maxRetry** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 3
**sendNke** | None, bool,  | NoneClass, BoolClass,  |  | [optional] if omitted the server will use the default value of False
**appResetSubcode** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] 
**multiFrames** | None, decimal.Decimal, int,  | NoneClass, decimal.Decimal,  |  | [optional] if omitted the server will use the default value of 0
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

