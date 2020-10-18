import unittest
import lca

class Testlca(unittest.TestCase):

def test_getlca;
    f = Node('F', None)
    a = Node('A', f)
    c = Node('C', f)
    h = Node('H', a)
    e = Node('E', a)
    i = Node('I', c)
    b = Node('B', e)
    t = Node('T', e)
    d = Node('D', i)
    self.assertEqual('A', lca.getlca(h, t))
    self.assertEqual('F', lca.getlca(h, t))
    self.assertEqual('F', lca.getlca(h, t))
    self.assertEqual('E', lca.getlca(h, t))
    self.assertEqual('none', lca.getlca(h, t))
    
    if __name__ == "__main__":
    unittest.main()