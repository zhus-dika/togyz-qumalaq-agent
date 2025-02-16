import unittest
import sys
sys.path.append('./')
from model_based_approach.TogyzQumalaq.TogyzQumalaqEnv import _get_env

class TestTogyzQumalaqMethods(unittest.TestCase):

    def test_states(self):

        env = _get_env()

        ### Test #1

        acts = [4, 5, 8, 0, 5, 7, 5, 3, 7, 5, 2, 7, 5, 8, 6, 4, 8, 4, 3, 5]

        for act in acts:
            obs, rew, _, _, _ = env.env.last()

            observation = list(obs['observation'])

            env.step(act)

        obs, rew, _, _, _ = env.env.last()
        observation = list(obs['observation'])
        tuzdyq = observation[18:20]
        otaular = observation[:18]
        qazandar = observation[20:22]

        tuzdyq_test = [12, -1]
        otaular_test = [17, 0, 4, 1, 5, 4, 3, 6, 2, 10, 20, 19, 0, 2, 1, 19, 5, 1]
        qazandar_test = [25, 18]

        self.assertEqual(otaular, otaular_test)
        self.assertEqual(tuzdyq, tuzdyq_test)
        self.assertEqual(qazandar, qazandar_test)

        env.reset()

        ### Test #2
        acts = [4, 7, 0, 6, 3, 3, 1, 0, 6, 3]

        for act in acts:
            obs, rew, _, _, _ = env.env.last()

            observation = list(obs['observation'])

            env.step(act)[0]

        obs, rew, _, _, _ = env.env.last()
        observation = list(obs['observation'])
        tuzdyq = observation[18:20]
        otaular = observation[:18]
        qazandar = observation[20:22]

        tuzdyq_test = [-1, 3]
        otaular_test = [4, 3, 14, 0, 6, 15, 1, 14, 14, 2, 14, 14, 1, 14, 3, 3, 4, 13]
        qazandar_test = [20, 3]

        self.assertEqual(otaular, otaular_test)
        self.assertEqual(tuzdyq, tuzdyq_test)
        self.assertEqual(qazandar, qazandar_test)
        env.reset()

        ### Test #3
        acts = [2, 3, 8, 6, 4, 7, 0, 4, 3, 0, 1, 3, 8, 3, 7, 2, 2, 0, 6, 5, 7, 8]

        for act in acts:
            obs, rew, _, _, _ = env.env.last()

            observation = list(obs['observation'])

            env.step(act)[0]

        obs, rew, _, _, _ = env.env.last()
        observation = list(obs['observation'])
        tuzdyq = observation[18:20]
        otaular = observation[:18]
        qazandar = observation[20:22]

        tuzdyq_test = [16, -1]
        otaular_test = [7, 5, 4, 8, 11, 21, 2, 2, 6, 4, 11, 4, 6, 5, 2, 11, 0, 2]
        qazandar_test = [49, 2]

        self.assertEqual(otaular, otaular_test)
        self.assertEqual(tuzdyq, tuzdyq_test)
        self.assertEqual(qazandar, qazandar_test)

    def test__legal_moves(self):
        env = _get_env()

        ### Test #1
        acts = [5, 1, 5, 2, 4, 2, 5, 3, 0, 3]

        for act in acts:
            obs, rew, _, _, _ = env.env.last()

            env.step(act)

        obs, rew, _, _, _ = env.env.last()
        potential_moves = [idx for idx, item in enumerate(obs['action_mask']) if item > 0]
        potential_moves_test = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(potential_moves, potential_moves_test)

        ### Test #2

        env.reset()

        acts = [5, 3, 5, 1, 0, 6, 4, 2, 1, 1, 3, 2, 5, 8, 4, 7, 7, 1, 1, 1]

        for act in acts:
            obs, rew, _, _, _ = env.env.last()

            potential_moves = [idx for idx, item in enumerate(obs['action_mask']) if item > 0]

            env.step(act)
        potential_moves_test = [0, 1, 3, 4, 6, 7, 8]
        self.assertEqual(potential_moves, potential_moves_test)

    def test_check_tuzdyq(self):

        env = _get_env()

        ### Test #1

        acts = [3, 8, 0, 8, 5, 6, 1, 1, 8, 5, 1, 7, 5, 0, 6, 1, 2, 5, 1, 8]

        for act in acts:
            obs, rew, _, _, _ = env.env.last()

            env.step(act)

        obs, rew, _, _, _ = env.env.last()

        observation = list(obs['observation'])

        tuzdyq = observation[18:20]
        tuzdyq_test = [-1, 5]
        self.assertEqual(tuzdyq, tuzdyq_test)

        env.reset()
        ## Test #2

        acts = [7, 7, 1, 0, 4, 4, 3, 7, 1, 8, 0]

        for act in acts:
            obs, rew, _, _, _ = env.env.last()

            env.step(act)

        obs, rew, _, _, _ = env.env.last()

        observation = list(obs['observation'])

        tuzdyq = observation[18:20]
        tuzdyq_test = [13, 6]
        self.assertEqual(tuzdyq, tuzdyq_test)

    def test_check_atsyrau(self):
        env = _get_env()
        ### Test #1
        acts = [6, 2, 5, 8, 3, 0, 8, 4, 1, 5,
                3, 2, 3, 0, 7, 1, 4, 7, 1, 0,
                0, 5, 6, 3, 0, 3, 3, 1, 7, 4,
                8, 0, 4, 1, 6, 2, 4, 1, 2, 8,
                6, 8, 6, 7, 2, 4, 4, 1, 6, 7,
                8, 6, 4, 1, 8, 8, 8, 5, 7, 2,
                3, 2, 2, 4, 0, 1, 6, 0, 8, 1,
                0, 4, 4, 8, 8, 1, 2, 8, 7, 2,
                8, 2, 5, 4, 4, 8, 6, 4, 2, 1,
                7, 0, 5, 5, 6, 8, 2, 2, 2, 1,
                8, 6, 8, 8, 4, 0, 7, 2, 5, 2,
                2, 1, 8, 7, 0, 0, 6, 6, 8, 0,
                6, 7, 5, 2, 3, 0, 2, 2, 7, 2,
                6, 5, 8, 6, 6, 1, 8, 0, 4, 5,
                4, 5, 5, 6, 6, 2, 5, 4, 6, 5,
                3, 1, 4, 1, 5, 2, 7, 6, 8, 0,
                7, 0, 3, 4, 4, 6, 6, 5, 5, 1,
                6, 1, 7, 6, 7, 2, 8, 5, 8, 8,
                0, 8, 0, 2]
        for act in acts:
            obs, rew, _, _, _ = env.env.last()

            env.step(act)

        obs, rew, term, _, _ = env.env.last()

        self.assertTrue(term)

    def test_check_for_winner(self):
        env = _get_env()
        ### Test #1
        acts = [4, 8, 7, 4, 8, 2, 5, 7, 7, 0,
                7, 1, 2, 5, 6, 7, 0, 8, 1, 8,
                5, 0, 1, 1, 8, 0, 6, 0, 3, 3,
                3, 0, 6, 6, 7, 4, 8, 2, 2, 3,
                1, 8, 6, 8, 6, 1, 0, 3, 1, 1,
                5, 2, 7, 6, 1, 1, 7, 8, 0, 2,
                6, 7, 5, 7, 2, 8, 1, 3, 2, 3,
                7, 6, 5, 4, 7, 5, 6, 8, 0, 7,
                5, 8, 7, 4, 2, 5, 7, 1, 6, 2,
                6, 1, 8, 6, 8, 8, 7, 2, 8, 7,
                3, 2, 5, 3, 3, 4, 6, 4, 0, 5,
                7, 3, 2, 5, 3, 1, 2, 6, 8, 6,
                7, 4, 0, 2, 3, 3, 8, 7, 0, 8,
                6, 4, 1, 5, 0, 6, 7, 5, 8, 8,
                0, 6, 2, 7, 2, 7, 0, 8, 1, 8]
        for act in acts:
            obs, rew, _, _, _ = env.env.last()

            env.step(act)

        obs, rew, term, _, _ = env.env.last()

        self.assertTrue(term)

if __name__ == "__main__":
    unittest.main()