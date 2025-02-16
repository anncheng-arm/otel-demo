from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.exporter.otlp.proto.grpc.metric_exporter import OTLPMetricExporter
from opentelemetry.metrics import get_meter_provider, set_meter_provider, Observation
import random
import time


resource = Resource.create({"service.name": "bmc_temperature_monitor"})
exporter = OTLPMetricExporter(endpoint="http://localhost:4317", insecure=True)
reader = PeriodicExportingMetricReader(exporter)
provider = MeterProvider(metric_readers=[reader], resource=resource)
set_meter_provider(provider)
meter = get_meter_provider().get_meter("bmc.monitor")


def get_cpu_temp(callback_options):
    return [Observation(random.randint(30, 60))]

def get_ambient_temp(callback_options):
    return [Observation(random.randint(30, 60))]


cpu_temp = meter.create_observable_gauge(
    "host_cpu_temperature",
    unit="C",
    callbacks=[get_cpu_temp],
    description="Host CPU Temperature in Celsius"
)

ambient_temp = meter.create_observable_gauge(
    "host_ambient_temperature",
    unit="C",
    callbacks=[get_ambient_temp],
    description="Host Ambient Temperature in Celsius"
)

print("BMC Metrics Collection Started...")
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    print("\nStopping BMC Metrics Collection.")
