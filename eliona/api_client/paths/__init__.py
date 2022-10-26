# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from eliona.api_client.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    VERSION = "/version"
    APPS_APPNAME = "/apps/{app-name}"
    APPS_APPNAME_PATCHES_PATCHNAME = "/apps/{app-name}/patches/{patch-name}"
    ASSETTYPES = "/asset-types"
    ASSETTYPES_ASSETTYPENAME = "/asset-types/{asset-type-name}"
    ASSETTYPES_ASSETTYPENAME_ATTRIBUTES = "/asset-types/{asset-type-name}/attributes"
    ASSETS = "/assets"
    ASSETS_ASSETID = "/assets/{asset-id}"
    DATA = "/data"
    DATATRENDS = "/data-trends"
    DATALISTENER = "/data-listener"
    DATAAGGREGATED = "/data-aggregated"
    AGGREGATIONS = "/aggregations"
    AGGREGATIONS_AGGREGATIONID = "/aggregations/{aggregation-id}"
    WIDGETTYPES = "/widget-types"
    WIDGETTYPES_WIDGETTYPENAME = "/widget-types/{widget-type-name}"
    DASHBOARDS = "/dashboards"
    DASHBOARDS_DASHBOARDID = "/dashboards/{dashboard-id}"
    DASHBOARDS_DASHBOARDID_WIDGETS = "/dashboards/{dashboard-id}/widgets"
    ALARMRULES = "/alarm-rules"
    ALARMRULES_ALARMRULEID = "/alarm-rules/{alarm-rule-id}"
    ALARMS = "/alarms"
    ALARMS_ALARMRULEID = "/alarms/{alarm-rule-id}"
    ALARMSHISTORY = "/alarms-history"
    ALARMSHISTORY_ALARMRULEID = "/alarms-history/{alarm-rule-id}"
    ALARMSHIGHEST = "/alarms-highest"
    NODES = "/nodes"
    NODES_NODEIDENT = "/nodes/{node-ident}"
    AGENTS = "/agents"
    AGENTS_AGENTCLASS = "/agents/{agent-class}"
    AGENTS_AGENTCLASS_AGENTID_DEVICES = "/agents/{agent-class}/{agent-id}/devices"
    AGENTDEVICES_AGENTCLASS_AGENTDEVICEID_MAPPINGS = "/agent-devices/{agent-class}/{agent-device-id}/mappings"
