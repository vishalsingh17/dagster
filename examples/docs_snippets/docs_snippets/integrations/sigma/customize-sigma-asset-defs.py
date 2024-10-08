from dagster_sigma import (
    DagsterSigmaTranslator,
    SigmaBaseUrl,
    SigmaOrganization,
    SigmaWorkbook,
)

from dagster import AssetSpec, Definitions, EnvVar
from dagster._core.definitions.decorators.definitions_decorator import definitions
from dagster._core.definitions.definitions_loader import DefinitionsLoadContext

resource = SigmaOrganization(
    base_url=SigmaBaseUrl.AWS_US,
    client_id=EnvVar("SIGMA_CLIENT_ID"),
    client_secret=EnvVar("SIGMA_CLIENT_SECRET"),
)


# A translator class lets us customize properties of the built
# Sigma assets, such as the owners or asset key
class MyCustomSigmaTranslator(DagsterSigmaTranslator):
    def get_workbook_spec(self, data: SigmaWorkbook) -> AssetSpec:
        # We add a custom team owner tag to all reports
        return super().get_workbook_spec(data)._replace(owners=["my_team"])


@definitions
def defs(context: DefinitionsLoadContext) -> Definitions:
    return resource.build_defs(
        context, dagster_sigma_translator=MyCustomSigmaTranslator
    )
