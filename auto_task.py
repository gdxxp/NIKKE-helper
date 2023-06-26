import time

from auto_player import Player

my_player = Player(accuracy=0.6, adb_mode=False)
my_rough_player = Player(accuracy=0.3, adb_mode=False)


def gain_rewards():
    # 仓库收米
    if my_player.exist(['100%']):
        my_player.find_touch(['lobby', '100%', 'gain_reward', 'click_gain_reward', 'REWARD'])
        time.sleep(2)
    # 友情点
    if my_player.exist(['friend']):
        my_player.find_touch(['friend', 'give', 'confirm'])
        time.sleep(2)
    # 邮箱
    if my_player.exist(['mail']):
        my_player.find_touch(['mail', 'gain_mail', 'lobby'])
        time.sleep(2)
    # 商店每日免费物品
    if my_player.exist(['shop']):
        my_player.find_touch(['shop', '0'])
        time.sleep(2)
        my_player.find_touch(['buy', 'REWARD', 'home', 'home'])
        time.sleep(2)
    # 付费商店每日钻石
    # if my_player.exist(['pay_shop']):
    #     my_player.find_touch(['pay_shop', 'package', 'everyday'])
    # 特殊竞技场收米
    if my_player.exist(['ark']):
        my_player.find_touch(
            ['ark', 'arena', 'special_arena', 'special_arena', 'touch', 'gain_reward_2', 'REWARD', 'home'])
        time.sleep(2)
    # 任务委托收米
    if my_player.exist(['base']):
        my_player.find_touch(['base'])
        time.sleep(4)
        my_player.find_touch(['board', 'gain_all', 'REWARD', 'dispatch_all', 'dispatch', 'home'])


def send_friendship():
    my_player.find_touch(['friend'])
    time.sleep(1)
    my_player.find_touch(['give', 'confirm'])


def simulation_room():
    if my_player.find_touch(['ark']):
        time.sleep(2)
        my_player.find_touch(['simulation_room'])
        time.sleep(2)
        my_player.find_touch(['start_simulation_1'])
        time.sleep(4)
        my_player.find_touch(['start_simulation_2'])
        while True:
            if my_player.exist(['normal_battle']):
                my_player.find_touch(['normal_battle'])
            elif my_player.exist(['hard_battle']):
                my_player.find_touch(['hard_battle'])
            elif my_player.exist(['boss_battle']):
                my_player.find_touch(['boss_battle'])
            elif my_player.exist(['treatment_room']):
                my_player.find_touch(['treatment_room', 'cure', 'confirm'])
                time.sleep(1)
                my_player.find_touch(['confirm'])
            elif my_player.exist(['cure']):
                my_player.find_touch(['cure', 'confirm'])

            if my_player.exist(['quick_battle']):
                my_player.find_touch(['quick_battle'])
            else:
                my_player.find_touch(['enter_battle'])

            time.sleep(1)
            my_player.find_touch(['next_step'])

            if my_player.exist(['EPIC']):
                my_player.find_touch(['EPIC', 'confirm'])
            elif my_player.exist(['SSR']):
                my_player.find_touch(['SSR', 'confirm'])
            else:
                my_player.find_touch(['SR', 'confirm'])

            if my_player.exist(['enter_B']):
                my_player.find_touch(['enter_B'])
            # else:
            #     my_player.find_touch(['enter_C'])

            time.sleep(0.5)


def auto_aim():
    if my_player.exist(['red_circle']):
        my_rough_player.find_touch(['red_circle'])
