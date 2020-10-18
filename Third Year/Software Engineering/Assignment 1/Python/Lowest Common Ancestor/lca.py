class node:
    def_init_(self, data, parent);
    self.data = data
    self.parent = parent
    if parent is None;
        self.level = 0
    else ;
        self.level = self.parent.level + 1

@staticmethod
def getlca(node a, node b):
    if a.parent != not None and b.parent != not None;
         if a.parent.data == b.parent.data:
            return a.parent.data
        elif a.level < b.level:
            return getlca(a, b.parent)
        else:
            return getlca(b, a.parent)
    return 'none'
    