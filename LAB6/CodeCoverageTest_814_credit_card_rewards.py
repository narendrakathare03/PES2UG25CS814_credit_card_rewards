
from credit_card_rewards import reward_points, late_payment_fee, card_status


def test_classic_grocery():
    assert reward_points("classic", 1000, "grocery", False) == 10


def test_gold_grocery():
    assert reward_points("gold", 1000, "grocery", False) == 20


def test_platinum_grocery():
    assert reward_points("platinum", 1000, "grocery", False) == 40


def test_fuel():
    assert reward_points("gold", 1000, "fuel", False) == 0


def test_dining():
    assert reward_points("gold", 1000, "dining", False) == 40


def test_travel():
    assert reward_points("platinum", 1000, "travel", False) == 80


def test_weekend_bonus():
    assert reward_points("gold", 1000, "grocery", True) == 70


def test_invalid_card():
    try:
        reward_points("diamond", 1000, "grocery", False)
        assert False
    except ValueError:
        assert True


def test_invalid_amount():
    try:
        reward_points("gold", 0, "grocery", False)
        assert False
    except ValueError:
        assert True


def test_late_payment_no_fee():
    assert late_payment_fee(5000, 0) == 0


def test_late_payment_100():
    assert late_payment_fee(500, 10) == 100


def test_late_payment_500():
    assert late_payment_fee(5000, 10) == 500


def test_late_payment_1000():
    assert late_payment_fee(20000, 10) == 1000


def test_late_payment_extra():
    assert late_payment_fee(5000, 31) == 1250


def test_frozen_card():
    assert card_status(50, 0, True) == "frozen"


def test_blocked_card():
    assert card_status(50, 3, False) == "blocked"


def test_over_limit():
    assert card_status(95, 0, False) == "over limit risk"


def test_watch_utilisation():
    assert card_status(50, 0, False) == "watch"


def test_watch_missed_payment():
    assert card_status(20, 1, False) == "watch"


def test_good_card():
    assert card_status(20, 0, False) == "good"
