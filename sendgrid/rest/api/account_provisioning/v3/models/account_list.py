from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.account_provisioning.v3.models.account_provisioning_account import (
    AccountProvisioningAccount,
)
from sendgrid.rest.api.account_provisioning.v3.models.account_provisioning_pagination import (
    AccountProvisioningPagination,
)


class AccountList:
    def __init__(
        self,
        accounts: Optional[List[AccountProvisioningAccount]] = None,
        pages: Optional[AccountProvisioningPagination] = None,
    ):
        self.accounts = accounts
        self.pages = pages

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"accounts": self.accounts, "pages": self.pages}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AccountList(accounts=payload.get("accounts"), pages=payload.get("pages"))
