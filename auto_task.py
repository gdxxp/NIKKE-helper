import time

from auto_player import Player

my_player = Player(accuracy=0.8, adb_mode=False)


def change_accuracy(new_accuracy):
    my_player.change_accuracy(new_accuracy)


def change_interval(new_interval):
    my_player.change_interval(new_interval)


def gain_rewards():

    # 仓库收米
    if my_player.exist(['100%']):
        destroy_item(my_player, '100%')
    elif my_player.exist(['no100%']):
        destroy_item(my_player, 'no100%')
    # 友情点
    if my_player.exist(['friend']):
        my_player.find_touch(['friend', 'give', 'confirm', 'close', 'lobby'])
    # 邮箱
    if my_player.exist(['mail']):
        my_player.find_touch(['mail', 'gain_mail', 'REWARD', 'close_3', 'lobby'])
    # 商店每日免费物品
    if my_player.exist(['shop']):
        my_player.find_touch(['shop', '0'])
        time.sleep(3.5)
        my_player.find_touch(['buy', 'REWARD', 'home', 'home'])
        time.sleep(my_player.interval)
    # 付费商店每日,每周,每月钻石
    if my_player.exist(['pay_shop']):
        my_player.find_touch(['pay_shop', 'gift'])
        time.sleep(my_player.interval)

        if my_player.exist(['everymonth']):
            claim_free_diamond(my_player, ['everymonth'])

        if my_player.exist(['everyweek']):
            claim_free_diamond(my_player, ['everyweek'])

        claim_free_diamond(my_player, ['everyday'])

        my_player.find_touch(['home'])
    # 特殊竞技场收米
    if my_player.exist(['ark']):
        my_player.find_touch(
            ['ark', 'arena', 'arena', 'special_arena', 'special_arena', 'touch', 'gain_reward_2', 'REWARD', 'home'])
        time.sleep(my_player.interval)
    # 任务委托收米
    if my_player.exist(['base']):
        my_player.find_touch(['base'])
        time.sleep(5.5)
        my_player.find_touch(['board', 'gain_all', 'REWARD', 'dispatch_all', 'dispatch', 'home', 'home'])
        time.sleep(5)
    # 日常任务
    if my_player.exist(['mission']):
        my_player.find_touch(['mission', 'gain_all_2', 'gain_all_2', 'REWARD', 'close_2'])
    # pass
    if my_player.exist(['friend']):
        my_player.find_touch_skewing(['friend'], 270, 50)
        my_player.find_touch(['mission_2', 'gain_all_3'])
        if my_player.exist(['rank_up_2']):
            my_player.find_touch_skewing(['rank_up_2'], 270, 80)
            my_player.find_touch(['gain_all_3'])
        my_player.find_touch(['friend'])
    # 露菲弹窗广告
    if my_player.exist(['ad']):
        my_player.find_touch(['ad', 'confirm_2'])


def recruit():
    my_player.find_touch_same_screen(['recruit_one', 'skip', 'confirm_3'])


def simulation_room():
    if my_player.exist(['ark']):
        my_player.find_touch(['ark', 'simulation_room', 'simulation_room', 'start_simulation_1'])
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
            my_player.find_touch(['treatment_room', 'cure', 'confirm_5', 'confirm_5'])
        elif my_player.exist(['cure']):
            my_player.find_touch(['cure', 'confirm_5', 'confirm_5'])

        if my_player.exist(['quick_battle']):
            my_player.find_touch(['quick_battle'])
        elif my_player.exist(['enter_battle']):
            my_player.find_touch(['enter_battle'])

        if my_player.exist(['next_step']):
            my_player.find_touch(['next_step'])

        if my_player.exist(['EPIC']):
            my_player.find_touch(['EPIC', 'confirm_7', 'confirm_4'])
        elif my_player.exist(['SSR']):
            my_player.find_touch(['SSR', 'confirm_7', 'confirm_4'])
        elif my_player.exist(['SR']):
            my_player.find_touch(['SR', 'confirm_7', 'confirm_4'])
        elif my_player.exist(['R']):
            my_player.find_touch(['R', 'confirm_7', 'confirm_4'])

        if my_player.exist(['enter_B']):
            my_player.find_touch(['enter_B'])
        elif my_player.exist(['enter_C']):
            my_player.find_touch(['enter_C'])
        elif my_player.exist(['end_simulation']):
            my_player.find_touch(['end_simulation'])
            break


def auto_consult():
    if my_player.exist(['nikke']):
        my_player.find_touch(['nikke', 'consult'])
    if my_player.exist(['nikke_consult']):
        my_player.find_touch(['nikke_consult', 'consult_2', 'confirm_6', 'auto'])
    if my_player.exist(['consult_option']):
        my_player.find_touch(['consult_option', 'skip', 'back'])
    if my_player.exist(['rank_up']):
        my_player.find_touch(['rank_up', 'back'])


def auto_arena():
    if my_player.exist(['ark']):
        my_player.find_touch(['ark', 'arena', 'arena', 'rookie_arena'])
    if my_player.exist(['rookie_arena']):
        my_player.find_touch(['rookie_arena'])
    if my_player.exist(['enter_battle_2']):
        my_player.find_touch_skewing(['enter_battle_2'], 90, 163)
        my_player.find_touch(['enter_battle_3'])
    if my_player.exist(['win']):
        my_player.find_touch(['win'])


def destroy_item(player, location):
    player.find_touch(['lobby', location, 'destroy'])

    if player.exist(['start_destroy']):
        player.find_touch(['start_destroy', 'REWARD'])

    player.find_touch(['cancel', 'gain_reward', 'REWARD_2', 'REWARD', 'lobby'])


def claim_free_diamond(player, location):
    player.find_touch(location)

    if player.exist(['free_diamond']):
        player.find_touch(['free_diamond', 'REWARD'])

