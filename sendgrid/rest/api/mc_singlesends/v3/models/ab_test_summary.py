from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.mc_singlesends.v3.models.type import Type
from sendgrid.rest.api.mc_singlesends.v3.models.winner_criteria import WinnerCriteria


class AbTestSummary:
    def __init__(
        self,
        type: Optional[Type] = None,
        winner_criteria: Optional[WinnerCriteria] = None,
        test_percentage: Optional[int] = None,
        duration: Optional[str] = None,
        winning_template_id: Optional[str] = None,
        winner_selected_at: Optional[str] = None,
        expiration_date: Optional[str] = None,
    ):
        self.type = type
        self.winner_criteria = winner_criteria
        self.test_percentage = test_percentage
        self.duration = duration
        self.winning_template_id = winning_template_id
        self.winner_selected_at = winner_selected_at
        self.expiration_date = expiration_date

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "type": self.type,
                "winner_criteria": self.winner_criteria,
                "test_percentage": self.test_percentage,
                "duration": self.duration,
                "winning_template_id": self.winning_template_id,
                "winner_selected_at": self.winner_selected_at,
                "expiration_date": self.expiration_date,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AbTestSummary(
            type=payload.get("type"),
            winner_criteria=payload.get("winner_criteria"),
            test_percentage=payload.get("test_percentage"),
            duration=payload.get("duration"),
            winning_template_id=payload.get("winning_template_id"),
            winner_selected_at=payload.get("winner_selected_at"),
            expiration_date=payload.get("expiration_date"),
        )
