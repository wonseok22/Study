import sys
input = sys.stdin.readline


def is_strightflush():
    if not can_flush:
        return False

def is_quads():
    if can_quads == 0:
        return False
    return can_quads

def is_title():


def is_flush():
    if not can_flush:
        return False

def is_straight():


def is_triple():


def is_twopair():


def is_onepair():



card = [[],[]]

for _ in range(4):
    a,b = map(int,input().split())
    card[0].append(a)
    card[1].append(b)
can_flush = card[0].count(card[0][0]) == 4
can_quads = 0
can_title = 0
if card[1].count(card[1][0]) >= 3:
    can_quads = card[1][0]
elif card[1].count(card[1][1]) >= 3:
    can_quads = card[1][1]
s_card = sorted(card[1])
if s_card[0] == s_card[1] and s_card[1]


