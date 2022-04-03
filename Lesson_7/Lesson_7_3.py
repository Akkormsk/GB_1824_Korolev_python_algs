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


class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if not node.contains(char):
                node.put(char)
            node = node.get(char)
        node.set_end()

    def search(self, word: str) -> bool:
        node = self.root

        def helper(word, node):
            if node.is_end_flag == True and word == '':
                return True
            if word == '':
                return False
            for char in word:
                if node.contains(char):
                    node = node.get(char)
                    return helper(word[1:], node)
                if char == '.':
                    for link in node.links:
                        if helper(word[1:], node.get(link)) == True:
                            return True
                return False

        return helper(word, node)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)