from mahjong.shanten import Shanten
from mahjong.hand_calculating.hand import HandCalculator
from mahjong.hand_calculating.hand_config import HandConfig, OptionalRules
from mahjong.meld import Meld

class HaiList:
    # 向聴数の計算用
    def hai34list(tehai):
        hai34list = [0 for i in range(34)]
        for hai in tehai:
            hai34list[hai.kinds * 9 + hai.number] += 1
        return hai34list

    # 点数計算用
    def hai0to135list(tehai):
        hai0to135list = [hai.number0to135 for hai in tehai]
        return hai0to135list

class Rule:

    def shantensuu(tehai):
        shanten = Shanten()
        tiles = HaiList.hai34list(tehai)
        result = shanten.calculate_shanten(tiles)
        return result

    def agari(tehai, dora, tsumo, riichi, jikaze, bakaze):

        calculator = HandCalculator()
        tiles = HaiList.hai0to135list(tehai)
        win = HaiList.hai0to135list([tehai[1]])
        dora_indicators = HaiList.hai0to135list(dora)
        tiles = tiles + win
        win_tile = win[0]
        dora_indicators = None
        melds = None
        config = HandConfig(is_tsumo=tsumo, is_riichi=riichi, player_wind=jikaze, round_wind=bakaze,
                            options=OptionalRules(has_open_tanyao=True))
        tehai_result = calculator.estimate_hand_value(tiles, win_tile, melds, dora_indicators, config)
        return tehai_result