from enum import Enum
import numpy as np

class Action(Enum):
    up = 1
    down = 2
    left = 3
    right = 4

class Block(Enum):
    start = 1
    barrier = 2
    trap = 3
    goal = 4
    normal = 5

class Markov:

    ACTION_COUNT = 4
    gamma = 0.8 # 衰减因子
    MAX_ITER_COUNT = 100 # 最大迭代周期
    REWARD_BARRIER = 0
    REWARD_TRAP = -10
    REWARD_GOAL = 10
    REWARD_NORMAL = 0

    def __init__(self):
        pass

    def read_map(self, size, start, barrier, trap, goal):
        self.row = size[0]
        self.column = size[1]
        self.start = start
        self.barrier = barrier
        self.trap = trap
        self.goal = goal

    def trans_coordinate(self, coordinate):
        return coordinate[0] * self.column + coordinate[1]

    def reverse_coordinate(self, index):
        return [index // self.column, index % self.column]

    def get_dist_type(self, dist):
        if (dist[0] < 0 or dist[0] >= self.row or dist[1] < 0 or dist[1] >= self.column):
            return Block.barrier
        else:
            return self.state[self.trans_coordinate(dist)]['type']

    def set_block_prob_and_reward(self, origin, dist, action, prob):
        # 若原目标不是普通块, 则没有必要修改
        if self.get_dist_type(origin) in [Block.barrier, Block.trap, Block.goal]:
            return

        block_type = self.get_dist_type(dist)
        index_origin = self.trans_coordinate(origin)
        

        # 根据转移目标块的类型来修改概率转移函数和奖励函数
        if block_type == Block.barrier:
            self.trans_prob[action][index_origin].append(prob)
            self.reward[action][index_origin].append(self.REWARD_BARRIER)
            self.trans_dist[action][index_origin].append(index_origin)
        elif block_type == Block.trap:
            self.trans_prob[action][index_origin].append(prob)
            self.reward[action][index_origin].append(self.REWARD_TRAP)
            self.trans_dist[action][index_origin].append(self.trans_coordinate(self.start))
        elif block_type == Block.goal:
            self.trans_prob[action][index_origin].append(prob)
            self.reward[action][index_origin].append(self.REWARD_GOAL)
            self.trans_dist[action][index_origin].append(self.trans_coordinate(dist))
        else:
            self.trans_prob[action][index_origin].append(prob)
            self.reward[action][index_origin].append(self.REWARD_NORMAL)
            self.trans_dist[action][index_origin].append(self.trans_coordinate(dist))


    # 初始化转移概率函数和回报函数
    def init_prob_and_reward(self):
        self.trans_prob = {}
        self.reward = {}
        self.trans_dist = {}
        for action in Action:
            self.trans_prob[action] = [[] for i in range(self.row * self.column)]
            self.reward[action] = [[] for i in range(self.row * self.column)]
            self.trans_dist[action] = [[] for i in range(self.row * self.column)]
            for index in range(self.row * self.column):
                coordinate = self.reverse_coordinate(index)
                # action: up
                if action == Action.up:
                    # 左上方
                    self.set_block_prob_and_reward(coordinate, [coordinate[0] - 1, coordinate[1] - 1], action, 1 / 5)
                    # 正上方
                    self.set_block_prob_and_reward(coordinate, [coordinate[0] - 1, coordinate[1]], action, 3 / 5)
                    # 右上方
                    self.set_block_prob_and_reward(coordinate, [coordinate[0] - 1, coordinate[1] + 1], action, 1 / 5)

                # action: down
                elif action == Action.down:
                    # 左下方
                    self.set_block_prob_and_reward(coordinate, [coordinate[0] + 1, coordinate[1] - 1], action, 1 / 5)
                    # 正下方
                    self.set_block_prob_and_reward(coordinate, [coordinate[0] + 1, coordinate[1]], action, 3 / 5)
                    # 右下方
                    self.set_block_prob_and_reward(coordinate, [coordinate[0] + 1, coordinate[1] + 1], action, 1 / 5)

                # action: left
                elif action == Action.left:
                    # 左上方
                    self.set_block_prob_and_reward(coordinate, [coordinate[0] - 1, coordinate[1] - 1], action, 1 / 5)
                    # 正左方
                    self.set_block_prob_and_reward(coordinate, [coordinate[0], coordinate[1] - 1], action, 3 / 5)
                    # 左下方
                    self.set_block_prob_and_reward(coordinate, [coordinate[0] + 1, coordinate[1] - 1], action, 1 / 5)

                # action: right
                elif action == Action.right:
                    # 右上方
                    self.set_block_prob_and_reward(coordinate, [coordinate[0] - 1, coordinate[1] + 1], action, 1 / 5)
                    # 正右方
                    self.set_block_prob_and_reward(coordinate, [coordinate[0], coordinate[1] + 1], action, 3 / 5)
                    # 右下方
                    self.set_block_prob_and_reward(coordinate, [coordinate[0] + 1, coordinate[1] + 1], action, 1 / 5)



    # 获取在指定位置指定动作下的reward
    def get_reward(self, coordinate, action):
        return self.state[self.trans_coordinate(coordinate)]['reward'][action]

    def initialize_state(self):
        self.state = [{} for i in range(self.row * self.column)]
        for i in range(self.row * self.column):
            self.state[i]['type'] = Block.normal
            self.state[i]['policy'] = None

        # 初始化地图格子的种类
        self.state[self.trans_coordinate(self.start)]['type'] = Block.start

        for b in self.barrier:
            self.state[self.trans_coordinate(b)]['type'] = Block.barrier
        
        for t in self.trap:
            self.state[self.trans_coordinate(t)]['type'] = Block.trap

        for g in self.goal:
            self.state[self.trans_coordinate(g)]['type'] = Block.goal

        # 初始化状态转移概率向量, 奖励函数等
        self.init_prob_and_reward()

        # 初始化状态价值函数    
        self.value_vector = [0 for i in range(self.row * self.column)]

        
    # 判断最优方向
    def judge_option_action(self, value_list):
        option_action = Action.right
        option_value = value_list[option_action]

        for action in value_list:
            if value_list[action] > option_value:
                option_action = action
                option_value = value_list[action]
        
        return option_action
        

    # 迭代一次更新状态价值函数
    def update_value_once(self):
        self.next_value = [0 for i in range(self.row * self.column)]
        for index in range(self.row * self.column):
            origin = self.reverse_coordinate(index)
            if self.get_dist_type(origin) in [Block.barrier, Block.goal, Block.trap]:
                continue

            value_list = {}
            for action in Action:
                value = 0
                origin_index = self.trans_coordinate(origin)
                next_state_num = len(self.trans_dist[action][origin_index])
                for i in range(next_state_num):
                    value += self.trans_prob[action][origin_index][i] * \
                            (self.reward[action][origin_index][i] + self.gamma * \
                             self.value_vector[self.trans_dist[action][origin_index][i]])

                value_list[action] = value

            option_action = self.judge_option_action(value_list)
            self.next_value[index] = value_list[option_action]
            self.state[index]['policy'] = option_action

        for index in range(self.row * self.column):
            self.value_vector[index] = self.next_value[index]

    def transfrom_policy(self, action):
        if action == Action.up:
            return "↑"
        elif action == Action.down:
            return "↓"
        elif action == Action.left:
            return "←"
        elif action == Action.right:
            return "→"
        else:
            return "."

    def get_policy(self):
        policy_array = [self.transfrom_policy(s['policy']) for s in self.state]
        policy_matrix = np.array(policy_array, dtype=np.str).reshape((self.row, self.column))
        return policy_matrix

    def get_value(self):
        value_matrix = np.array(self.value_vector).reshape((self.row, self.column))
        return value_matrix
        


if __name__ == "__main__":
    markov = Markov()
    markov.read_map([5, 5], [0, 0], [[1, 2], [2, 2]], [[2, 3]], [[4, 4]])
    markov.initialize_state()

    for i in range(20):
        markov.update_value_once()

    markov.get_policy()
    markov.get_value()

