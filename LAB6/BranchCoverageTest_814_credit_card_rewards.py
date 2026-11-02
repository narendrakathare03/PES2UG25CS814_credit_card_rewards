
import pytest
from credit_card_rewards import reward_points, late_payment_fee, card_status


# Reward points tests

def test_invalid_card_tier():
    with pytest.raises(ValueError):
        reward_points("diamond", 1000, "grocery", False)


def test_valid_card_tier():
    assert reward_points("classic", 1000, "grocery", False) == 10


def test_invalid_amount():
    with pytest.raises(ValueError):
        reward_points("gold", 0, "grocery", False)


def test_negative_amount():
    with pytest.raises(ValueError):
        reward_points("gold", -100, "grocery", False)


def test_fuel_category():
    assert reward_points("gold", 1000, "fuel", False) == 0


def test_grocery_category():
    assert reward_points("gold", 1000, "grocery", False) == 20


def test_dining_category():
    assert reward_points("gold", 1000, "dining", False) == 40


def test_travel_category():
    assert reward_points("gold", 1000, "travel", False) == 40


def test_weekday_bonus_not_applied():
    assert reward_points("gold", 1000, "grocery", False) == 20


def test_weekend_classic_no_bonus():
    assert reward_points("classic", 1000, "grocery", True) == 10


def test_weekend_gold_bonus():
    assert reward_points("gold", 1000, "grocery", True) == 70


# Late payment fee tests

def test_no_fee_when_not_late():
    assert late_payment_fee(5000, 0) == 0


def test_no_fee_when_outstanding_zero():
    assert late_payment_fee(0, 10) == 0


def test_no_fee_when_outstanding_negative():
    assert late_payment_fee(-500, 10) == 0


def test_fee_for_low_outstanding():
    assert late_payment_fee(500, 10) == 100


def test_fee_at_1000():
    assert late_payment_fee(1000, 10) == 100


def test_fee_for_medium_outstanding():
    assert late_payment_fee(5000, 10) == 500


def test_fee_at_10000():
    assert late_payment_fee(10000, 10) == 500


def test_fee_for_high_outstanding():
    assert late_payment_fee(20000, 10) == 1000


def test_extra_fee_after_30_days():
    assert late_payment_fee(5000, 31) == 1250


def test_no_extra_fee_at_30_days():
    assert late_payment_fee(5000, 30) == 500


# Card status tests

def test_frozen_card():
    assert card_status(50, 0, True) == "frozen"


def test_frozen_card_priority():
    assert card_status(95, 4, True) == "frozen"


def test_blocked_card():
    assert card_status(50, 3, False) == "blocked"


def test_not_blocked_card():
    assert card_status(50, 2, False) == "watch"


def test_over_limit_risk():
    assert card_status(95, 0, False) == "over limit risk"


def test_not_over_limit():
    assert card_status(50, 0, False) == "watch"


def test_watch_due_to_utilisation():
    assert card_status(50, 0, False) == "watch"


def test_watch_due_to_missed_payment():
    assert card_status(20, 1, False) == "watch"


def test_good_card():
    assert card_status(20, 0, False) == "good"
