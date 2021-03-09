import random

WORDS = (
    'do', 'deserunt', 'proident', 'tempor', 'voluptate', 'dolor', 'pariatur',
    'culpa', 'fugiat', 'ipsum', 'ullamco', 'ad', 'consequat', 'lorem', 'ut',
    'nulla', 'sunt', 'mollit', 'nisi', 'reprehenderit', 'eu', 'commodo',
    'occaecat', 'quis', 'excepteur', 'et', 'velit', 'id', 'cillum', 'nostrud',
    'enim', 'ea', 'irure', 'aliquip', 'qui', 'consectetur', 'aute',
    'cupidatat', 'laborum', 'labore', 'laboris', 'sed', 'in', 'sit', 'anim',
    'eiusmod', 'veniam', 'adipiscing', 'duis', 'elit', 'dolore', 'est',
    'minim', 'exercitation', 'magna', 'non', 'sint', 'incididunt', 'ex',
    'officia', 'aliqua', 'esse', 'amet')


class TextLorem:
    def __init__(self, wsep=' ', ssep=' ', psep='\n\n', send='.',
                 srange=(4, 8), prange=(5, 10), trange=(3, 6),
                 words=None):
        self._wsep = wsep
        self._ssep = ssep
        self._psep = psep
        self._send = send
        self._srange = srange
        self._prange = prange
        self._trange = trange
        if words:
            self._words = words
        else:
            self._words = WORDS

    def sentence(self):
        n = random.randint(*self._srange)
        s = self._wsep.join(self.word() for _ in range(n))
        return s[0].upper() + s[1:] + self._send

    def paragraph(self):
        n = random.randint(*self._prange)
        p = self._ssep.join(self.sentence() for _ in range(n))
        return p

    def text(self):
        n = random.randint(*self._trange)
        t = self._psep.join(self.paragraph() for _ in range(n))
        return t

    def word(self):
        return random.choice(self._words)
