from tests.base_unittest import BaseUnitTest
from pypoker2.engine.card import Card
from pypoker2.engine.hand_evaluator import HandEvaluator

class HandEvaluatorTest(BaseUnitTest):

  def test_eval_high_card(self):
    community = [
        Card(Card.CLUB, 3),
        Card(Card.CLUB, 7),
        Card(Card.CLUB, 10),
        Card(Card.DIAMOND, 5),
        Card(Card.DIAMOND, 6)
        ]
    hole = [
        Card(Card.CLUB, 9),
        Card(Card.DIAMOND, 2)
        ]

    bit = HandEvaluator.eval_hand(hole, community)
    self.eq(HandEvaluator.HIGHCARD, HandEvaluator._HandEvaluator__mask_strength(bit))
    self.eq(9, HandEvaluator._HandEvaluator__high_rank(bit))
    self.eq(2, HandEvaluator._HandEvaluator__low_rank(bit))

  def test_onepair(self):
    community = [
        Card(Card.CLUB, 3),
        Card(Card.CLUB, 7),
        Card(Card.CLUB, 10),
        Card(Card.DIAMOND, 5),
        Card(Card.DIAMOND, 6)
        ]
    hole = [
        Card(Card.CLUB, 9),
        Card(Card.DIAMOND, 3)
        ]

    bit = HandEvaluator.eval_hand(hole, community)
    self.eq(HandEvaluator.ONEPAIR, HandEvaluator._HandEvaluator__mask_strength(bit))
    self.eq(3, HandEvaluator._HandEvaluator__high_rank(bit))
    self.eq(0, HandEvaluator._HandEvaluator__low_rank(bit))

  def test_twopair(self):
    community = [
        Card(Card.CLUB, 7),
        Card(Card.CLUB, 9),
        Card(Card.DIAMOND, 2),
        Card(Card.DIAMOND, 3),
        Card(Card.DIAMOND, 5)
        ]
    hole = [
        Card(Card.CLUB, 9),
        Card(Card.DIAMOND, 3)
        ]

    bit = HandEvaluator.eval_hand(hole, community)
    self.eq(HandEvaluator.TWOPAIR, HandEvaluator._HandEvaluator__mask_strength(bit))
    self.eq(9, HandEvaluator._HandEvaluator__high_rank(bit))
    self.eq(3, HandEvaluator._HandEvaluator__low_rank(bit))

  def test_threecard(self):
    community = [
        Card(Card.CLUB, 3),
        Card(Card.CLUB, 7),
        Card(Card.DIAMOND, 3),
        Card(Card.DIAMOND, 5),
        Card(Card.DIAMOND, 6)
        ]
    hole = [
        Card(Card.CLUB, 9),
        Card(Card.DIAMOND, 3)
        ]

    bit = HandEvaluator.eval_hand(hole, community)
    self.eq(HandEvaluator.THREECARD, HandEvaluator._HandEvaluator__mask_strength(bit))
    self.eq(3, HandEvaluator._HandEvaluator__high_rank(bit))
    self.eq(0, HandEvaluator._HandEvaluator__low_rank(bit))

  def test_straight(self):
    community = [
        Card(Card.CLUB, 3),
        Card(Card.CLUB, 7),
        Card(Card.DIAMOND, 2),
        Card(Card.DIAMOND, 5),
        Card(Card.DIAMOND, 6)
        ]
    hole = [
        Card(Card.CLUB, 4),
        Card(Card.DIAMOND, 5)
        ]

    bit = HandEvaluator.eval_hand(hole, community)
    self.eq(HandEvaluator.STRAIGHT, HandEvaluator._HandEvaluator__mask_strength(bit))
    self.eq(3, HandEvaluator._HandEvaluator__high_rank(bit))
    self.eq(0, HandEvaluator._HandEvaluator__low_rank(bit))

  def test_flash(self):
    community = [
        Card(Card.CLUB, 7),
        Card(Card.DIAMOND, 2),
        Card(Card.DIAMOND, 3),
        Card(Card.DIAMOND, 5 ),
        Card(Card.DIAMOND, 6)
        ]
    hole = [
        Card(Card.CLUB, 4),
        Card(Card.DIAMOND, 5)
        ]

    bit = HandEvaluator.eval_hand(hole, community)
    self.eq(HandEvaluator.FLASH, HandEvaluator._HandEvaluator__mask_strength(bit))
    self.eq(6, HandEvaluator._HandEvaluator__high_rank(bit))
    self.eq(0, HandEvaluator._HandEvaluator__low_rank(bit))

  def test_fullhouse(self):
    community = [
        Card(Card.CLUB, 4),
        Card(Card.DIAMOND, 2),
        Card(Card.DIAMOND, 4),
        Card(Card.DIAMOND, 5 ),
        Card(Card.DIAMOND, 6)
        ]
    hole = [
        Card(Card.CLUB, 4),
        Card(Card.DIAMOND, 5)
        ]

    bit = HandEvaluator.eval_hand(hole, community)
    self.eq(HandEvaluator.FULLHOUSE, HandEvaluator._HandEvaluator__mask_strength(bit))
    self.eq(4, HandEvaluator._HandEvaluator__high_rank(bit))
    self.eq(5, HandEvaluator._HandEvaluator__low_rank(bit))

  def test_straightflash(self):
    community = [
        Card(Card.DIAMOND, 4),
        Card(Card.DIAMOND, 5),
        Card(Card.HEART, 11),
        Card(Card.HEART, 12),
        Card(Card.HEART, 13)
        ]
    hole = [
        Card(Card.HEART, 10),
        Card(Card.HEART, 1)
        ]

    bit = HandEvaluator.eval_hand(hole, community)
    self.eq(HandEvaluator.STRAIGHTFLASH, HandEvaluator._HandEvaluator__mask_strength(bit))
    self.eq(10, HandEvaluator._HandEvaluator__high_rank(bit))
    self.eq(0, HandEvaluator._HandEvaluator__low_rank(bit))

