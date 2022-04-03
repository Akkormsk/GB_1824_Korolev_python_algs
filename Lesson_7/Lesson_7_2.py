class Node:
    def __init__(self):
        self.links = dict()
        self.is_end_flag = False

    def contains(self, char):
        return char in self.links

    def put(self, char):
        self.links[char] = Node()

    def get(self, char):
        return self.links[char]

    def set_end(self):
        self.is_end_flag = True


class Tree:
    def __init__(self):
        self.root = Node()

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if node.contains(char):
                node = node.get(char)
            else:
                return None
        return node

    def insert(self, word):
        node = self.root
        for char in word:
            if not node.contains(char):
                node.put(char)
            node = node.get(char)
        node.set_end()

    def is_pref(self, word):
        pref = ''
        node = self.root
        for char in word:
            if node.is_end_flag:
                return pref
            if not node.contains(char):
                return None
            node = node.get(char)
            pref += char


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        t = Tree()
        sen_list = sentence.split(' ')
        for pref in dictionary:
            t.insert(pref)
            for i, word in enumerate(sen_list):
                if t.is_pref(word):
                    sen_list[i] = pref
        return ' '.join(sen_list)
