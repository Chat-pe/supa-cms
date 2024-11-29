from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional, Literal
from src.plans.schemas import CountryCurrencyPrice

# Request DTOs
class CreatePlanDTO(BaseModel):
    uniquelink: str
    name: str
    id_alias: dict[str, str]
    metadata: dict[str, str | bool]
    checkout_link: str
    description: str
    max_allowed_members: int
    period: int
    plan_level: int
    features: dict
    default_price: CountryCurrencyPrice
    price: List[CountryCurrencyPrice]
    is_trial: Optional[bool] = False
    is_monthly: Optional[bool] = True
    status: Optional[Literal["active", "inactive"]] = "inactive"

class UpdatePlanDTO(BaseModel):
    name: Optional[str]
    id_alias: Optional[dict[str, str]]
    metadata: Optional[dict[str, str | bool]]
    checkout_link: Optional[str]
    description: Optional[str]
    max_allowed_members: Optional[int]
    period: Optional[int]
    plan_level: Optional[int]
    features: Optional[dict]
    price: Optional[List[CountryCurrencyPrice]]
    default_price: Optional[CountryCurrencyPrice]
    is_trial: Optional[bool]
    is_monthly: Optional[bool]
    status: Optional[Literal["active", "inactive"]]

# Response DTOs
class PlanResponseDTO(BaseModel):
    
    uniquelink: str
    name: str
    id_alias: dict[str, str]
    metadata: dict[str, str | bool]
    checkout_link: str
    description: str
    max_allowed_members: int
    period: int
    plan_level: int
    features: dict
    price: List[CountryCurrencyPrice]
    default_price: CountryCurrencyPrice
    is_trial: bool
    is_monthly: bool
    status: Literal["active", "inactive"]
    created_at: datetime
    updated_at: datetime

class PlansListResponseDTO(BaseModel):
    plans: List[PlanResponseDTO]
    total: int

class DeletePlanResponseDTO(BaseModel):
    message: str
    deleted_plan_id: str
