from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.account_provisioning.v3.models.catalog_entry import CatalogEntry



class AccountProvisioningCatalog:
    def __init__(
            self,
            catalog: Optional[List[CatalogEntry]]=None
    ):
        self.catalog=catalog

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "catalog": self.catalog
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AccountProvisioningCatalog(
            catalog=payload.get('catalog')
        ) 

