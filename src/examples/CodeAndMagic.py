import sys
import math
import itertools
import random
import pandas
import time

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

battle = 0      # switch from drafting to battle
count = 0       # counter for how many turns
output = "PASS"
MANA_GOALS = {
    0: 2,
    1: 3,
    2: 4,
    3: 4,
    4: 3,
    5: 2,
    6: 1,
    7: 1,
    8: 2,
    9: 1,
    12: 0,
    'items': 3
}
CARDS_RANKED = {
    1 : 0.28,
    2 : 0.37,
    3 : 0.38,
    4 : 0.29,
    5 : 0.03,
    6 : -0.05,
    7 : 0.27,
    8 : -0.13,
    9 : -0.07,
    10 : -0.79,
    11 : 0.09,
    12 : -0.15,
    13 : 0.52,
    14 : 0.87,
    15 : -0.01,
    16 : -0.34,
    17 : -0.01,
    18 : 1.21,
    19 : 0.05,
    20 : -0.2,
    21 : 0.13,
    22 : -0.3,
    23 : 0.73,
    24 : -0.12,
    25 : -0.2,
    26 : 0.51,
    27 : 0.16,
    28 : -0.07,
    29 : 0.01,
    30 : 0.63,
    31 : -0.98,
    32 : 0.07,
    33 : 0.13,
    34 : -0.46,
    35 : -1.46,
    36 : -0.27,
    37 : 0.65,
    38 : 1.05,
    39 : 0.64,
    40 : 0.11,
    41 : 0.53,
    42 : -0.74,
    43 : -0.7,
    44 : 0.23,
    45 : -0.96,
    46 : -1.58,
    47 : 1.03,
    48 : 0.41,
    49 : 0.39,
    50 : 0.04,
    51 : 0.51,
    52 : -0.55,
    53 : -1.18,
    54 : -0.53,
    55 : 0.21,
    56 : -0.17,
    57 : -0.25,
    58 : -0.62,
    59 : 0.62,
    60 : -1.54,
    61 : 0.85,
    62 : 0.79,
    63 : 0.61,
    64 : -0.29,
    65 : 0.27,
    66 : -1.51,
    67 : 0.56,
    68 : 0.58,
    69 : 0.83,
    70 : 0.48,
    71 : -0.31,
    72 : -0.09,
    73 : 1.39,
    74 : -0.11,
    75 : 0.46,
    76 : -0.37,
    77 : 0.01,
    78 : -0.33,
    79 : 0.06,
    80 : 1.67,
    81 : -1.64,
    82 : -0.48,
    83 : 1.73,
    84 : 1.36,
    85 : 0.28,
    86 : 0.69,
    87 : 0.75,
    88 : -0.09,
    89 : -0.78,
    90 : -2.03,
    91 : 0.75,
    92 : 0.03,
    93 : 0.39,
    94 : 0.29,
    95 : 0.37,
    96 : 0.45,
    97 : -0.07,
    98 : -0.14,
    99 : 0.35,
    100 : 0.27,
    101 : -0.58,
    102 : -0.51,
    103 : 0.4,
    104 : -0.01,
    105 : -0.03,
    106 : 0.05,
    107 : -0.9,
    108 : -1.16,
    109 : 0.05,
    110 : -0.83,
    111 : 0.11,
    112 : -0.54,
    113 : -1.59,
    114 : 0.17,
    115 : -2.06,
    116 : 0.68,
    117 : 0.45,
    118 : 0.73,
    119 : -0.03,
    120 : -0.01,
    121 : 0.66,
    122 : 0.46,
    123 : 0.36,
    124 : 0.0,
    125 : -0.72,
    126 : -0.48,
    127 : -0.32,
    128 : 0.32,
    129 : -0.17,
    130 : 0.0,
    131 : -0.98,
    132 : -0.45,
    133 : 0.29,
    134 : -0.2,
    135 : 0.52,
    136 : 0.32,
    137 : -0.3,
    138 : -0.46,
    139 : 0.01,
    140 : 0.0,
    141 : 1.19,
    142 : 1.18,
    143 : 0.0,
    144 : -0.09,
    145 : -0.59,
    146 : 0.0,
    147 : 1.15,
    148 : -0.88,
    149 : -0.12,
    150 : -0.62,
    151 : 0.32,
    152 : -1.03,
    153 : 0.23,
    154 : 0.36,
    155 : -0.11,
    156 : -0.06,
    157 : -0.36,
    158 : 0.22,
    159 : -0.06,
    160 : -0.22,
}
CARDS_AVERAGED = {
    1 : 0.78,
    2 : 0.87,
    3 : 0.88,
    4 : 0.72,
    5 : 0.52,
    6 : 0.47,
    7 : 0.71,
    8 : 0.41,
    9 : 0.46,
    10 : -0.03,
    11 : 0.56,
    12 : 0.40,
    13 : 0.83,
    14 : 1.05,
    15 : 0.495,
    16 : 0.29,
    17 : 0.495,
    18 : 1.255,
    19 : 0.53,
    20 : 0.38,
    21 : 0.58,
    22 : 0.325,
    23 : 0.915,
    24 : 0.38,
    25 : 0.4,
    26 : 0.88,
    27 : 0.62,
    28 : 0.45,
    29 : 0.505,
    30 : 0.92,
    31 : -0.16,
    32 : 0.55,
    33 : 0.58,
    34 : 0.23,
    35 : -0.35,
    36 : 0.35,
    37 : 0.88,
    38 : 1.55,
    39 : 1.14,
    40 : 0.58,
    41 : 0.86,
    42 : 0.04,
    43 : 0.09,
    44 : 0.64,
    45 : -0.06,
    46 : -0.38,
    47 : 1.28,
    48 : 0.91,
    49 : 0.795,
    50 : 0.53,
    51 : 0.82,
    52 : 0.16,
    53 : -0.24,
    54 : 0.15,
    55 : 0.655,
    56 : 0.40,
    57 : 0.35,
    58 : 0.14,
    59 : 0.86,
    60 : -0.38,
    61 : 0.97,
    62 : 0.93,
    63 : 0.955,
    64 : 0.29,
    65 : 0.71,
    66 : -0.405,
    67 : 0.83,
    68 : 0.84,
    69 : 1.06,
    70 : 0.80,
    71 : 0.31,
    72 : 0.45,
    73 : 1.37,
    74 : 0.44,
    75 : 0.78,
    76 : 0.29,
    77 : 0.505,
    78 : 0.32,
    79 : 0.54,
    80 : 1.44,
    81 : -0.41,
    82 : 0.23,
    83 : 1.73,
    84 : 1.52,
    85 : 0.69,
    86 : 0.96,
    87 : 0.97,
    88 : 0.45,
    89 : 0.03,
    90 : -0.64,
    91 : 0.75,
    92 : 0.53,
    93 : 0.89,
    94 : 0.72,
    95 : 0.78,
    96 : 0.84,
    97 : 0.46,
    98 : 0.41,
    99 : 0.74,
    100 : 0.68,
    101 : 0.14,
    102 : 0.18,
    103 : 0.8,
    104 : 0.495,
    105 : 0.48,
    106 : 0.53,
    107 : -0.04,
    108 : -0.20,
    109 : 0.53,
    110 : 0.00,
    111 : 0.57,
    112 : 0.19,
    113 : -0.43,
    114 : 0.60,
    115 : -0.66,
    116 : 0.87,
    117 : 0.95,
    118 : 0.73,
    119 : 0.47,
    120 : 0.495,
    121 : 1.00,
    122 : 0.85,
    123 : 0.77,
    124 : 0.5,
    125 : 0.02,
    126 : 0.18,
    127 : 0.29,
    128 : 0.70,
    129 : 0.40,
    130 : 0.5,
    131 : -0.11,
    132 : 0.23,
    133 : 0.68,
    134 : 0.375,
    135 : 0.81,
    136 : 0.32,
    137 : 0.275,
    138 : 0.16,
    139 : 0.505,
    140 : 0.5,
    141 : 1.19,
    142 : 0.64,
    143 : 0.0,
    144 : 0.41,
    145 : 0.105,
    146 : 0.5,
    147 : 1.37,
    148 : -0.16,
    149 : 0.42,
    150 : 0.04,
    151 : 0.99,
    152 : -0.09,
    153 : 0.68,
    154 : 0.77,
    155 : 0.43,
    156 : 0.46,
    157 : 0.26,
    158 : 0.65,
    159 : 0.46,
    160 : 0.34,
    }

BEST_CARDS = [53, 82, 116, 122, 142, 148, 149, 151]
RED_ITEMS = [142, 148, 149, 151]

class Deck:
    def __init__(self):
        self.all_cards = []
        self.creatures = []
        self.gr_items = []
        self.red_items = []
        self.bl_items = []
        self.cards = [self.creatures, self.gr_items, self.red_items, self.bl_items]
        self.mana_list = []
        self.mana_table = self.buildManaTable()
        self.abilities = {
            'B':[],
            'C':[],
            'D':[],
            'G':[],
            'L':[],
            'W':[],
        }
        self.active = []
        self.inactive = []
        self.opponent_cards = []
        self.cards_by_location = [self.inactive, self.active, self.opponent_cards]
        self.nightmares = []
        self.player_deck_strengths =''
        self.op_deck_strengths = ''
        self.summon_combo = []
        self.attack_combo = []
        self.op_card = Card()
        self.my_card = Card()
        print('INIT Deck',file=sys.stderr, flush=True)

    # getter methods 
    def getManaList(self):
        return self.mana_list
    def getSummonCombo(self):
        return self.summon_combo
    def getAttackCombo(self):
        return self.attack_combo
    def getAverageMana(self):
        return sum(self.mana_list)//len(self.mana_list)
    def getCreatures(self):
        return self.cards[0]
    def getMyCard(self):
        return self.my_card
    def getOpCard(self):
        return self.op_card
    def countItems(self):
        count = 0
        for type in self.getItems():
            for i in type:
                count += 1
        return count
    def getItems(self):
        return [self.cards[1], self.cards[2], self.cards[3]]
    def getGreenItems(self):
        return self.cards[1]
    def getRedItems(self):
        return self.cards[2]
    def getBlueItems(self):
        return self.cards[3]
    def getAbilities(self,ability):
        return self.abilities[ability]
    def getAllAbilities(self):
        return self.abilities
    def getPlayerDeckStrengths(self):
        return self.player_deck_strengths
    def getActiveCards(self):
        return self.cards_by_location[1][0::]
    def getOpponentCards(self):
        return self.cards_by_location[-1][0::]
    def getCardsByLocation(self,location):
        return self.cards_by_location[location]
    def getInactiveCards(self):
        return self.cards_by_location[0][0::]
    def getManaTable(self):
        return self.mana_table
    
    #setter methods
    def buildManaTable(self):
        table = {}
        for i in range(13):
            table[i]=0
        return table
    def resetAbilities(self,ability):
        self.abilities[ability]=[]
    def resetAllAbilities(self):
        self.abilities = {
            'B':[],
            'C':[],
            'D':[],
            'G':[],
            'L':[],
            'W':[],
        }
    def moveCard(self, card):
        card.location = 1
        # actives, inactives = [],[]
        # for c in self.active:
        #     actives.append(c.id)
        # for d in self.inactive:
        #     inactives.append(d.id)
        # print(actives, file=sys.stderr, flush=True)
        # print(inactives, file=sys.stderr, flush=True)
        self.active.append(card)
        # actives.append(card.id)
        self.inactive.remove(card)
        # inactives.remove(card.id)
        # print(actives, file=sys.stderr, flush=True)
        # print(inactives, file=sys.stderr, flush=True)
    def addCard(self, card):
        if card not in self.all_cards:
            self.all_cards.append(card)
        self.cards[card.type].append(card)
        self.cards_by_location[card.location].append(card)
        self.mana_list.append(card.cost)
        self.mana_table[card.cost]+=1
        if card.card_number == 116 and card not in self.nightmares:
            self.nightmares.append(card)
    def setOpCard(self, card):
        self.op_card = card
    def setMyCard(self, card):
        self.my_card = card
    def setAbilities(self, ability):
        self.resetAbilities(ability)
        for creature in self.cards[0]:
            if ability in creature.abilities:
                self.abilities[ability].append(creature)
    def setAllAbilities(self):
        abilities = ['B','C','G','D','L','W']
        for a in abilities:
            self.setAbilities(a)
    def setDeckStrengths(self):
        my_strengths = ''
        op_strengths = ''
        for c in self.cards_by_location[1]:
            my_strengths += c.categories
        self.player_deck_strengths = my_strengths
        for o in self.cards_by_location[-1]:
            op_strengths += o.categories
        self.op_deck_strengths = op_strengths
        return my_strengths, op_strengths
    
    def scoreMana_2(self,card_list, mana_table):
        scores = []
        for card in card_list:
            c_score = MANA_GOALS[card.cost] - mana_table[card.cost]
            if card.type>0:
                item_count = self.countItems()
                offset =  item_count - MANA_GOALS['items']
                if offset >= 0:
                    c_score -= offset
                else:
                    c_score -= item_count
            if card.card_number in BEST_CARDS:
                c_score += 2
            scores.append(c_score)
        return scores
        pass
    def draftCard(self, card_list):
        choice = 0
        hi_score = float('-inf')
        mana_table = self.getManaTable()
        print(mana_table, file=sys.stderr, flush=True)
        for i in range(len(card_list)):
            c = card_list[i]
            score = CARDS_AVERAGED[c.card_number]
            goal_score = MANA_GOALS[c.cost] - mana_table[c.cost]
            print('goal score: ',goal_score, file=sys.stderr, flush=True)
            if goal_score < 0:
                score += .5 * goal_score
            if c.type > 0 and self.countItems() > 3:
                score -= .2 * self.countItems()
            print('Card #',c.card_number, ' = ', score, file=sys.stderr, flush=True)
            if score > hi_score:
                choice = i
                hi_score = score
        self.addCard(card_list[choice])
        return choice
        pass


class Player:
    def __init__(self, player_number, player_health=30, player_mana=1, player_deck=30, player_rune=5, player_draw=1):
        self.number = player_number
        self.health = player_health
        self.mana = player_mana
        self.deck_all = []
        self.deck = Deck()
        self.cards_left = player_deck
        self.deck_left = []
        self.rune = player_rune
        self.draw = player_draw
        self.next_draw = self.draw
        self.next_hand_size = 0
        self.mana_spent = 0
        self.next_health = 0
        self.add_health = 0
        self.minus_health = 0
        self.opponent = None
        self.op_cards_left = 0
        self.op_health = 0
        self.op_draw = 0
        self.op_mana = 0
        self.op_rune = 0
        self.op_actions = []
        self.op_hand_size = 0
        self.next_op_health = 0
        self.current_active_cards = []
        self.player_card = Card()
        self.op_card = Card()
        self.current_op_cards = []
    
    def updatePlayer(self, player_number, player_health, player_mana, player_deck, player_rune, player_draw):
        self.number = player_number
        self.health = player_health
        self.mana = player_mana
        self.cards_left = player_deck
        self.rune = player_rune
        self.draw = player_draw

    def resetNextPlayer(self):
        self.next_draw = self.draw
        self.next_hand_size = len(self.deck.inactive)
        self.mana_spent = 0
        self.next_health = self.health
        self.next_op_health = self.op_health
        self.current_active_cards = []
        self.player_card = self.copyCard(self.deck.my_card)
        self.op_card = self.copyCard(self.deck.op_card)
        self.current_op_cards = []
    def resetForBattle(self):
        self.next_health = self.health
        self.next_op_health = self.op_health
    def resetForSummon(self):
        self.add_health = 0
        self.minus_health = 0
        self.next_draw = self.draw
        self.next_hand_size = len(self.deck.inactive)
        self.mana_spent = 0
    def addCard(self, card):
        self.deck.addCard(card)
        pass
    def addDeck(self, deck):
        self.deck = deck
    def updateOpponent(self, op):
        self.op_cards_left = op.cards_left
        self.op_health = op.health
        self.op_mana = op.mana
        self.op_rune = op.rune
        self.op_draw = op.draw
    def __str__ (self):
        return "PLAYER #" + str(self.number) + " // HP: " + str(self.health) + " // MANA: " + str(self.mana) + " // DECK: " + str(self.deck)

    def getOutput(self, start_time, debug = False):
        debug = True
        output = ''
        self.resetNextPlayer()
        mana_total = self.mana
        hi_score = float('-inf')
        cards_in_hand = self.deck.getInactiveCards()
        cards_in_hand_copy = self.copyCardSet(cards_in_hand)
        cards_in_play = self.deck.getActiveCards()
        cards_in_play_copy = self.copyCardSet(cards_in_play)
        op_cards = self.deck.getOpponentCards()
        op_cards_copy = self.copyCardSet(op_cards)
        cards_to_summon = []
        second_summon = []
        best_combo = []
        best_second_combo = []
        summon_perms = self.getSummonPermutations_v2(mana_total, cards_in_play_copy, cards_in_hand_copy, debug)
        if summon_perms:
            summon_count = 1
            for summon_perm, mana_left in summon_perms:
                if not timeElapsed(start_time):
                    print('    ***    summon perm count: ',summon_count, ' *** ', file=sys.stderr, flush=True)
                    self.resetForSummon()
                    self.resetCardSet(cards_in_hand_copy, cards_in_hand)
                    self.resetCardSet(cards_in_play_copy, cards_in_play)
                    self.resetCardSet(op_cards_copy, op_cards)
                    max_count = 8000 // len(summon_perms)
                    cards_left = self.updateSummonPerm(summon_perm, cards_in_hand_copy)
                    cards_for_sim = cards_in_play_copy + summon_perm
                    combo, score = self.simulateAttackTurn(cards_for_sim, op_cards_copy, start_time, max_count, debug)
                    # if mana_left > 0 and not timeElapsed(start_time):
                    #     best_second_combo = []
                    #     hi_2 = float('-inf')
                    #     more_summon_perms = self.getSummonPermutations_v2(mana_left, cards_in_play_copy, cards_left, debug)
                    #     if more_summon_perms:
                    #         for perm_2, mana_left in more_summon_perms:
                    #             self.mana_spent = self.mana - mana_left
                    #             self.next_hand_size -= len(perm_2)
                    #             cih2 = self.updateSummonPerm(perm_2, cards_in_hand_copy)
                    #             c2, s2 = self.simulateAttackTurn(cards_in_play_copy, op_cards_copy, start_time, debug)
                    #             if s2 > hi_2:
                    #                 hi_2 = s2
                    #                 second_summon = perm_2
                    #                 best_second_combo = c2

                    if score > hi_score:
                        hi_score = score
                        cards_to_summon = summon_perm
                        best_combo = combo
                        print('NEW SUMMON PERM HIGH SCORE = ', score, self.printBattle(combo), file=sys.stderr, flush=True)
                    summon_count += 1
        for c in cards_to_summon:
            if c.type == 0:
                output += 'SUMMON ' + str(c.id) + '; '
        output += printAttack(best_combo)
        if second_summon:
            for c in second_summon:
                output += 'SUMMON ' + str(c.id) + '; '
            if best_second_combo:
                output += printAttack(best_second_combo)
        if len(output)<4:
            output = 'PASS'
        return output

    def copyCard(self,orig_card, copy_card = None):
        card = Card()
        if copy_card:
            card = copy_card
        # else: 
        #     print('creating new card', file=sys.stderr, flush=True)
        card.card_number = orig_card.card_number
        card.id = orig_card.id
        card.location = orig_card.location
        card.type = orig_card.type
        card.cost = orig_card.cost
        card.attack = orig_card.attack
        card.defense = orig_card.defense
        card.summoned = orig_card.summoned
        card.waiting = orig_card.waiting
        card.abilities = orig_card.abilities
        card.my_health_change = orig_card.my_health_change
        card.op_health_change = orig_card.op_health_change
        card.card_draw = orig_card.card_draw
        card.dead = orig_card.dead
        card.giveAbilities = orig_card.giveAbilities
        card.takeAbilities = orig_card.takeAbilities
        card.changeAttack = orig_card.changeAttack
        card.changeDefense = orig_card.changeDefense
        card.target_type = orig_card.target_type
        # if card.id == -1:
        #     print('reseting ',card, file=sys.stderr, flush=True)
        return card
    
    def copyCardSet(self,card_list):
        copy_list = []
        for card in card_list:
            copy_list.append(self.copyCard(card))
        return copy_list

    def resetCardSet(self, new_card_set, orig_set):
        for card in new_card_set:
            for o_card in orig_set:
                if card.id == o_card.id:
                    self.copyCard(o_card, card)
                    # print('reseting card# ',card.id, file=sys.stderr, flush=True)
    
    def getManaValue(self,card_list):
        mana_value = 0
        for card in card_list:
            mana_value+=card.cost
        return mana_value
    
    def simulateAttackTurn(self, p_cards, op_cards, start_time, max_count, debug = False):
        debug = False
        simulate_op = False
        op_debug = False
        start = time.time()
        count = 0
        self.player_card = self.copyCard(self.deck.my_card)
        self.current_active_cards = self.copyCardSet(p_cards)
        self.current_op_cards = self.copyCardSet(op_cards)
        self.op_card = self.copyCard(self.deck.op_card)
        best_combo = []
        hi_battle_score = float("-inf")
        possible_combinations = self.getAttackCombinations(self.current_active_cards, self.player_card, self.current_op_cards, self.op_card, start_time, max_count, debug)
        if not possible_combinations:
            hi_battle_score, score_stats = self.getTurnScore(debug)
            print(hi_battle_score, file=sys.stderr, flush=True)
        for perm in possible_combinations:    
            count += 1       
            if timeElapsed(start_time):
                print('out of time: ', time.time()-start, ' count: ',count, file=sys.stderr, flush=True)
                return best_combo, hi_battle_score
            self.resetCardSet(self.current_active_cards, p_cards)
            self.resetCardSet(self.current_op_cards, op_cards)
            self.resetCardSet([self.player_card,self.op_card],[self.deck.my_card,self.deck.op_card])
            self.resetForBattle()
            battle_score, perm_stats, final_combo = self.simulateBattle(perm, self.player_card, self.op_card, self.current_active_cards, self.current_op_cards, debug)
            if debug:
                print(self.printBattle(perm), ' SCORE: ', battle_score, file=sys.stderr, flush=True)
            if simulate_op:
                hi_op_score = -1000
                op_perms = self.getAttackCombinations(self.current_op_cards, self.op_card, self.current_active_cards, self.player_card, start_time, max_count, debug)
                for op_perm in op_perms:
                    op_score, op_stats, op_combo = self.simulateBattle(op_perm, self.op_card, self.player_card, self.current_op_cards, self.current_active_cards, debug)
                    if op_score > hi_op_score:
                        hi_op_score = op_score
                        if op_debug:
                            print("New Op high score = ", hi_op_score,' ', self.printBattle(op_perm), file=sys.stderr, flush=True)
                            for stat in op_stats:
                                print(stat, file=sys.stderr, flush=True)
                if hi_op_score != -1000:
                    battle_score += hi_op_score
            if battle_score > hi_battle_score:
                hi_battle_score = battle_score
                best_combo = final_combo
                # if debug:
                print("New Player high score = ", hi_battle_score, ' ', self.printBattle(best_combo), file=sys.stderr, flush=True)
                for stat in perm_stats:
                    print(stat, file=sys.stderr, flush=True)
        return best_combo, hi_battle_score
    
    def redBattle(self, p, o):
        o.defense += max(p.defense,-o.defense)
        o.attack += max(p.attack,-o.attack)
        for a in p.abilities:
            if a in o.abilities:
                o.abilities.remove(a)
        p.spendItem()
        pass
    def blueBattle(self, p, o):
        o.defense += max(p.defense,-o.defense)
        o.attack += max(p.attack,-o.attack) 
        p.spendItem()
        pass
    def greenBattle(self, p, o):
        o.defense += p.defense
        o.attack += p.attack
        for a in p.abilities:
            if a not in o.abilities:
                o.abilities.append(a)
        p.spendItem()
        pass
    def creatureBattle(self, p, o, player, op, op_cards):
        if o.dead:
            pass
        else:
            guarded = self.isGuardPresent(op_cards)
            p_attack = p.attack
            p_defense = p.defense
            o_attack = min(o.attack, p.defense)
            o_defense = o.defense
            breakthrough = 0
            add_life = 0
            if guarded and "G" not in o.abilities:
                p_attack = 0
                o_attack = 0
            elif o.id != -1:
                if 'L' in p.abilities:
                    # print('L/a',file=sys.stderr, flush=True)
                    p_attack = o_defense
                if 'L' in o.abilities:
                    # print('L/d',file=sys.stderr, flush=True)
                    o_attack = p_defense
                if 'W' in o.abilities and p_attack > 0:
                    # print('W/d',file=sys.stderr, flush=True)
                    p_attack = 0
                    o.abilities.remove('W')
                if 'W' in p.abilities and o_attack >0:
                    # print('W/a',file=sys.stderr, flush=True)
                    o_attack = 0
                    p.abilities.remove('W')
                if 'B' in p.abilities:
                    # print('B',file=sys.stderr, flush=True)
                    breakthrough = max(0, p_attack-o_defense)
            if 'D' in p.abilities:
                # print('D',file=sys.stderr, flush=True)
                add_life = min(p_attack, o_defense)
            
            o.defense -= p_attack
            p.defense -= o_attack
            op.defense -= breakthrough
            player.defense += add_life
            if o.defense <= 0:
                o.defense = 0
                o.dead = True
            if p.defense <= 0:
                p.defense = 0
                p.dead = True
            if p.card_number == 14 and o.card_number == 63:
                print(p, file=sys.stderr, flush=True)
                print(o, file=sys.stderr, flush=True)
    
    def isGuardPresent(self, op_cards):
        guard = False
        for card in op_cards:
            if "G" in card.abilities and not card.dead:
                guard = True
        return guard

    def simulateBattle(self, battle_pairs, p_card, op_card, player_cards, op_cards, debug = False):
        debug = False
        
        final_combo = []
        attack_player = [] # have all cards attack the player afterwards, just in case.
        total_score = 0
        for a_card, d_card in battle_pairs:
            new_pair = []
            # if a_card.card_number == 41:
            #     debug = True
            # else:
            #     debug = False
            if debug:
                print('testing ', a_card.id, ' vs ', d_card.id, file=sys.stderr, flush=True)

            if a_card.type == 1:  #If green item, get a new target, set scores
                self.greenBattle(a_card, d_card)
            elif a_card.type == 2:
                self.redBattle(a_card,d_card)
            elif a_card.type == 3:
                self.blueBattle(a_card, d_card)
            elif not a_card.dead:
                if a_card.attack <= 0 and a_card.location == 1:
                    new_pair = [a_card, op_card]
                    # print('0 Attack Power: ', a_card, file=sys.stderr, flush=True)
                else:
                    self.creatureBattle(a_card,d_card,p_card,op_card, op_cards)
            # else:
            #     print('NO CARD TYPE', file=sys.stderr, flush=True)
            # if debug:
            #     if new_pair:
            #         print(a_card, file=sys.stderr, flush=True)
            #         print(op_card, file=sys.stderr, flush=True)
            #     else:
            #         print(a_card, file=sys.stderr, flush=True)
            #         print(d_card, file=sys.stderr, flush=True)
            if d_card.id != 1 and not new_pair:
                attack_player.append([a_card, op_card])
            if new_pair:
                final_combo.append(new_pair)
            else:
                final_combo.append([a_card, d_card])
        total_score, score_stats = self.getTurnScore(debug)
        # if debug:
        #     cards_used = []
        #     print(self.printBattle(battle_pairs) + 'SCORE: ' + str(total_score), file=sys.stderr, flush=True)
        #     for p,o in battle_pairs:
        #         if p not in cards_used:
        #             cards_used.append(p)
        #         if o not in cards_used:
        #             cards_used.append(o)
        #     for c in cards_used:
        #         print(c, file=sys.stderr, flush=True)
        return total_score, score_stats, final_combo + attack_player

    def printBattle(self, battle_pairs):
        output = 'BATTLE TEST: '
        for a,d in battle_pairs:
            output+= str(a.id) + ' vs ' + str(d.id) + ' // '
        return output

    def getTurnScore(self, debug = False):
        # debug = True
        calc_stats = True
        total_score = 0
        mana_advantage = self.mana_spent - self.op_mana
        hand_size_advantage = self.next_hand_size + self.next_draw - self.op_hand_size - self.op_draw
        board_advantage = 0
        op_board = 0
        player_board = 0
        board_mana_advantage = 0
        op_board_mana = 0
        player_board_mana = 0
        ability_advantage = 0
        op_abilities = 0
        player_abilities = 0
        attack_advantage = 0
        op_attack = 0
        player_attack = 0
        op_d = 0
        player_d = 0
        # for c in self.deck.getInactiveCards():
        #     if c.summoned:
        #         active_player_cards.append(c)
        for op_card in self.current_op_cards:
            if not op_card.dead and op_card.id != -1:
                op_d += op_card.defense 
                op_attack += op_card.attack
                # print('attack power =', op_attack, file=sys.stderr, flush=True)
                op_board += 1
                op_board_mana += op_card.cost
                op_abilities += self.scoreCard(op_card)
                if "G" in op_card.abilities:
                    op_d += op_card.defense * .5
                    if "W" in op_card.abilities:
                        op_d += 2
        for player_card in self.current_active_cards:
            if not player_card.dead and player_card.type == 0:
                player_d += player_card.defense 
                player_attack += player_card.attack
                player_board += 1
                player_board_mana += player_card.cost
                player_abilities += self.scoreCard(player_card)
                if "G" in player_card.abilities:
                    player_d += player_card.defense * .5
                    if "W" in player_card.abilities:
                        player_d += 2
        # print('p_attack: ',player_attack,' op_d: ',op_d, ' op_a: ',op_attack, ' player_d: ',player_d, file=sys.stderr, flush=True)
        attack_advantage = (player_attack - op_d) - (op_attack - player_d)
        board_advantage = player_board - op_board
        # board_mana_advantage = player_board_mana - op_board_mana
        ability_advantage = player_abilities - op_abilities
        health_advantage = self.next_health - self.next_op_health
        advantage_list = [
            mana_advantage,
            hand_size_advantage,
            attack_advantage//2,
            board_advantage,
            board_mana_advantage,
            round(ability_advantage, 2),
            health_advantage
            ]
        total_score = round(sum(advantage_list),2)
        if self.next_op_health <=0:
            total_score += 1000
        advantage_list.append(total_score)
        # uncomment below for debugging:
        score_stats = []
        if calc_stats:
            COLS = ['MANA',' /H_SIZE', ' /ATTK',' /BOARD',' /B_MANA',' /ABLS',' /HLTH',' /TOTAL']
            score_message = ''
            for i in range(len(COLS)):
                score_message += (' '*(len(COLS[i])-len(str(advantage_list[i]))+2)) + str(advantage_list[i]) + '  '
            score_stats = [COLS, score_message]
            if debug: 
                print(COLS, file=sys.stderr, flush=True)
                print(score_message, file=sys.stderr, flush=True)
        return total_score, score_stats
    
    def scoreAbilities(self,abilities):
        points = {
            'B':1,
            'C':0,
            'D':1,
            'G':1,
            'L':1,
            'W':1
        }
        score = 0
        for a in abilities:
            score += points[a]
        return score
    def scoreCard(self,card):
        ability_points = {
            'B':card.attack * .3,
            'C':0,
            'D':card.attack * .7,
            'G':card.defense *.7,
            'L':3,
            'W':card.defense *.5
        }
        score = 0
        for a in card.abilities:
            score += ability_points[a]
        return score
        pass

    def getAttackCombinations(self, p_cards_copy, p_card, all_op_cards, op_card, start_time, max_count = 8000, debug = False):
        debug = True
        start = time.time()
        op_cards_copy = []
        guards = []
        max_combo = max_count // 3
        current_player = 1
        for op in all_op_cards:
            if op.location != -1:
                current_player = -1
                max_count = max_count // 2
                max_combo = max_combo // 2

            if not op.dead:
                if "G" in op.abilities:
                    guards.append(op)
                else:
                    op_cards_copy.append(op)
        green_items = []
        blue_items = []
        red_items = []
        active_creatures = []
        green_targets = []
        blue_targets = [p_card,op_card]+guards + op_cards_copy
        red_targets = guards + op_cards_copy
        creature_targets = guards + op_cards_copy + [op_card]
        for p_card in p_cards_copy:
            if "C" in p_card.abilities:
                print('CHARGER FOUND' , p_card, file=sys.stderr, flush=True)
            if p_card.dead:
                pass
            elif p_card.type == 0:
                if not p_card.waiting:
                    active_creatures.append(p_card)
                green_targets.append(p_card)
            elif p_card.type == 1:
                green_items.append(p_card)
            elif p_card.type == 2:
                red_items.append(p_card)
            else:
                blue_items.append(p_card)
        player_active_count = len(active_creatures)+len(green_items)+len(red_items)+len(blue_items)
        op_count = len(op_cards_copy)+len(guards)+1
        fast = False
        fast_creature_targets = []
        if player_active_count>4 or player_active_count+op_count>=8:
            print('fast battle', file=sys.stderr, flush=True)
            fast = True
        all_perms = []
        if green_items:
            green_perms = list(itertools.permutations(green_items))
            if green_targets:
                green_target_perms = list(itertools.product(green_targets, repeat=len(green_items)))
            else:
                green_target_perms = []
            all_perms.append([green_perms, green_target_perms])
        if blue_items:
            blue_perms = list(itertools.permutations(blue_items))
            blue_target_perms = list(itertools.product(blue_targets, repeat=len(blue_items) ))
            all_perms.append([blue_perms, blue_target_perms])
        if red_items:
            red_perms = list(itertools.permutations(red_items))
            if red_targets:
                red_target_perms = list(itertools.product(red_targets, repeat=len(red_items)))
            else:
                red_target_perms = []
            all_perms.append([red_perms, red_target_perms])
        if active_creatures:
            creature_perms = list(itertools.permutations(active_creatures))
            if fast:
                fast_creature_targets = list(itertools.product([op_card] + guards, repeat=len(active_creatures)))
            creature_target_perms = list(itertools.product(creature_targets, repeat = len(active_creatures)))
            all_perms.append([creature_perms, creature_target_perms])
        all_combos = [] #match each perm set with each possible target

        if fast:
            count = 0
            combo_count = 0
            while combo_count <= max_combo and count <= max_count:
            # while time.time()-start <= timer:
                this_combo = []
                for i in range(len(all_perms)):
                    x_indx = random.randint(0,len(all_perms[i][0])-1)
                    xp = all_perms[i][0][x_indx]
                    if i == len(all_perms)-1 and fast_creature_targets:
                        yp = fast_creature_targets.pop()
                    else:
                        if len(all_perms[i][1])>0:
                            y_indx = random.randint(0,len(all_perms[i][1])-1)
                            yp = all_perms[i][1][y_indx]
                        else:
                            yp = None
                    if yp:
                        pair = []
                        for j in range(len(xp)):
                            pair.append([xp[j], yp[j]])
                            count+=1
                        this_combo += pair
                all_combos.append(this_combo)
                combo_count += 1           
        else:
            combos = []
            for p_perms,o_perms in all_perms:
                perm_section = []
                for p_perm in p_perms:
                    for o_perm in o_perms:
                        combo = []
                        for i in range(len(p_perm)):
                            pair = [p_perm[i],o_perm[i]]
                            combo.append(pair)
                        perm_section.append(combo)
                combos.append(perm_section)
            if combos:
                for i in combos[0]:
                    if len(combos)>1:
                        for j in combos[1]:
                            if len(combos)>2:
                                for k in combos[2]:
                                    if len(combos)>3:
                                        for l in combos[3]:
                                            all_combos.append(i+j+k+l)
                                    else:
                                        all_combos.append(i+j+k)
                            else:
                                all_combos.append(i+j)
                    else:
                        all_combos.append(i)
        if debug:
            print('permuations for player ', current_player,'complete. time elapsed: ', time.time()-start_time, file=sys.stderr, flush=True)
            print('# of combos:  ', len(all_combos), file=sys.stderr, flush=True)
        return all_combos #all combos = [[my_perm1][my_perm2]...]

    def updateSummonPerm(self,summon_perm, cards_in_hand):
        # calculates all effects of summoning a card
        for s in summon_perm:
            self.add_health += s.my_health_change
            self.next_draw += s.card_draw
            self.next_hand_size -= 1
            self.minus_health += s.op_health_change
            self.mana_spent += s.cost
            s.summoned = 1
            if s.type == 0 and 'C' not in s.abilities:
                s.waiting = True
        cards_left = []
        for c in cards_in_hand:
            if c.summoned == 0:
                cards_left.append(c)
        return cards_left
   
    def getSummonPermutations_v2(self, mana, cards_in_play, cards_in_hand, debug = False):
        debug = True
        maxdraft = 6 - len(cards_in_play)
        perms = list(powerset(cards_in_hand))
        best_summons = []
        possibilities = {}
        for perm in perms:
            below_limit = True
            if len(perm)>maxdraft:
                creatures = 0
                for c in perm:
                    if c.type == 0:
                        creatures += 1
                if creatures > maxdraft:
                    below_limit = False
            if below_limit:
                total_cost = 0
                for card in perm:
                    total_cost+= card.cost 
                if total_cost <= mana:
                    possibilities[perm] = total_cost 
        # print(possibilities, file=sys.stderr, flush=True)
        sorted_possibilities = list(sorted(possibilities.items(), key=lambda item: item[1], reverse=True))
        if len(sorted_possibilities)>5:  #Change this to get more summon combos to try
            sorted_possibilities = sorted_possibilities[:5]
        # else:
        #     sorted_possibilities = sorted_possibilities[-1::-1]
        if debug:
            message = '['
            for top in sorted_possibilities:
                for card in top[0]:
                    message+= str(card.id)+ ','
                message += '] score: ' + str(top[1]) + ' // ['
            print(message, file=sys.stderr, flush=True)
        for c,m in sorted_possibilities:
            best_summons.append([list(c), mana - m]) # list of card combos, and manna remaining
        return best_summons

ITEM_LIST = {
    'target_types':[
        'A' # Attacker a>8
        'B' # Bully a>=6, d<=2,
        'G' # Guard,
        'S' # shield d>=6,
        'H' # hero mana>=6,
        'L' # lethal L,
        'W' # weakling, A<=2, mana<=3
        'J' # jack-of-all-trades len(abilities)>=2
        'P' # player
        'Z' # Super Hero
        ],
    117:{
        'giveAbilities' :'B',
        'takeAbilities' :'',
        'changeAttack' : 1,
        'changeDefense' : 1,
        'avoid_types' : '',
        'target_types' : 'ABH'
        },
    118:{
        'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : 3,
        'avoid_types' : 'L',
        'target_types' : 'ABGSHLWJ'
        },
    119:{
        'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 1,
        'changeDefense' : 2,
        'avoid_types' : '',
        'target_types' : 'ABGSHWJ'
    },
    120:{
        'giveAbilities' :'L',
        'takeAbilities' :'',
        'changeAttack' : 1,
        'changeDefense' : 0,
        'avoid_types' : 'L',
        'target_types' : 'GSW'
    },
    121:{
        'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : 3,
        'avoid_types' : 'L',
        'target_types' : 'ABGSHLWJ'
    },
    122:{'giveAbilities' :'G',
        'takeAbilities' :'',
        'changeAttack' : 1,
        'changeDefense' : 3,
        'avoid_types' : '',
        'target_types' : 'ABSHW'},
    123:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 2,
        'changeDefense' : 4,
        'avoid_types' : 'L',
        'target_types' : 'ABGSHWJ'},
    124:{'giveAbilities' :'D',
        'takeAbilities' :'',
        'changeAttack' : 3,
        'changeDefense' : 2,
        'avoid_types' : '',
        'target_types' : 'ABGSHLWJZ'},
    125:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 1,
        'changeDefense' : 4,
        'avoid_types' : 'L',
        'target_types' : 'ABGSHWJ'},
    126:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 2,
        'changeDefense' : 3,
        'avoid_types' : '',
        'target_types' : 'ABGSHWJL'},
    127:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : 6,
        'avoid_types' : 'L',
        'target_types' : 'ABGSHWJL'},
    128:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 4,
        'changeDefense' : 3,
        'avoid_types' : '',
        'target_types' : 'ABGSHWJL'},
    129:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 2,
        'changeDefense' : 5,
        'avoid_types' : 'L',
        'target_types' : 'ABGSHWJL'},
    130:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : 6,
        'avoid_types' : 'L',
        'target_types' : 'ABGSHLJ'},
    131:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 4,
        'changeDefense' : 1,
        'avoid_types' : '',
        'target_types' : 'ABGSHWLJ'},
    132:{'giveAbilities' :'B',
        'takeAbilities' :'',
        'changeAttack' : 3,
        'changeDefense' : 3,
        'avoid_types' : '',
        'target_types' : 'AGBJ'},
    133:{'giveAbilities' :'W',
        'takeAbilities' :'',
        'changeAttack' : 4,
        'changeDefense' : 0,
        'avoid_types' : '',
        'target_types' : 'ABGDSHWLJ'},
    134:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 2,
        'changeDefense' : 2,
        'avoid_types' : '',
        'target_types' : 'ABGSHWLJ'},
    135:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 5,
        'changeDefense' : 5,
        'avoid_types' : 'L',
        'target_types' : 'ABGSHWLJ'},
    136:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 1,
        'changeDefense' : 1,
        'avoid_types' : '',
        'target_types' : 'ABGSHLWJ'},
    137:{'giveAbilities' :'W',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : 0,
        'avoid_types' : '',
        'target_types' : 'ABGSHLJ'},
    138:{'giveAbilities' :'G',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : 0,
        'avoid_types' : 'L',
        'target_types' : 'ASHJ'},
    139:{'giveAbilities' :'LW',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : 0,
        'avoid_types' : '',
        'target_types' : 'ABDGSHWJ'},
    140:{'giveAbilities' :'C',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : 0,
        'avoid_types' : '',
        'target_types' : 'ABSHWLJ'},
    141:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : -1,
        'changeDefense' : -1,
        'avoid_types' : '',
        'target_types' : 'ABGSHLWJ'},
    142:{'giveAbilities' :'',
        'takeAbilities' :'BCDGLW',
        'changeAttack' : 0,
        'changeDefense' : 0,
        'avoid_types' : '',
        'target_types' : 'GJZ'},
    143:{'giveAbilities' :'',
        'takeAbilities' :'G',
        'changeAttack' : 0,
        'changeDefense' : 0,
        'avoid_types' : '',
        'target_types' : 'G'},
    144:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : -2,
        'avoid_types' : '',
        'target_types' : 'ABGHLWJZ'},
    145:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : -2,
        'changeDefense' : -2,
        'avoid_types' : '',
        'target_types' : 'ABGHLWJZ'},
    146:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : -2,
        'changeDefense' : -2,
        'avoid_types' : '',
        'target_types' : 'ABGHLWJZ'},
    147:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : -1,
        'avoid_types' : '',
        'target_types' : 'ABGHLWJZ'},
    148:{'giveAbilities' :'',
        'takeAbilities' :'BCDGLW',
        'changeAttack' : 0,
        'changeDefense' : -2,
        'avoid_types' : '',
        'target_types' : 'JGZ'},
    149:{'giveAbilities' :'',
        'takeAbilities' :'BCDGLW',
        'changeAttack' : 0,
        'changeDefense' : 0,
        'avoid_types' : '',
        'target_types' : 'JGZ'},
    150:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : -3,
        'avoid_types' : '',
        'target_types' : 'ABGHLJ'},
    151:{'giveAbilities' :'',
        'takeAbilities' :'BCDGLW',
        'changeAttack' : 0,
        'changeDefense' : -99,
        'avoid_types' : '',
        'target_types' : 'ZH'},
    152:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : -7,
        'avoid_types' : '',
        'target_types' : 'GSH'},
    153:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : 0,
        'avoid_types' : '',
        'target_types' : 'P'},
    154:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : 0,
        'avoid_types' : '',
        'target_types' : 'P'},
    155:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : -3,
        'avoid_types' : '',
        'target_types' : 'PGB'},
    156:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : 0,
        'avoid_types' : '',
        'target_types' : 'P'},
    157:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : -1,
        'avoid_types' : '',
        'target_types' : 'BLP'},
    158:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : -4,
        'avoid_types' : '',
        'target_types' : 'ABGLHJP'},
    159:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : -3,
        'avoid_types' : '',
        'target_types' : 'ABGLHJP'},
    160:{'giveAbilities' :'',
        'takeAbilities' :'',
        'changeAttack' : 0,
        'changeDefense' : 0,
        'avoid_types' : '',
        'target_types' : 'P'},
}
CATEGORY_TARGETS = {
        'A': 'PJHGD', # Attacker a>8
        'B': 'PHD', # Bully a>=6, d<=2,
        'G': 'PG', # Guard,
        'S': 'WP', # shield d>=6,
        'H': 'PAGJ', # hero mana>=6,
        'L': 'ABGSHJDP', # lethal L,
        'W': 'BLGR', # weakling, A<=2, mana<=3
        'J': 'P', # jack-of-all-trades len(abilities)>=2
        'R':  'P', # has Ward
        'D': 'PWBHLJ', # Destroyer. a>=6, has breakthrough
        'P': '', # player
        'Z': 'PH'
}

CATEGORY_AVOID = {
        'A': 'L', # Attacker a>8
        'B': 'W', # Bully a>=6, d<=2,
        'G': '', # Guard,
        'S': '', # shield d>=6,
        'H': 'L', # hero mana>=6,
        'L': 'W', # lethal L,
        'W': 'D', # weakling, A<=2, mana<=3
        'J': 'L', # jack-of-all-trades len(abilities)>=2
        'R':  'W', # has Ward
        'D': 'L', # Destroyer. a>=6, has breakthrough
        'P': '', # player
        'Z': ''
}

class Card:
    def __init__(self):
        self.card_number = 0  #actual card number, i.e. Turta is #97
        self.id = 0 #instance id, i.e. card #9 on the game board
        self.location = 0 # 0=my hand, 1=my side of board, -1=op side of board
        self.type = 0 # 0: creature, 1: Green item, 2: Red item, 3: Blue item
        self.cost = 0 #cost in mana
        self.attack = 0
        self.defense = 0
        self.summoned = 0
        self.waiting = False
        self.abilities = [] #B: Breakthrough, C: Charge, G: Guard, D: Drain, L: Lethal, W: Ward
        self.my_health_change = 0 
        self.op_health_change = 0
        self.card_draw = 0 #number of extra cards drawn next turn
        self.dead = False
        self.giveAbilities = []
        self.takeAbilities = []
        self.changeAttack = 0
        self.changeDefense = 0
        self.avoid_type = ''
        self.target_type = ''
        self.item_powers = []
        self.categories = ''
        self.targets = []
        self.avoids = []
        self.unique_id = random.random()
        pass
    def __str__(self):
        return "CARD#" + str(self.card_number) + " // ID: " + str(self.id)+ " // LOC: " + str(self.location) + " // TYPE: " + str(self.type) + " // SUMMONED: " + str(self.summoned) + " // WAITING: " + str(self.waiting) +\
            "\n // COST: " + str(self.cost) + " // AT: " + str(self.attack) + " // DEF: " + str(self.defense) + ' // DEAD: ' + str(self.dead) + ' ABLS: ' + str(self.abilities) + ' u_ID: ' + str(self.unique_id)
        # return [self.card_number, self.instance_id, self.location]
    def setAbilities(self,abilities):
        for a in abilities:
            if a != '-':
                self.abilities.append(a)
    def getAbilities(self):
        return self.abilities
    def getCategories(self):
        return self.categories
    def spendItem(self):
        self.location = 2
        self.cost = 0
        self.attack = 0
        self.defense = 0
        self.summoned = 0
        self.my_health_change = 0
        self.op_health_change = 0
        self.abilities = []
        self.changeAttack = 0
        self.changeDefense = 0
        self.dead = True
    def updateCard(self):
        if self.type >=1:
            self.item_powers = self.setItemPowers()
        self.categories = self.setCategory()
        self.targets, self.avoids = self.setTargets()
    def getItemPowers(self):
        return self.item_powers
    def defend(self, attack):
        self.defense -= attack
        if self.defense <= 0:
            self.defense = 0
            self.dead = True
    def getName(self):
        return str(self.id)
    def setItemPowers(self):
        self.giveAbilities = ITEM_LIST[self.card_number]['giveAbilities']
        self.takeAbilities = ITEM_LIST[self.card_number]['takeAbilities']
        self.changeAttack = ITEM_LIST[self.card_number]['changeAttack']
        self.changeDefense = ITEM_LIST[self.card_number]['changeDefense']
        self.avoid_type = ITEM_LIST[self.card_number]['avoid_types']
        self.target_type = ITEM_LIST[self.card_number]['target_types']
        return [self.giveAbilities, self.takeAbilities, self.changeAttack, self.changeDefense, self.target_type]
    def setCategory(self):
        categories = ''
        if self.type > 0:
            return categories
        if self.attack >=8:
            categories += 'A' #Attacker
        if self.attack >=6 and self.defense <= 2:
            categories += 'B' #Bully
        if 'G' in self.abilities:
            categories += 'G' #Guard
        if self.defense >= 6:
            categories += 'S' #Shield
        if self.cost >= 6:
            categories += 'H' #Hero
        if 'L' in self.abilities:
            categories += 'L' #Lethal
        if 'W' in self.abilities:
            categories += 'R' #waRd
        if 'B' in self.abilities and self.attack >= 6:
            categories += 'D' #Destroyer
        if self.attack <= 2 or self.cost <= 3:
            categories += 'W' #Weakling
        if len(self.abilities)>=2:
            categories += 'J' #Jack-of-all-trades
        if self.id in [1,-1]:
            categories += 'P' #Player
        if self.card_number == 116 or self.card_number == 82:
            categories += 'Z' #Zombie Hero
        return categories
    def setTargets(self):
        if self.type > 0:
            return ITEM_LIST[self.card_number]['target_types'], ITEM_LIST[self.card_number]['avoid_types']
        targets = ''
        avoids = ''
        for c in self.categories:
            targets += CATEGORY_TARGETS[c]
            avoids += CATEGORY_AVOID[c]
        self.target_type = targets
        self.avoid_type = avoids
        return targets, avoids

def printAttack(combo_list, summoned=False):
    # print("combo list: ", combo_list, file=sys.stderr, flush=True)
    output = ''
    count = 0
    if summoned:
        output+= ';'
    for combo in combo_list:
        # for a,d in combo:
        a,d = combo[0],combo[1]
        if count > 0:
            output+= ';'
        if a.type ==0:
            output += 'ATTACK ' + a.getName() + ' ' + d.getName()
        else:
            output += 'USE '+ a.getName() + ' ' + d.getName()
        count += 1
    return output
    
def powerset(lyst):
    s = list(lyst)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(1, len(s)+1))

def timeElapsed(start_time):
    if time.time()-start_time > .09:
        print('Time Up!: ', time.time()-start_time, file=sys.stderr, flush=True)
        return True
    # print('time elapsed: ', time.time()-start_time, file=sys.stderr, flush=True)
    return False

def createCard(id, card_number, health, location):
    c = Card()
    c.id = id
    c.card_number = card_number
    c.defense = health
    c.location = location
    return c

my_draft_deck = Deck()
op_draft_deck = Deck()
players = [Player(1),Player(2)]


# game loop
while True:
    opponent_turn=[]
    card_list = []
    for i in range(2):
        player_health, player_mana, player_deck, player_rune, player_draw = [int(j) for j in input().split()]
        players[i].updatePlayer(i+1, player_health, player_mana, player_deck, player_rune, player_draw)
    opponent_hand, opponent_actions = [int(i) for i in input().split()]
    op_actions = []
    for i in range(opponent_actions):
        card_number_and_action = input()
        op_actions.append(card_number_and_action)
    players[0].op_actions = op_actions
    players[0].op_hand_size = opponent_hand
    players[0].updateOpponent(players[1])
    # print(op_actions,  file=sys.stderr, flush=True)
    card_count = int(input())
    cards_input = ''
    for i in range(card_count):
        card = Card()
        inputs = input().split()
        card.card_number = int(inputs[0])
        card.id = int(inputs[1])
        card.location = int(inputs[2])
        card.type = int(inputs[3])
        card.cost = int(inputs[4])
        card.attack = int(inputs[5])
        card.defense = int(inputs[6])
        card.setAbilities(inputs[7])
        card.my_health_change = int(inputs[8])
        card.op_health_change = int(inputs[9])
        card.card_draw = int(inputs[10])
        card.updateCard()
        card_list.append(card)
        cards_input+=str(card.id)+', '

    # print('cards input: ',cards_input, file=sys.stderr, flush=True)

    #update decks for player and opponent
    #update player with decks
    # move simulation methods to player instead of deck

    if count == 30 and battle == 0:
        battle = 1

    if battle == 0:
        choice = my_draft_deck.draftCard(card_list)
        output = "PICK "+str(choice)

    if battle == 1:
        start_time = time.time()
        print('starting process: ', time.time()-start_time, file=sys.stderr, flush=True)
        op_card = createCard(-1, 666, players[1].health, -1)
        p_card = createCard(-1, 777, players[0].health, -1)
        battle_plan = []
        active = False
        my_player, op_player = players[0],players[1]
        output = ''
        my_deck = Deck()
        for card in card_list:
            if card.location == 1:
                active = True
            my_deck.addCard(card)
        my_deck.setMyCard(p_card)
        my_deck.setOpCard(op_card)
        my_player.addDeck(my_deck)
        my_player.updateOpponent(op_player)
        my_player.deck.setDeckStrengths()
        output = my_player.getOutput(start_time, debug=False)
    
    count+=1
    # print("count = " + str(count), file=sys.stderr, flush=True)
    # print(players[0], file=sys.stderr, flush=True)
    # print(opponent_turn, file=sys.stderr, flush=True)
    # print(card_list[0], file=sys.stderr, flush=True)

    print(output)