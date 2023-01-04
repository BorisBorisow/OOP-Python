from unittest import TestCase, main

#from python_oop.exercise.exercise_10_testing.hero.project.hero import Hero
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self):
        self.hero = Hero("Pesho", 1, 50.0, 51.0)
        self.enemy = Hero("Ivo", 1, 25.0, 25.0)

    def test_correct_initializing(self):
        self.assertEqual("Pesho", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(50.0, self.hero.health)
        self.assertEqual(51.0, self.hero.damage)

    def test_battle_when_the_hero_is_the_same_enemy(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_raises_exception_when_health_of_hero_is_zero_or_negative(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_raises_exception_when_health_of_enemy_is_zero_or_negative(self):
        self.enemy.health = 0

        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight Ivo. He needs to rest", str(ve.exception))

    def test_health_remove_after_fight_except_correct_and_fight_is_draw(self):
        self.hero.health = 100
        self.hero.damage = 100
        self.enemy.health = 100
        self.enemy.damage = 100

        result = self.hero.battle(self.enemy)

        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy.health)
        self.assertEqual("Draw", result)

    def test_hero_win_the_battle(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.hero.level)
        self.assertEqual(30, self.hero.health)
        self.assertEqual(56, self.hero.damage)
        self.assertEqual("You win", result)

    def test_enemy_lose_the_battle(self):
        self.hero, self.enemy = self.enemy, self.hero

        result = self.hero.battle(self.enemy)

        self.assertEqual(2, self.enemy.level)
        self.assertEqual(30, self.enemy.health)
        self.assertEqual(56, self.enemy.damage)
        self.assertEqual("You lose", result)

    def test_correct_str(self):
        expected = f"Hero Pesho: 1 lvl\n" \
                   f"Health: 50.0\n" \
                   f"Damage: 51.0\n"
        actual = self.hero.__str__()
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    main()
