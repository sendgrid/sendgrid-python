from enum import Enum
from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from enum import Enum
from sendgrid.rest.api.account_provisioning.v3.models.account_provisioning_offering_v1 import AccountProvisioningOfferingV1
from sendgrid.rest.api.account_provisioning.v3.models.catalog_entry_entitlements import CatalogEntryEntitlements



class CatalogEntry:
    def __init__(
            self,
            offering: Optional[AccountProvisioningOfferingV1]=None,
            entitlements: Optional[CatalogEntryEntitlements]=None
    ):
        self.offering=offering
        self.entitlements=entitlements

    def to_dict(self):
        return {key: to_serializable(value)
            for key, value in {
            "offering": self.offering,
            "entitlements": self.entitlements
            }.items() if value is not None}

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return CatalogEntry(
            offering=payload.get('offering'),
            entitlements=payload.get('entitlements')
        ) 

