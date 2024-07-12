import time

import keyboard as keyboard

from auto_player import Player

my_player = Player(accuracy=0.8, adb_mode=False)


def change_accuracy(new_accuracy):
    my_player.change_accuracy(new_accuracy)


def change_interval(new_interval):
    my_player.change_interval(new_interval)

def change_click(click_pattern):
    my_player.change_click(click_pattern)


def gain_rewards(arena_shop_task):
    while True:
        # 仓库收米
        if my_player.exist(['shop']):
            my_player.find_touch_skewing(['shop'], 90, 104)
            my_player.find_touch(['destroy'])

            if my_player.exist(['start_destroy']):
                my_player.find_touch(['start_destroy', 'REWARD'])

            my_player.find_touch(['cancel', 'gain_reward', 'REWARD_2', 'REWARD', 'lobby'])
        # 友情点
        if my_player.exist(['friend']):
            my_player.find_touch(['friend', 'give', 'confirm', 'close'])
        # 邮箱
        if my_player.exist(['mail']):
            my_player.find_touch(['mail'])
            time.sleep(my_player.interval)
            my_player.find_touch(['gain_mail'])
            time.sleep(my_player.interval)
            my_player.find_touch(['REWARD', 'close_3'])
        # 商店每日免费物品
        if my_player.exist(['shop']):
            my_player.find_touch(['shop', '0'])
            my_player.find_touch(['buy', 'REWARD'])
            if arena_shop_task:
                my_player.find_touch(['arena_shop'])
                my_player.find_touch_skewing(['arena_shop_2'], 0, 110)
                my_player.find_touch(['buy', 'REWARD'])
                my_player.find_touch_skewing(['arena_shop_2'], 0, 220)
                my_player.find_touch(['buy', 'REWARD'])
                my_player.find_touch_skewing(['arena_shop_2'], 0, 330)
                my_player.find_touch(['buy', 'REWARD'])
                my_player.find_touch_skewing(['arena_shop_2'], 0, 440)
                my_player.find_touch(['buy', 'REWARD'])
            my_player.find_touch(['home', 'home'])
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
            my_player.find_touch(['ark', 'ark', 'arena', 'arena', 'special_arena', 'special_arena'])
            my_player.find_touch_skewing(['touch'], 90, 87)
            time.sleep(my_player.interval)
            my_player.find_touch(['gain_reward_2', 'REWARD', 'home'])
            time.sleep(my_player.interval)
        # 任务委托收米
        if my_player.exist(['base']):
            my_player.find_touch(['base'])
            time.sleep(my_player.interval * 2.5)
            my_player.find_touch(['board', 'gain_all', 'REWARD', 'dispatch_all', 'dispatch', 'home', 'home'])
            time.sleep(my_player.interval * 2.5)
        # 日常任务
        if my_player.exist(['mission']):
            my_player.find_touch_skewing(['mission'], 180, 155)
            my_player.find_touch(['gain_all_2', 'gain_all_2', 'REWARD', 'close_2'])
            if my_player.exist(['000']):
                break
        # 露菲弹窗广告
        if my_player.exist(['ad']):
            my_player.find_touch(['ad', 'confirm_2'])


def recruit():
    my_player.find_touch_same_screen(['recruit_one', 'skip', 'confirm_3'])


def simulation_room(overclocking):
    if my_player.exist(['ark']):
        my_player.find_touch(['ark', 'simulation_room', 'simulation_room'])
        time.sleep(my_player.interval)

        if overclocking:
            my_player.find_touch_skewing(['start_simulation_1'], 90, 133)
            time.sleep(my_player.interval)
            my_player.find_touch(['bios_setting', 'start_simulation_3'])
        else:
            my_player.find_touch(['start_simulation_1', 'difficulty', 'zone'])
            time.sleep(my_player.interval)
            my_player.find_touch(['start_simulation_2'])

    while True:
        if my_player.exist(['start_simulation_2']):
            my_player.find_touch(['start_simulation_2'])
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
            handle_buff()
        elif my_player.exist(['SSR']):
            my_player.find_touch(['SSR', 'confirm_7', 'confirm_4'])
            handle_buff()
        elif my_player.exist(['SR']):
            my_player.find_touch(['SR', 'confirm_7', 'confirm_4'])
            handle_buff()
        elif my_player.exist(['R']):
            my_player.find_touch(['R', 'confirm_7', 'confirm_4'])
            handle_buff()

        handle_buff()

        if my_player.exist(['enter_B']):
            my_player.find_touch(['enter_B'])
        elif my_player.exist(['enter_C']):
            my_player.find_touch(['enter_C'])
        elif my_player.exist(['end_simulation']):
            my_player.find_touch(['end_simulation', 'confirm_9'])
            if my_player.exist(['EPIC']):
                my_player.find_touch(['EPIC', 'confirm_4'])
            elif my_player.exist(['SSR']):
                my_player.find_touch(['SSR', 'confirm_4'])
            elif my_player.exist(['SR']):
                my_player.find_touch(['SR', 'confirm_4'])
            elif my_player.exist(['R']):
                my_player.find_touch(['R', 'confirm_4'])
            handle_buff()
            my_player.find_touch(['home', 'home'])
            break


def auto_consult():
    while True:
        if my_player.exist(['lobby']):
            my_player.find_touch_skewing(['lobby'], 180, 145)
            my_player.find_touch(['consult'])
        if my_player.exist(['nikke_consult']):
            my_player.find_touch(['nikke_consult'])
            if my_player.exist(['quick_consult']):
                my_player.find_touch(['quick_consult', 'confirm_6', 'back'])
            else:
                my_player.find_touch(['consult_2', 'confirm_6', 'confirm_6', 'auto'])
        if my_player.exist(['confirm_6']):
            my_player.find_touch(['confirm_6'])
        # 小红帽选项
        if my_player.exist(['consult_option_2']):
            time.sleep(my_player.interval)
            my_player.find_touch(['consult_option', 'skip', 'back'])
        if my_player.exist(['consult_option']):
            time.sleep(my_player.interval)
            my_player.find_touch(['consult_option', 'skip', 'back'])
        if my_player.exist(['rank_up']):
            my_player.find_touch(['rank_up', 'back'])
        if my_player.exist(['consult_done']):
            my_player.find_touch(['home'])
            break


def auto_arena():
    while True:
        if my_player.exist(['ark']):
            my_player.find_touch(['ark', 'arena', 'arena', 'rookie_arena'])
        if my_player.exist(['rookie_arena']):
            my_player.find_touch(['rookie_arena'])
        if my_player.exist(['enter_battle_2']):
            my_player.find_touch_skewing(['enter_battle_2'], 90, 163)
            my_player.find_touch(['enter_battle_3'])
        if my_player.exist(['win']):
            my_player.find_touch(['win'])
        if my_player.exist(['lose']):
            my_player.find_touch(['lose'])
        if my_player.exist(['enter_battle_4']) and not my_player.exist(['enter_battle_2']):
            my_player.find_touch(['home'])
            break


def union_battle():
    while True:
        if my_player.exist(['friend']):
            my_player.find_touch_skewing(['friend'], 90, 60)
        if my_player.exist(['union_attack']):
            my_player.find_touch(['union_attack', 'skip_reward', 'skip_reward', 'confirm_8'])
        if my_player.exist(['union_attack_2']):
            my_player.find_touch_skewing(['union_attack_2'], 90, 285)
        if my_player.exist(['enter_union_battle']):
            my_player.find_touch(['enter_union_battle'])
        elif my_player.exist(['02']):
            my_player.find_touch(['02', 'enter_union_battle'])
            if my_player.exist(['03']):
                my_player.find_touch(['03', 'enter_union_battle'])
                if my_player.exist(['battle_times_done']):
                    my_player.find_touch(['home'])
                    time.sleep(1)
                    break

        if my_player.exist(['next_step']):
            my_player.find_touch(['next_step'])
        if my_player.exist(['confirm_8']):
            if my_player.exist(['skip_reward']):
                my_player.find_touch(['skip_reward'])
            my_player.find_touch(['confirm_8'])


def interception_battle():
    while True:
        if my_player.exist(['ark']):
            my_player.find_touch(['ark', 'interception', 'interception'])
        if my_player.exist(['interception_battle']):
            my_player.find_touch_skewing(['interception_battle'], 90, 170)
        if my_player.exist(['quick_battle_2']):
            my_player.find_touch(['quick_battle_2', 'next_step'])
        elif my_player.exist(['enter_union_battle']):
            my_player.find_touch(['enter_union_battle'])
        else:
            my_player.find_touch(['home'])
            break
        if my_player.exist(['next_step']):
            my_player.find_touch(['next_step'])


def single_raids():
    while True:
        if my_player.exist(['challenge_mode']):
            my_player.find_touch(['7'])
        if my_player.exist(['single_raids']):
            my_player.find_touch(['single_raids'])
        if my_player.exist(['quick_battle_2']):
            my_player.find_touch(['quick_battle_2', 'max'])
            my_player.find_touch_skewing(['max'], 35, 100)
        elif my_player.exist(['challenge']):
            my_player.find_touch(['challenge', 'confirm_2'])
        if my_player.exist(['enter_union_battle']):
            my_player.find_touch(['enter_union_battle'])
        elif my_player.exist(['team_set']):
            my_player.find_touch_skewing(['team_set_2'], 0, 43)
            my_player.find_touch(['enter_union_battle'])
        if my_player.exist(['next_step']):
            my_player.find_touch(['next_step'])
        if my_player.exist(['enemy_defeated']):
            my_player.find_touch(['enemy_defeated'])
        if my_player.exist(['battle_times_done_2']):
            my_player.find_touch(['home'])
            break


def continuous_click():
    while True:
        if keyboard.is_pressed('q'):
            my_player.continuous_click()


def auto_all(auto_task_list, arena_shop_task, overclocking):
    if auto_task_list[0]:
        simulation_room(overclocking)
        time.sleep(my_player.interval)
    if auto_task_list[1]:
        auto_arena()
        time.sleep(my_player.interval)
    if auto_task_list[2]:
        auto_consult()
        time.sleep(my_player.interval)
    if auto_task_list[4]:
        union_battle()
        time.sleep(my_player.interval)
    if auto_task_list[5]:
        interception_battle()
        time.sleep(my_player.interval)
    if auto_task_list[6]:
        single_raids()
        time.sleep(my_player.interval)
    if auto_task_list[3]:
        gain_rewards(arena_shop_task)
        time.sleep(my_player.interval)


def claim_free_diamond(player, location):
    player.find_touch(location)

    if player.exist(['free_diamond']):
        player.find_touch(['free_diamond', 'REWARD'])


def handle_buff():
    if my_player.exist(['exceeded_buff']):
        my_player.find_touch_skewing(['exceeded_buff'], 90, 300)
        my_player.find_touch(['confirm_4'])

    if my_player.exist(['repeated_buff']):
        my_player.find_touch_skewing(['repeated_buff'], 90, 300)
        my_player.find_touch(['confirm_4'])

