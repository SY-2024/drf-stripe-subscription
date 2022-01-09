from datetime import datetime
from enum import Enum
from typing import List, Dict, Union, Optional

from pydantic import BaseModel

from .price import StripePrice


class StripeSubscriptionStatus(Enum):
    """See: https://stripe.com/docs/api/subscriptions/object#subscription_object-status"""
    ACTIVE = 'active'
    PAST_DUE = 'past_due'
    UNPAID = 'unpaid'
    CANCELED = 'canceled'
    INCOMPLETE = 'incomplete'
    INCOMPLETE_EXPIRED = 'incomplete_expired'
    TRIALING = 'trialing'
    ENDED = 'ended'


class StripeSubscriptionItemsDataItem(BaseModel):
    """Based on https://stripe.com/docs/api/subscriptions/object#subscription_object-items-data"""
    id: str
    billing_thresholds: Dict = None
    created: datetime
    metadata: Dict
    price: StripePrice
    quantity: int
    subscription: str
    tax_rates: List


class StripeSubscriptionItems(BaseModel):
    """Based on https://stripe.com/docs/api/subscriptions/object#subscription_object-items"""
    data: List[StripeSubscriptionItemsDataItem]
    has_more: bool
    url: str


class StripeSubscription(BaseModel):
    """Based on https://stripe.com/docs/api/subscriptions/object"""
    id: Optional[str]
    cancel_at_period_end: Optional[bool]
    current_period_end: Optional[datetime]
    current_period_start: Optional[datetime]
    customer: Optional[str]
    default_payment_method: Union[str, None]
    items: Optional[StripeSubscriptionItems]
    latest_invoice: Optional[str]
    metadata: Optional[Dict]
    pending_setup_intent: str = None
    pending_update: str = None
    status: Optional[StripeSubscriptionStatus]