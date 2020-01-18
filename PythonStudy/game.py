import random

class Creature():

    def __init__(self, name, is_ai):
        self.name = name
        self.hp = random.randint(50, 61)
        self.full_hp = self.hp
        self.is_ai = is_ai
        #怪物类型分为 0: 攻击型, 1: 均衡型, 2: 反击型
        self.monster_type = random.randint(0,3)

    def is_alive(self):
        if self.hp > 0:
            return True
        else:
            return False

    def attack(self):
        attack_value = 20
        if self.monster_type == 0:
            attack_value += random.randint(0,5)
        elif self.monster_type == 1:
            pass
        else:
            attack_value -= random.randint(0,5)
        #AI输出折损60%
        if self.is_ai:
            attack_value = int(attack_value * 0.4)
        else:
            pass
        return attack_value

    def being_attack(self, damage):
        self.hp -= damage

    #反击成功率
    def counter_attack(self):
        if self.monster_type == 0:
            if random.randint(0,100) < 30 + 20 * (self.hp / self.full_hp):
                return True
            else:
                return False
        elif self.monster_type == 1:
            if random.randint(0,100) < 50 + 15 * (self.hp / self.full_hp):
                return True
            else:
                return False
        else:
            if random.randint(0,100) < 70 + 10 * (self.hp / self.full_hp):
                return True
            else:
                return False

    def check_hp_state(self):
        return [self.hp, self.full_hp]

    def get_monster_type(self):
        if self.monster_type == 0:
            return '攻击型'
        elif self.monster_type == 1:
            return '均衡型'
        else:
            return '反击型'

    #不同怪物采取行动的策略
    def is_ai_attack(self):
        if self.monster_type == 0:
            if random.randint(0,100) < 0 + self.full_hp - self.hp:
                return True
            else:
                return False
        elif self.monster_type == 1:
            if random.randint(0,100) < 25 + self.full_hp - self.hp:
                return True
            else:
                return False
        else:
            if random.randint(0,100) < 50 + self.full_hp - self.hp:
                return True
            else:
                return False

player_name = input('请输入您的游戏ID：')
player = Creature(player_name, False)
monster1 = Creature('怪物1', True)
monster2 = Creature('怪物2', True)
print(
'''

    游戏规则：
        怪物类型分为“攻击型”、“均衡型”和“防御型”。
        “攻击型”怪物的基础攻击力高，反击成功率低，AI的主动攻击欲望强；
        “均衡型”怪物的基础攻击力中，反击成功率中，AI的主动攻击欲望中等；
        “反击型”怪物的基础攻击力低，反击成功率高，AI的主动攻击欲望弱。

        行动顺序固定为：您 -> 怪物1 -> 怪物2
        由于是一打二，所以AI的输出会有折损，但是血量和您相当。
        血量越低，反击成功率越高，请合理选择攻击或反击！
        
        祝您好运！

''')
print('您战宠的怪物类型为"{}"，两个敌人的怪物类型分别为"{}"和"{}"。'.format(player.get_monster_type(), 
    monster1.get_monster_type(), monster2.get_monster_type()))

round = 1
while player.is_alive() and (monster1.is_alive() or monster2.is_alive()):
    print('\n********第{}回合********'.format(round))
    #预置本轮伤害
    player_damage_this_turn = player.attack()
    monster1_damage_this_turn = monster1.attack()
    monster2_damage_this_turn = monster2.attack()
    #预置怪物本轮行动
    is_monster1_attack_this_turn = monster1.is_ai_attack()
    is_monster2_attack_this_turn = monster2.is_ai_attack()
    #获取玩家行动
    while True:
        user_input = input('Attack or counter attack? (A/C):')
        if user_input == 'A':
            print('您选择了进攻')
            break
        elif user_input == 'C':
            print('您选择了反击')
            break
        else:
            pass
    #获取玩家选取的目标
    if user_input == 'A':
        while True:
            try:
                target = int(input('Select target: (1/2)'))
                if target == 1:
                    print('您选择了攻击怪物1')
                    break
                elif target == 2:
                    print('您选择了攻击怪物2')
                    break
                else:
                    continue
            except:
                continue
        if monster1.is_alive():
            print('怪物1选择了{}'.format('进攻' if is_monster1_attack_this_turn else '反击'))
        if monster2.is_alive():
            print('怪物2选择了{}'.format('进攻' if is_monster2_attack_this_turn else '反击'))
        if target == 1:
            if monster1.is_alive():
                #怪物1是否反击
                if not is_monster1_attack_this_turn:
                    #怪物1是否反击成功
                    if monster1.counter_attack():
                        player.being_attack(monster1_damage_this_turn)
                        print('怪物1反击成功！！对您造成{}点反击伤害，您当前的血条：{}/{}'.format(monster1_damage_this_turn,
                            max(player.check_hp_state()[0], 0), player.check_hp_state()[1]))
                    else:
                        monster1.being_attack(player_damage_this_turn)
                        print('您对怪物1造成了{}点伤害，怪物1当前的血条：{}/{}'.format(player_damage_this_turn,
                            max(monster1.check_hp_state()[0], 0), monster1.check_hp_state()[1]))
                else:
                    monster1.being_attack(player_damage_this_turn)
                    print('您对怪物1造成了{}点伤害，怪物1当前的血条：{}/{}'.format(player_damage_this_turn,
                        max(monster1.check_hp_state()[0], 0), monster1.check_hp_state()[1]))
            else:
                print('您鞭尸了怪物1')

        elif target == 2:
            if monster2.is_alive():
                #怪物2是否反击
                if not is_monster2_attack_this_turn:
                    #怪物2是否反击成功
                    if monster2.counter_attack():
                        player.being_attack(monster2_damage_this_turn)
                        print('怪物2反击成功！！对您造成{}点反击伤害，您当前的血条：{}/{}'.format(monster2_damage_this_turn,
                            max(player.check_hp_state()[0], 0), player.check_hp_state()[1]))
                    else:
                        monster2.being_attack(player_damage_this_turn)
                        print('您对怪物2造成了{}点伤害，怪物2当前的血条：{}/{}'.format(player_damage_this_turn,
                            max(monster2.check_hp_state()[0], 0), monster2.check_hp_state()[1]))
                else:
                    monster2.being_attack(player_damage_this_turn)
                    print('您对怪物2造成了{}点伤害，怪物2当前的血条：{}/{}'.format(player_damage_this_turn,
                        max(monster2.check_hp_state()[0], 0), monster2.check_hp_state()[1]))
            else:
                print('您鞭尸了怪物2')
        else:
            print('**********Debug: 玩家目标选取异常***********')

        if monster1.is_alive():
            #怪物1主动攻击
            if is_monster1_attack_this_turn:
                if player.is_alive():
                    player.being_attack(monster1_damage_this_turn)
                    print('怪物1向您发起攻击，对您造成{}点伤害，您当前的血条：{}/{}'.format(monster1_damage_this_turn, 
                        max(player.check_hp_state()[0], 0), player.check_hp_state()[1]))
                else:
                    print('怪物1鞭尸了您')
        if monster2.is_alive():
            #怪物2主动攻击
            if is_monster2_attack_this_turn:
                if player.is_alive():
                    player.being_attack(monster2_damage_this_turn)
                    print('怪物2向您发起攻击，对您造成{}点伤害，您当前的血条：{}/{}'.format(monster2_damage_this_turn, 
                        max(player.check_hp_state()[0], 0), player.check_hp_state()[1]))
                else:
                    print('怪物2鞭尸了您')


    elif user_input == 'C':
        if monster1.is_alive():
            print('怪物1选择了{}'.format('进攻' if is_monster1_attack_this_turn else '反击'))
        if monster2.is_alive():
            print('怪物2选择了{}'.format('进攻' if is_monster2_attack_this_turn else '反击'))
        if monster1.is_alive():
            #怪物1主动攻击
            if is_monster1_attack_this_turn:
                if player.is_alive():
                    #玩家反击成功
                    if player.counter_attack():
                        monster1.being_attack(player_damage_this_turn)
                        print('您成功反击了怪物1的攻击！！对怪物1造成{}点伤害，怪物1当前的血条：{}/{}'.format(player_damage_this_turn,
                            max(monster1.check_hp_state()[0], 0), monster1.check_hp_state()[1]))
                    #玩家反击失败
                    else:
                        player.being_attack(monster1_damage_this_turn)
                        print('怪物1向您发起攻击，对您造成{}点伤害，您当前的血条：{}/{}'.format(monster1_damage_this_turn, 
                            max(player.check_hp_state()[0], 0), player.check_hp_state()[1]))
                else:
                    print('怪物1鞭尸了您')

        if monster2.is_alive():
            #怪物2主动攻击
            if is_monster2_attack_this_turn:
                if player.is_alive():
                    #玩家反击成功
                    if player.counter_attack():
                        monster2.being_attack(player_damage_this_turn)
                        print('您成功反击了怪物2的攻击！！对怪物2造成{}点伤害，怪物2当前的血条：{}/{}'.format(player_damage_this_turn,
                            max(monster2.check_hp_state()[0], 0), monster1.check_hp_state()[1]))
                    #玩家反击失败
                    else:
                        player.being_attack(monster2_damage_this_turn)
                        print('怪物2向您发起攻击，对您造成{}点伤害，您当前的血条：{}/{}'.format(monster2_damage_this_turn, 
                            max(player.check_hp_state()[0], 0), player.check_hp_state()[1]))
                else:
                    print('怪物2鞭尸了您')
    else:
        print('*********Debug: 玩家输入行动异常***********')
    print('\n血量情况：  玩家：{}/{}，怪物1：{}/{}，怪物2：{}/{}'.format(
        max(player.check_hp_state()[0], 0), player.check_hp_state()[1],
        max(monster1.check_hp_state()[0], 0), monster1.check_hp_state()[1],
        max(monster2.check_hp_state()[0], 0), monster2.check_hp_state()[1]))
    round += 1

if player.is_alive():
    print('\n\n{}，恭喜您获得了胜利！'.format(player_name))
else:
    print('\n\n{}，很遗憾您失败了！'.format(player_name))