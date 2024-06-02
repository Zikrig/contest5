# Что хранить
# количество голов команды
# колиество матей команды
# количество голов игрока
# к какой команде принадлежит игрок
# минуты забитых голов для данного игрока
# Сколько раз команда открывала счет
# сколько раз игрок открывал счет



# что выводить

import re

class Command:
    def __init__(self, name):
        self.name = name
        self.matches_count = 0
        self.goals_count = 0
        self.opens_count = 0
        # self.players_list = []

    def print_command(self):
        print(f'Имя {self.name}, число матчей {self.matches_count},\n число голов {self.goals_count}, число открытий {self.opens_count}')

    # def add_player(self, name):
    #     self.players_list.append(name)


    def add_match(self, goals):
        self.goals_count += goals

class Player:
    def __init__(self, name, command):
        self.name = name
        self.matches_count = 0
        self.goals_count = 0
        self.opens_count = 0
        self.minutes = {}
        self.command = command

    def print_player(self):
        print(f'Имя {self.name}, число матчей {self.matches_count},\n число голов {self.goals_count}, число открытий {self.opens_count}')
        print(self.minutes)

    def add_goal(self, minute):
        if(minute in self.minutes):
            self.minutes[minute] += 1
        else:
            self.minutes[minute] = 1
        self.goals_count +=1

class Reestr:
    def __init__(self, file, out):
        self.commands = {}
        self.players = {}

        f = open(file, 'r')
        self.file = f.read().split('\n')
        f.close()
        self.file_i = 0
        self.outfile = out
        self.res_text = []

    def put_to_file(self):
        lst = [str(s) for s in self.res_text]
        for l in range(len(self.res_text)):
            print(lst[l])

    def check_player(self, name):
        # return name in self.players
        if(name in self.players):
            return True
        return False
    
    def check_commands(self, name):
        if(name[0] in self.commands):
            return True
        return False
        # return name in self.commands

    def print_reestr(self):
        for command in self.commands:
            self.commands[command].print_command()
        for player in self.players:
            self.players[player].print_player()

    def garant_command(self, name):
        if not name in self.commands:
            self.commands[name] = Command(name)
        self.commands[name].matches_count += 1

    def garant_player(self, name, command):
        if not name in self.players:
            self.players[name] = Player(name, command)
        self.players[name].matches_count += 1

    def parse_file(self):
        while(self.file_i < len(self.file)):
            str_text = self.file[self.file_i]
            if('-' in str_text):
                self.parse_input()
                self.file_i += 1
                continue
            else:
                self.parse_request(str_text)
                self.file_i += 1
    
    def parse_request(self, request):
        com = re.findall(r'\"[\s\w]+\"', request)
        if(len(com) == 1):
            if not self.check_commands(com):
                self.res_text.append(0)
                return True
        
        if('Total goals for' in request):
            com = re.findall(r'\"[\s\w]+\"', request)
            self.res_text.append(self.commands[com[0]].goals_count)
        elif('Total goals by' in request):
            player = request.replace('Total goals by', '')
            player = player.strip()
            if self.check_player(player):
                self.res_text.append(self.players[player].goals_count)
            else:
                self.res_text.append(0)
        elif('Mean goals per game for' in request):
            com = re.findall(r'\"[\s\w]+\"', request)
            games = self.commands[com[0]].matches_count
            goals = self.commands[com[0]].goals_count
            self.res_text.append(round(goals/games, 3))
        elif('Mean goals per game by' in request):
            player = request.replace('Mean goals per game by', '')
            player = player.strip()
            games = self.commands[self.players[player].command].matches_count
            goals = self.players[player].goals_count
            if self.check_player(player):
                self.res_text.append(round(goals/games, 3))
            else:
                self.res_text.append(0)
        elif('Goals on minute' in request):
            minu = re.findall(r'\d+', request)[0]
            player = request.split(minu)[1]
            minute = int(re.findall(r'\d+', request)[0])
            player = player[3:].strip()
            if self.check_player(player):
                mins = self.players[player].minutes
                res = 0
                for min_item in mins:
                    if(min_item==minute):
                        res+=mins[min_item]
                self.res_text.append(res)
            else:
                self.res_text.append(0)
            
        elif('Goals on first' in request):
            minute = int(re.findall(r'\d+', request)[0])
            player = request.split('minutes by')[1]
            player = player.strip()

            if self.check_player(player):
                mins = self.players[player].minutes
                res = 0
                for min_item in mins:
                    if(min_item<=minute):
                        res+=mins[min_item]
                self.res_text.append(res)
            else:
                self.res_text.append(0)

        elif('Goals on last' in request):
            minute = int(re.findall(r'\d+', request)[0])
            player = request.split('minutes by')[1]
            player = player.strip()

            if self.check_player(player):
                mins = self.players[player].minutes
                res = 0
                for min_item in mins:
                    if(min_item<=90 and min_item>=91-minute):
                        res+=mins[min_item]
                self.res_text.append(res)
            else:
                self.res_text.append(0)
           
        elif('Score opens by' in request and '"' in request):
            com = re.findall(r'\"[\s\w]+\"', request)
            ops = self.commands[com[0]].opens_count
            self.res_text.append(ops)
        elif('Score opens by' in request):
            player = request.replace('Score opens by', '')
            player = player.strip()
            if self.check_player(player):
                ops = self.players[player].opens_count
                self.res_text.append(ops)
            else:
                self.res_text.append(0)

        # else:
        #     print(f'Нихрена не опознали в "{request}"')
        
        

    def parse_input(self):
        # Парсим строку с командами. Добавляем счет по матчам
        commands = self.file[self.file_i]
        
        coms = re.findall(r'\"[\s\w]+\"', commands)
        goal_count = re.findall(r'\d+', commands)
        self.garant_command(coms[0])
        self.commands[coms[0]].add_match(int(goal_count[0]))
        self.garant_command(coms[1])
        self.commands[coms[1]].add_match(int(goal_count[1]))

        open_goal = {
            'min': 150,
            'command': '',
            'player': ''
        }

        for command_item in range(2):
            # print(f'command {command_item}')
            for i in range(int(goal_count[command_item])):
                # print(f'goal {i}')
                self.file_i += 1
                goal_str = self.file[self.file_i]
                time = int(re.findall(r'\d+', goal_str)[0])
                player_name = ' '.join(goal_str.split(' ')[:-1])
                self.garant_player(player_name, coms[command_item])
                self.players[player_name].add_goal(time)
                if(i == 0):
                    if(time<open_goal['min']):
                        open_goal['min'] = time
                        open_goal['command'] = coms[command_item]
                        open_goal['player'] = player_name

        if(open_goal['min'] != 150):
            self.commands[open_goal['command']].opens_count += 1
            self.players[open_goal['player']].opens_count += 1
        
    # def parse_match()


reestr = Reestr('input.txt', 'output.txt')

reestr.parse_file()
reestr.put_to_file()