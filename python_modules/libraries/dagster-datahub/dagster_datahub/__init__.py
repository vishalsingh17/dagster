from dagster._core.libraries import DagsterLibraryRegistry

from dagster_datahub.resources import (
    DatahubConnection,
    DatahubKafkaEmitterResource,
    DatahubRESTEmitterResource,
    datahub_kafka_emitter,
    datahub_rest_emitter,
)
from dagster_datahub.version import __version__

DagsterLibraryRegistry.register("dagster-datahub", __version__)

__all__ = [
    "datahub_rest_emitter",
    "datahub_kafka_emitter",
    "DatahubKafkaEmitterResource",
    "DatahubConnection",
    "DatahubRESTEmitterResource",
]
