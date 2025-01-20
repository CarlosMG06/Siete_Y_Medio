USE seven_and_half;

INSERT INTO player
VALUES  ('11115555A', 'Mario', True, 2),
		('22226666B', 'Ruben', True, 1),
        ('33337777C', 'BotLine', False, 3),
        ('44448888D', 'TopLane', False, 2);

INSERT INTO deck
VALUES  ('ESP48', 'Baraja Española de 48 cartas'),
		('ESP40', 'Baraja Española de 40 cartas'),
        ('Poker', 'Standard Poker Deck');

INSERT INTO card(id, suit)
VALUES  ('O01', 'Oros'), ('O02', 'Oros'), ('O03', 'Oros'), ('O04', 'Oros'), ('O05', 'Oros'), ('O06', 'Oros'),
        ('O07', 'Oros'), ('O08', 'Oros'), ('O09', 'Oros'), ('O10', 'Oros'), ('O11', 'Oros'), ('O12', 'Oros'),
        ('C01', 'Copas'), ('C02', 'Copas'), ('C03', 'Copas'), ('C04', 'Copas'), ('C05', 'Copas'), ('C06', 'Copas'),
        ('C07', 'Copas'), ('C08', 'Copas'), ('C09', 'Copas'), ('C10', 'Copas'), ('C11', 'Copas'), ('C12', 'Copas'),
        ('E01', 'Espadas'), ('E02', 'Espadas'), ('E03', 'Espadas'), ('E04', 'Espadas'), ('E05', 'Espadas'), ('E06', 'Espadas'),
        ('E07', 'Espadas'), ('E08', 'Espadas'), ('E09', 'Espadas'), ('E10', 'Espadas'), ('E11', 'Espadas'), ('E12', 'Espadas'),
        ('B01', 'Bastos'), ('B02', 'Bastos'), ('B03', 'Bastos'), ('B04', 'Bastos'), ('B05', 'Bastos'), ('B06', 'Bastos'),
        ('B07', 'Bastos'), ('B08', 'Bastos'), ('B09', 'Bastos'), ('B10', 'Bastos'), ('B11', 'Bastos'), ('B12', 'Bastos'),
        
        ('D01', 'Diamonds'), ('D02', 'Diamonds'), ('D03', 'Diamonds'), ('D04', 'Diamonds'), ('D05', 'Diamonds'), ('D06', 'Diamonds'), ('D07', 'Diamonds'), 
        ('D08', 'Diamonds'), ('D09', 'Diamonds'), ('D10', 'Diamonds'), ('D11', 'Diamonds'), ('D12', 'Diamonds'), ('D13', 'Diamonds'),
        ('H01', 'Hearts'), ('H02', 'Hearts'), ('H03', 'Hearts'), ('H04', 'Hearts'), ('H05', 'Hearts'), ('H06', 'Hearts'), ('H07', 'Hearts'), 
        ('H08', 'Hearts'), ('H09', 'Hearts'), ('H10', 'Hearts'), ('H11', 'Hearts'), ('H12', 'Hearts'), ('H13', 'Hearts'), 
        ('S01', 'Spades'), ('S02', 'Spades'), ('S03', 'Spades'), ('S04', 'Spades'), ('S05', 'Spades'), ('S06', 'Spades'), ('S07', 'Spades'),
        ('S08', 'Spades'), ('S09', 'Spades'), ('S10', 'Spades'), ('S11', 'Spades'), ('S12', 'Spades'), ('S13', 'Spades'),
        ('T01', 'Clubs'), ('T02', 'Clubs'), ('T03', 'Clubs'), ('T04', 'Clubs'), ('T05', 'Clubs'), ('T06', 'Clubs'), ('T07', 'Clubs'),
        ('T08', 'Clubs'), ('T09', 'Clubs'), ('T10', 'Clubs'), ('T11', 'Clubs'), ('T12', 'Clubs'), ('T13', 'Clubs');

INSERT INTO deck_card
VALUES  ('O01', 'ESP48'), ('O02', 'ESP48'), ('O03', 'ESP48'), ('O04', 'ESP48'), ('O05', 'ESP48'), ('O06', 'ESP48'),
        ('O07', 'ESP48'), ('O08', 'ESP48'), ('O09', 'ESP48'), ('O10', 'ESP48'), ('O11', 'ESP48'), ('O12', 'ESP48'),
        ('C01', 'ESP48'), ('C02', 'ESP48'), ('C03', 'ESP48'), ('C04', 'ESP48'), ('C05', 'ESP48'), ('C06', 'ESP48'),
        ('C07', 'ESP48'), ('C08', 'ESP48'), ('C09', 'ESP48'), ('C10', 'ESP48'), ('C11', 'ESP48'), ('C12', 'ESP48'),
        ('E01', 'ESP48'), ('E02', 'ESP48'), ('E03', 'ESP48'), ('E04', 'ESP48'), ('E05', 'ESP48'), ('E06', 'ESP48'),
        ('E07', 'ESP48'), ('E08', 'ESP48'), ('E09', 'ESP48'), ('E10', 'ESP48'), ('E11', 'ESP48'), ('E12', 'ESP48'),
        ('B01', 'ESP48'), ('B02', 'ESP48'), ('B03', 'ESP48'), ('B04', 'ESP48'), ('B05', 'ESP48'), ('B06', 'ESP48'),
        ('B07', 'ESP48'), ('B08', 'ESP48'), ('B09', 'ESP48'), ('B10', 'ESP48'), ('B11', 'ESP48'), ('B12', 'ESP48'),
        
        ('O01', 'ESP40'), ('O02', 'ESP40'), ('O03', 'ESP40'), ('O04', 'ESP40'), ('O05', 'ESP40'), ('O06', 'ESP40'),
        ('O07', 'ESP40'), ('O08', 'ESP40'), ('O09', 'ESP40'), ('O10', 'ESP40'),
        ('C01', 'ESP40'), ('C02', 'ESP40'), ('C03', 'ESP40'), ('C04', 'ESP40'), ('C05', 'ESP40'), ('C06', 'ESP40'),
        ('C07', 'ESP40'), ('C08', 'ESP40'), ('C09', 'ESP40'), ('C10', 'ESP40'),
        ('E01', 'ESP40'), ('E02', 'ESP40'), ('E03', 'ESP40'), ('E04', 'ESP40'), ('E05', 'ESP40'), ('E06', 'ESP40'),
        ('E07', 'ESP40'), ('E08', 'ESP40'), ('E09', 'ESP40'), ('E10', 'ESP40'),
        ('B01', 'ESP40'), ('B02', 'ESP40'), ('B03', 'ESP40'), ('B04', 'ESP40'), ('B05', 'ESP40'), ('B06', 'ESP40'),
        ('B07', 'ESP40'), ('B08', 'ESP40'), ('B09', 'ESP40'), ('B10', 'ESP40'),
        
        ('D01', 'Poker'), ('D02', 'Poker'), ('D03', 'Poker'), ('D04', 'Poker'), ('D05', 'Poker'), ('D06', 'Poker'), ('D07', 'Poker'), 
        ('D08', 'Poker'), ('D09', 'Poker'), ('D10', 'Poker'), ('D11', 'Poker'), ('D12', 'Poker'), ('D13', 'Poker'), 
        ('H01', 'Poker'), ('H02', 'Poker'), ('H03', 'Poker'), ('H04', 'Poker'), ('H05', 'Poker'), ('H06', 'Poker'), ('H07', 'Poker'), 
        ('H08', 'Poker'), ('H09', 'Poker'), ('H10', 'Poker'), ('H11', 'Poker'), ('H12', 'Poker'), ('H13', 'Poker'), 
        ('S01', 'Poker'), ('S02', 'Poker'), ('S03', 'Poker'), ('S04', 'Poker'), ('S05', 'Poker'), ('S06', 'Poker'), ('S07', 'Poker'), 
        ('S08', 'Poker'), ('S09', 'Poker'), ('S10', 'Poker'), ('S11', 'Poker'), ('S12', 'Poker'), ('S13', 'Poker'), 
        ('T01', 'Poker'), ('T02', 'Poker'), ('T03', 'Poker'), ('T04', 'Poker'), ('T05', 'Poker'), ('T06', 'Poker'), ('T07', 'Poker'), 
        ('T08', 'Poker'), ('T09', 'Poker'), ('T10', 'Poker'), ('T11', 'Poker'), ('T12', 'Poker'), ('T13', 'Poker');