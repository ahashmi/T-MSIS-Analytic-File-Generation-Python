{
    "cells": [
        {
            "cell_type": "code",
            "source": ["from taf.OT.OT_Runner import OT_Runner"],
            "metadata": {
                "application/vnd.databricks.v1+cell": {
                    "title": "",
                    "showTitle": false,
                    "inputWidgets": {},
                    "nuid": "05876a53-b24a-4fc2-90b2-0db623cd50cd",
                }
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "metadata": {
                        "application/vnd.databricks.v1+output": {
                            "data": "",
                            "errorSummary": "",
                            "metadata": {},
                            "errorTraceType": null,
                            "type": "ipynbError",
                            "arguments": {},
                        }
                    },
                    "output_type": "display_data",
                    "data": {
                        "text/html": [
                            '<style scoped>\n  .ansiout {\n    display: block;\n    unicode-bidi: embed;\n    white-space: pre-wrap;\n    word-wrap: break-word;\n    word-break: break-all;\n    font-family: "Source Code Pro", "Menlo", monospace;;\n    font-size: 13px;\n    color: #555;\n    margin-left: 4px;\n    line-height: 19px;\n  }\n</style>'
                        ]
                    },
                }
            ],
            "execution_count": 0,
        },
        {
            "cell_type": "code",
            "source": ["from taf.OT.OT_Metadata import OT_Metadata"],
            "metadata": {
                "application/vnd.databricks.v1+cell": {
                    "title": "",
                    "showTitle": false,
                    "inputWidgets": {},
                    "nuid": "a2bc8474-3f18-4592-9d54-3b5558387636",
                }
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "metadata": {
                        "application/vnd.databricks.v1+output": {
                            "data": "",
                            "errorSummary": "",
                            "metadata": {},
                            "errorTraceType": null,
                            "type": "ipynbError",
                            "arguments": {},
                        }
                    },
                    "output_type": "display_data",
                    "data": {
                        "text/html": [
                            '<style scoped>\n  .ansiout {\n    display: block;\n    unicode-bidi: embed;\n    white-space: pre-wrap;\n    word-wrap: break-word;\n    word-break: break-all;\n    font-family: "Source Code Pro", "Menlo", monospace;;\n    font-size: 13px;\n    color: #555;\n    margin-left: 4px;\n    line-height: 19px;\n  }\n</style>'
                        ]
                    },
                }
            ],
            "execution_count": 0,
        },
        {
            "cell_type": "code",
            "source": [
                'otr = OT_Runner(reporting_period = dbutils.widgets.get("reporting_period")\n               ,state_code       = dbutils.widgets.get("state_code")\n               ,run_id           = dbutils.widgets.get("run_id")\n               ,job_id           = dbutils.widgets.get("job_id"))'
            ],
            "metadata": {
                "application/vnd.databricks.v1+cell": {
                    "title": "",
                    "showTitle": false,
                    "inputWidgets": {},
                    "nuid": "1b699995-96a7-4857-a886-ad87a2cfa2c1",
                }
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "metadata": {
                        "application/vnd.databricks.v1+output": {
                            "data": "",
                            "errorSummary": "",
                            "metadata": {},
                            "errorTraceType": null,
                            "type": "ipynbError",
                            "arguments": {},
                        }
                    },
                    "output_type": "display_data",
                    "data": {
                        "text/html": [
                            '<style scoped>\n  .ansiout {\n    display: block;\n    unicode-bidi: embed;\n    white-space: pre-wrap;\n    word-wrap: break-word;\n    word-break: break-all;\n    font-family: "Source Code Pro", "Menlo", monospace;;\n    font-size: 13px;\n    color: #555;\n    margin-left: 4px;\n    line-height: 19px;\n  }\n</style>'
                        ]
                    },
                }
            ],
            "execution_count": 0,
        },
        {
            "cell_type": "code",
            "source": ['otr.job_control_wrt("TOT")'],
            "metadata": {
                "application/vnd.databricks.v1+cell": {
                    "title": "",
                    "showTitle": false,
                    "inputWidgets": {},
                    "nuid": "0d8cdb22-dc20-489f-bf88-ba9c0b408252",
                }
            },
            "outputs": [],
            "execution_count": 0,
        },
        {
            "cell_type": "code",
            "source": ["otr.job_control_updt()"],
            "metadata": {
                "application/vnd.databricks.v1+cell": {
                    "title": "",
                    "showTitle": false,
                    "inputWidgets": {},
                    "nuid": "7044f215-cd2a-4c0a-9f2e-bcb8c9f9f2a1",
                }
            },
            "outputs": [],
            "execution_count": 0,
        },
        {
            "cell_type": "code",
            "source": ["otr.print()"],
            "metadata": {
                "application/vnd.databricks.v1+cell": {
                    "title": "",
                    "showTitle": false,
                    "inputWidgets": {},
                    "nuid": "c2625069-1182-4322-b664-4518d8ab36c4",
                }
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "metadata": {
                        "application/vnd.databricks.v1+output": {
                            "data": "",
                            "errorSummary": "",
                            "metadata": {},
                            "errorTraceType": null,
                            "type": "ipynbError",
                            "arguments": {},
                        }
                    },
                    "output_type": "display_data",
                    "data": {
                        "text/html": [
                            '<style scoped>\n  .ansiout {\n    display: block;\n    unicode-bidi: embed;\n    white-space: pre-wrap;\n    word-wrap: break-word;\n    word-break: break-all;\n    font-family: "Source Code Pro", "Menlo", monospace;;\n    font-size: 13px;\n    color: #555;\n    margin-left: 4px;\n    line-height: 19px;\n  }\n</style>'
                        ]
                    },
                }
            ],
            "execution_count": 0,
        },
        {
            "cell_type": "code",
            "source": ["otr.init()"],
            "metadata": {
                "application/vnd.databricks.v1+cell": {
                    "title": "",
                    "showTitle": false,
                    "inputWidgets": {},
                    "nuid": "027a8f58-bc64-4a8b-88b9-c29b25ab338e",
                }
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "metadata": {
                        "application/vnd.databricks.v1+output": {
                            "data": "",
                            "errorSummary": "",
                            "metadata": {},
                            "errorTraceType": null,
                            "type": "ipynbError",
                            "arguments": {},
                        }
                    },
                    "output_type": "display_data",
                    "data": {
                        "text/html": [
                            '<style scoped>\n  .ansiout {\n    display: block;\n    unicode-bidi: embed;\n    white-space: pre-wrap;\n    word-wrap: break-word;\n    word-break: break-all;\n    font-family: "Source Code Pro", "Menlo", monospace;;\n    font-size: 13px;\n    color: #555;\n    margin-left: 4px;\n    line-height: 19px;\n  }\n</style>'
                        ]
                    },
                }
            ],
            "execution_count": 0,
        },
        {
            "cell_type": "code",
            "source": ["otr.run()"],
            "metadata": {
                "application/vnd.databricks.v1+cell": {
                    "title": "",
                    "showTitle": false,
                    "inputWidgets": {},
                    "nuid": "5d6b7adb-daa7-4231-b08b-c49ad74112f7",
                }
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "metadata": {
                        "application/vnd.databricks.v1+output": {
                            "data": "",
                            "errorSummary": "",
                            "metadata": {},
                            "errorTraceType": null,
                            "type": "ipynbError",
                            "arguments": {},
                        }
                    },
                    "output_type": "display_data",
                    "data": {
                        "text/html": [
                            '<style scoped>\n  .ansiout {\n    display: block;\n    unicode-bidi: embed;\n    white-space: pre-wrap;\n    word-wrap: break-word;\n    word-break: break-all;\n    font-family: "Source Code Pro", "Menlo", monospace;;\n    font-size: 13px;\n    color: #555;\n    margin-left: 4px;\n    line-height: 19px;\n  }\n</style>'
                        ]
                    },
                }
            ],
            "execution_count": 0,
        },
        {
            "cell_type": "code",
            "source": ["otr.view_plan()"],
            "metadata": {
                "application/vnd.databricks.v1+cell": {
                    "title": "",
                    "showTitle": false,
                    "inputWidgets": {},
                    "nuid": "8438ed97-bdef-46d1-942b-33651f3ef749",
                }
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "metadata": {
                        "application/vnd.databricks.v1+output": {
                            "data": "",
                            "errorSummary": "",
                            "metadata": {},
                            "errorTraceType": null,
                            "type": "ipynbError",
                            "arguments": {},
                        }
                    },
                    "output_type": "display_data",
                    "data": {
                        "text/html": [
                            '<style scoped>\n  .ansiout {\n    display: block;\n    unicode-bidi: embed;\n    white-space: pre-wrap;\n    word-wrap: break-word;\n    word-break: break-all;\n    font-family: "Source Code Pro", "Menlo", monospace;;\n    font-size: 13px;\n    color: #555;\n    margin-left: 4px;\n    line-height: 19px;\n  }\n</style>'
                        ]
                    },
                }
            ],
            "execution_count": 0,
        },
        {
            "cell_type": "code",
            "source": ["display(otr.audit())"],
            "metadata": {
                "application/vnd.databricks.v1+cell": {
                    "title": "",
                    "showTitle": false,
                    "inputWidgets": {},
                    "nuid": "238cff62-3b72-4f1b-8768-b5ee22758087",
                }
            },
            "outputs": [
                {
                    "output_type": "display_data",
                    "metadata": {
                        "application/vnd.databricks.v1+output": {
                            "data": "",
                            "errorSummary": "",
                            "metadata": {},
                            "errorTraceType": null,
                            "type": "ipynbError",
                            "arguments": {},
                        }
                    },
                    "output_type": "display_data",
                    "data": {
                        "text/html": [
                            '<style scoped>\n  .ansiout {\n    display: block;\n    unicode-bidi: embed;\n    white-space: pre-wrap;\n    word-wrap: break-word;\n    word-break: break-all;\n    font-family: "Source Code Pro", "Menlo", monospace;;\n    font-size: 13px;\n    color: #555;\n    margin-left: 4px;\n    line-height: 19px;\n  }\n</style>'
                        ]
                    },
                }
            ],
            "execution_count": 0,
        },
        {
            "cell_type": "code",
            "source": ["otr.job_control_updt2()"],
            "metadata": {
                "application/vnd.databricks.v1+cell": {
                    "title": "",
                    "showTitle": false,
                    "inputWidgets": {},
                    "nuid": "7cb8ad65-a4ff-471e-a9bb-bfe66a5ed3fa",
                }
            },
            "outputs": [],
            "execution_count": 0,
        },
        {
            "cell_type": "code",
            "source": [
                'TABLE_NAME = "TAF_OTH"\nFIL_4TH_NODE = "OTH"\n \notr.get_cnt(TABLE_NAME)\notr.getcounts("AWS_OT_MACROS", "1.1 AWS_Extract_Line_OT")\notr.create_meta_info(TABLE_NAME, FIL_4TH_NODE)\notr.create_eftsmeta_info(TABLE_NAME, "AWS_OT_MACROS", "1.1 AWS_Extract_Line_OT", "OT_HEADER", "new_submtg_state_cd")\notr.file_contents(TABLE_NAME)'
            ],
            "metadata": {
                "application/vnd.databricks.v1+cell": {
                    "title": "",
                    "showTitle": false,
                    "inputWidgets": {},
                    "nuid": "2b9d02ed-2e55-48b1-b355-6d5d31d000ab",
                }
            },
            "outputs": [],
            "execution_count": 0,
        },
        {
            "cell_type": "code",
            "source": [
                'TABLE_NAME = "TAF_OTL"\nFIL_4TH_NODE = "OTL"\n \notr.get_cnt(TABLE_NAME)\notr.getcounts("AWS_OT_MACROS", "1.1 AWS_Extract_Line_OT")\notr.create_meta_info(TABLE_NAME, FIL_4TH_NODE)\notr.create_eftsmeta_info(TABLE_NAME, "AWS_OT_MACROS", "1.1 AWS_Extract_Line_OT", "OT_LINE", "new_submtg_state_cd_line")\notr.file_contents(TABLE_NAME)'
            ],
            "metadata": {
                "application/vnd.databricks.v1+cell": {
                    "title": "",
                    "showTitle": false,
                    "inputWidgets": {},
                    "nuid": "9d9d2c85-33d1-4bf4-a1b6-9c90938c0e9f",
                }
            },
            "outputs": [],
            "execution_count": 0,
        },
    ],
    "metadata": {
        "application/vnd.databricks.v1+notebook": {
            "notebookName": "OT Runner",
            "dashboards": [],
            "notebookMetadata": {"pythonIndentUnit": 2},
            "language": "python",
            "widgets": {},
            "notebookOrigID": 467573,
        }
    },
    "nbformat": 4,
    "nbformat_minor": 0,
}