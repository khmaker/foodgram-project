import random

WORDS = (
    'dolor', 'molestiae', 'a', 'vero', 'harum', 'qui', 'fugiat', 'atque',
    'provident', 'voluptate', 'non', 'voluptatum', 'unde', 'dolorem',
    'laudantium', 'neque', 'iusto', 'ipsa', 'ea', 'ullam', 'cupiditate',
    'labore', 'vitae', 'dicta', 'sequi', 'modi', 'quam', 'quo', 'autem',
    'repudiandae', 'aliquam', 'ipsum', 'enim', 'at', 'nisi', 'in', 'doloribus',
    'accusantium', 'nihil', 'mollitia', 'corporis', 'eveniet', 'et',
    'consectetur', 'ducimus', 'consequuntur', 'libero', 'sint', 'error',
    'eligendi', 'tenetur', 'placeat', 'adipisci', 'delectus', 'saepe',
    'necessitatibus', 'hic', 'corrupti', 'odio', 'sunt', 'magnam', 'excepturi',
    'consequatur', 'distinctio', 'praesentium', 'illo', 'laboriosam', 'illum',
    'tempore', 'architecto', 'repellat', 'tempora', 'odit', 'minima', 'vel',
    'itaque', 'ab', 'culpa', 'rerum', 'expedita', 'veritatis', 'asperiores',
    'magni', 'iure', 'rem', 'soluta', 'debitis', 'cumque', 'sit', 'recusandae',
    'porro', 'repellendus', 'perspiciatis', 'facere', 'suscipit', 'voluptatem',
    'molestias', 'voluptates', 'ratione', 'maxime', 'ad', 'explicabo', 'nulla',
    'ut', 'amet', 'assumenda', 'alias', 'quae', 'est', 'velit', 'animi',
    'omnis', 'numquam', 'totam', 'natus', 'quia', 'aspernatur', 'id', 'eius',
    'iste', 'fugit', 'sapiente', 'quidem', 'ipsam', 'pariatur', 'quod',
    'quibusdam', 'eum', 'earum', 'voluptas', 'sed', 'nam', 'quos', 'deleniti',
    'accusamus', 'similique', 'laborum', 'minus', 'esse', 'exercitationem',
    'nostrum', 'doloremque', 'quisquam', 'nobis', 'commodi', 'quasi', 'cum',
    'officiis', 'perferendis', 'maiores', 'reiciendis', 'obcaecati', 'veniam',
    'inventore', 'quis', 'dolores', 'quaerat', 'dignissimos', 'quas', 'beatae',
    'voluptatibus', 'impedit', 'aliquid', 'ex', 'possimus', 'deserunt',
    'incidunt', 'aperiam', 'dolore', 'temporibus', 'facilis', 'reprehenderit',
    'eos', 'optio', 'blanditiis', 'eaque', 'nesciunt', 'officia', 'fuga',
    'nemo', 'aut', 'dolorum')


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
