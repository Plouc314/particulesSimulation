import unittest
import lib.simulation.cppSimulation as simul

class TestSimul(unittest.TestCase):

    def test_particule(self):

        # test init with 4 floats
        p = simul.Particule(1.23, 4.35, -3.45, 6.677)

        self.assertAlmostEqual(p.pos[0], 1.23, places=3)
        self.assertAlmostEqual(p.pos[1], 4.35, places=3)
        self.assertAlmostEqual(p.q, -3.45, places=3)

        try:
            pos = p.pos
            v = p.v
            a = p.a
        except Exception as e:
            self.fail(str(e))

        self.assertIs(type(p.v), list)

    def test_constants(self):

        c = simul.Constants()

        self.assertAlmostEqual(c.e, 8.85e-12, places=4)
        self.assertAlmostEqual(c.masse_proton, 1.6726e-27, places=4)

        c.e = 2
        self.assertEqual(2, c.e)
        
        c.k = 3
        self.assertEqual(3, c.k)

    def test_system(self):
        
        # create particules
        particules = [
            simul.Particule(0,0,1,1),
            simul.Particule(0,1,1,1),
        ]
        
        # create system
        system = simul.System(particules, 1)

        # override constants
        system.constants.k = 1

        system.update()

        p1, p2 = system.particules
        self.assertEqual(p1.pos[1], -1)
        self.assertEqual(p2.pos[1], 2)

        # test particule reference
        p = system.particules[0]
        p.pos = [0, 10]
        self.assertEqual(system.particules[0].pos, p.pos)

if __name__ == "__main__":
    unittest.main()