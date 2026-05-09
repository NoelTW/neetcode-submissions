class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        
        hand.sort()
        counter = Counter(hand)

        for start_card in hand:
            if counter[start_card]:
                for card in range(start_card, start_card + groupSize):
                    if counter[card] > 0:
                        counter[card] -= 1
                    else:
                        return False
        return True