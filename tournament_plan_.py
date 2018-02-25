# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 18:59:38 2018

@author: kh
"""

import itertools
import numpy as np
from collections import OrderedDict
import random
import time
import csv




#==============================================================================
# classes
#==============================================================================

class TournamentTable():
    """ """
    
    def __init__(self, nr_slots=10, nr_player = 14):
        """ """
        self.nr_slots = 10
        self.slots = []
        for i in range(self.nr_slots):
            self.slots.append(TimeSlot1())
        self.games_per_slot = self.slots[0].games_per_slot
        self.game_names = self.slots[0].game_names
        self.game_names_abbr = self.slots[0].game_names_abbr
        self.nr_games = self.games_per_slot * self.nr_slots
            
        self.nr_player = nr_player
        self.players = []
        for i in range(self.nr_player):
            self.players.append(i+1)
            
        self.encounters = TournamentTable.get_game_tuples(self.players)  
        self.nr_encounters = len(self.encounters)
        self.av = self.get_availability()    

        self.table = self.create_table()
        self.sel_enc = self.fill_table()
        return


    def get_availability(self):
        """ """
        temp = [(p, []) for p in self.players]
        av = OrderedDict(temp)    
        av = self.calc_availability3(av)      
        return av
        
    def calc_availability1(self, av):
        """ """
        av_keys = list(av.keys()).copy()
        for i in range(2*self.nr_games):
            av[av_keys[i%self.nr_player]].append(1)
        return av
        
    def calc_availability2(self, av):
        """ """
        av_keys = list(av.keys()).copy()
        for i in range(int(np.ceil(2*self.nr_games/self.nr_player))):
            for key in av_keys:
                av[key].append(1)
        return av

    def calc_availability3(self, av):
        """ """
        av_keys = list(av.keys()).copy()
        for i in range(2*self.nr_games+3):
            av[av_keys[i%self.nr_player]].append(1)
        return av


    def create_table(self):
        """ """
        table = np.zeros([self.nr_slots, self.games_per_slot], dtype='<U8')
        return table

    def create_player_table(self):
        """ """
        player_table = np.zeros([self.nr_player, self.nr_slots], dtype='<U16')
        return player_table        
        
    def fill_table(self):
        """ """
        selected_encounters = []
        av = self.av.copy()
        encounters = self.encounters.copy()

        # collect encounters        
        for i in range(self.nr_games):
            selected_encounters.append(self.find_one_encounter_in_encounters(av, encounters))

        # fill str-table
        for idx, enc in enumerate(selected_encounters):
            self.table[idx//self.games_per_slot,idx%self.games_per_slot] = str(enc)
        
        # fill tuple-table
        self.table_ = [[1 for i in range(self.games_per_slot)] for i in range(self.nr_slots)]
#        self.table_ = [[1]*self.games_per_slot]*self.nr_slots
        for idx, enc in enumerate(selected_encounters):
            self.table_[idx//self.games_per_slot][idx%self.games_per_slot] = enc
        return selected_encounters

    def fill_player_table(self):
        """ """
        self.player_table = self.create_player_table()        
        
        dct_times = self.get_players_play_times(self.table_)
        dct_discp = self.get_players_disciplines(self.table_)
        
        for player_idx, player in enumerate(self.players):
            for slot_idx in range(self.nr_slots):
                if slot_idx in dct_times[player]:
                    self.player_table[player_idx,slot_idx] = dct_discp[player].pop(0)
        return 
        
    def save_player_table_to_csv(self, fn=None):
        """ """
        if fn == None:
            fn = 'test2.csv'
        
        with open(fn, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            
            writer.writerow(['']+list(range(self.nr_slots)))
            
            for player_idx, player in enumerate(self.players):
                writer.writerow([player]+list(self.player_table[player_idx,:]))
        return
        
        
    def find_one_encounter_in_encounters(self, av, encounters):
        """randomly selects and removes an element from encounters in accordance
        to the av-orderedDict
        
        """
        len_start = len(encounters)
        
        while len_start == len(encounters):
            rand_idx = random.randrange(0,len(encounters))
            enc = encounters[rand_idx]      # enc is a tuple
            if (len(av[enc[0]]) >0) and (len(av[enc[1]]) > 0):
                av[enc[0]].pop(-1)
                av[enc[1]].pop(-1)
                encounters.pop(rand_idx)
        return enc

    def find_one_encounter_in_encounters2(self, av, encounters):
        """ """
        
        len_start = len(encounters)
        av_values = list(av_values())
        
        max_idx1 = np.argmax([len(val) for val in av_values])
        av_values[max_idx1] = []
        max_idx2 = np.argmax([len(val) for val in av_values])

    def swap_table_entries(self, idx_tuple1, idx_tuple2):
        """ """
        self.swap_str_table_entries(idx_tuple1, idx_tuple2)
        self.swap_tpl_table_entries(idx_tuple1, idx_tuple2)
        return

    def swap_str_table_entries(self, idx_tuple1, idx_tuple2):
        """ """
        new_table = tt.table.copy()

        temp = new_table[idx_tuple1].copy()
        new_table[idx_tuple1] = new_table[idx_tuple2]
        new_table[idx_tuple2] = temp
        self.table = new_table
        return      
        
    def swap_tpl_table_entries(self, idx_tuple1, idx_tuple2):
        """ """
        new_table = tt.table_.copy()

        temp = new_table[idx_tuple1[0]][idx_tuple1[1]]
        new_table[idx_tuple1[0]][idx_tuple1[1]] = new_table[idx_tuple2[0]][idx_tuple2[1]]
        new_table[idx_tuple2[0]][idx_tuple2[1]] = temp
        self.table_ = new_table
        return  
        
    def swap_random_arbitrary_entries(self):
        """ """
        row_idx1 = random.randrange(0, self.nr_slots) 
        col_idx1 = random.randrange(0, self.games_per_slot)
        row_idx2 = random.randrange(0, self.nr_slots)
        col_idx2 = random.randrange(0, self.games_per_slot)
        idx_tuple1, idx_tuple2 = (row_idx1, col_idx1), (row_idx2, col_idx2)
        
        self.swap_table_entries(idx_tuple1, idx_tuple2)
        return idx_tuple1, idx_tuple2
        
    def swap_random_in_timeslot(self):
        """ """
        row_idx = random.randrange(0, self.nr_slots)        
        col_idx1 = random.randrange(0, self.games_per_slot)
        col_idx2 = random.randrange(0, self.games_per_slot)
        idx_tuple1, idx_tuple2 = (row_idx, col_idx1), (row_idx, col_idx2)

        self.swap_str_table_entries(idx_tuple1, idx_tuple2)
        self.swap_tpl_table_entries(idx_tuple1, idx_tuple2)
        return idx_tuple1, idx_tuple2
        
    def swap_random_entire_timeslot(self):
        """ """
        row_idx1 = random.randrange(0, self.nr_slots) 
        row_idx2 = random.randrange(0, self.nr_slots) 
        
        idx_tuple1_lst = []
        idx_tuple2_lst = []
        for idx in range(self.games_per_slot):
            idx_tuple1_lst.append((row_idx1, idx))
            idx_tuple2_lst.append((row_idx2, idx))

        for idx in range(self.games_per_slot):  
            self.swap_table_entries(idx_tuple1_lst[idx], idx_tuple2_lst[idx])
                
#        idx_tuple01, idx_tupl02 = (row_idx1, 0), (row_idx2, 0)
#        idx_tuple11, idx_tupl12 = (row_idx1, 1), (row_idx2, 1)
#        idx_tuple21, idx_tupl22 = (row_idx1, 2), (row_idx2, 2)
#        
#        idx_tuple1_lst = [idx_tuple01, idx_tuple11, idx_tuple21]
#        idx_tuple2_lst = [idx_tuple02, idx_tuple12, idx_tuple22]

#        self.swap_table_entries(idx_tuple01, idx_tuple02)        
#        self.swap_table_entries(idx_tuple11, idx_tuple12)
#        self.swap_table_entries(idx_tuple21, idx_tuple22)
        return idx_tuple1_lst, idx_tuple2_lst
        
    def search_conflicts(self, print_out=True):
        """ """
        double_entries_lst = []
        for idx,time_slot in enumerate(self.table_):
            lst = self.get_list_of_players_in_one_timeslot(time_slot)
            double_entries_lst.append(TournamentTable.check_for_double_entry(lst))
            if print_out:
                print('row:',idx+1, ' :', double_entries_lst[-1])
        return double_entries_lst
        
        
    def get_list_of_players_in_one_timeslot(self, time_slot):
        """ """
#        time_slot = list(time_slot)
#        for idx,enc in enumerate(time_slot):
#            if type(enc) == np.str_:
#                time_slot[idx] = TournamentTable.conv_str_to_tpl(enc)
#        for tpl in time_slot:
        
        lst = []
        for enc in time_slot:
            for i in enc:
                lst.append(i)
        return lst

    def get_list_of_players_in_one_table_column(self, str_table, col_idx):
        """ """
        table_col = list(str_table[:,col_idx])
                
        lst = []
        for enc_str in table_col:
            enc = TournamentTable.conv_str_to_tpl(enc_str)
            for i in enc:
                lst.append(i)
        return lst
        
    def get_players_play_times(self, tpl_table):
        """ """
        dct = OrderedDict()
        for key in self.players:
            dct[key] = []
        
        for slot_idx in range(self.nr_slots):
            for game_idx in range(self.games_per_slot):
                tpl = tpl_table[slot_idx][game_idx]
                for i in tpl:
                    dct[i].append(slot_idx)
        return dct
        
    def get_players_disciplines(self, tpl_table):
        """ """
        game_names_abbr = self.game_names_abbr
        dct = OrderedDict()
        for key in self.players:
            dct[key] = []
            
        for slot_idx in range(self.nr_slots):
            for game_idx in range(self.games_per_slot):
                tpl = tpl_table[slot_idx][game_idx]
                for i in tpl:
                    dct[i].append(game_names_abbr[game_idx])
        return dct
        
    def calc_nr_of_conflicts(self):
        """ """
        conflict_lst = self.search_conflicts(print_out=False)
        nr_conflicts = [len(lst) for lst in conflict_lst]
        nr_conflicts = sum(nr_conflicts)
        
        return nr_conflicts

    def calc_minimizing_values_for_one_table_column(self, lst):
        """ """
        # create dct
        dct = {key:0 for key in lst}
        for val in lst:
            dct[val] +=1
            
        #calculate characteristic value for minimization
        val_list = list(dct.values())
        val = sum((np.array(val_list)-1)**2)
        return val
    
    def get_minimizing_val(self):
        """ """
        val_lst = []
        for col_idx in range(self.games_per_slot):
            lst = self.get_list_of_players_in_one_table_column(self.table, col_idx)
            val_lst.append(self.calc_minimizing_values_for_one_table_column(lst))
            
        # calculate overall minimizing value
        val_tot =  sum(np.array(val_lst)**2)
        return val_tot
        
    def get_minimizing2_val(self):
        """ """
        val_lst = []
        dct  = self.get_players_play_times(self.table_)
                
        for val in dct.values():
            val_lst.append(np.product(np.diff(val)))
        
        val_tot = sum(np.log(val_lst))
        return val_tot

    def minimizing_conflicts(self, nr_iteration=100):
        """swaps random arbitrary entries to reduce the conflicts of teams 
        occuring multiple times in the same time slot
        
        """
        val0 = self.calc_nr_of_conflicts()
        for i in range(nr_iteration):
            idx_tuple1, idx_tuple2 = self.swap_random_arbitrary_entries()
            val1 = self.calc_nr_of_conflicts()
            if val1 < val0:
                val0 = val1
            else:
                tt.swap_table_entries(idx_tuple1, idx_tuple2)
            print('val0: ', val0)
        return
              

    def minimizing1(self, nr_iteration=100):
        """swaps encounters within time slots to distribution of the teams 
        among different games (horizontal-improving)
        
        """        
        val0 = self.get_minimizing_val()
        for i in range(nr_iteration):
            idx_tuple1, idx_tuple2 = self.swap_random_in_timeslot()
            val1 = self.get_minimizing_val()
            if val1 < val0:
                val0 = val1
            else:
                tt.swap_table_entries(idx_tuple1, idx_tuple2)
            print('val0: ', val0)
        return
        
    def minimizing2(self, nr_iteration=100):
        """swaps time slots to increase breaks between two games by the same 
        team (vertical-improving) 
        
        """
        val0 = self.get_minimizing2_val()
        for i in range(nr_iteration):
            idx_tuple1_lst, idx_tuple2_lst = self.swap_random_entire_timeslot()
            val1 = self.get_minimizing2_val()
            if val1 > val0:
                val0 = val1
            else:
                for idx in range(self.games_per_slot):  
                    self.swap_table_entries(idx_tuple1_lst[idx], 
                                            idx_tuple2_lst[idx])
            print('val0: ', val0)
        return

        
    @staticmethod
    def get_game_tuples(players):
        """ """
        return list(itertools.combinations(players, 2))
        
    @staticmethod
    def conv_str_to_tpl(enc_str):
        """ """
        tpl = enc_str[1:-1].split(', ')
        tpl = tuple([int(val) for val in tpl])
        return tpl
        
    @staticmethod
    def conv_strTable_to_tplTable(str_table):
        """ """
        tpl_table = [[1 for i in range(str_table.shape[1])] for i in range(str_table.shape[0])]
        
        for i in range(str_table.shape[0]):
            for j in range(str_table.shape[1]):
                tpl_table[i][j] = TournamentTable.conv_str_to_tpl(str_table[i][j])
        return tpl_table

    @staticmethod
    def check_for_double_entry(lst):
        """ """
        double_entries = []        
        
        for idx, val in enumerate(lst):
            copy_list = lst.copy()
            copy_list.pop(idx)
            for val2 in copy_list:
                if val == val2:
                    double_entries.append(val)
        return double_entries
            


class TimeSlot():
    """ """
    
    def __init__(self, games_per_slot, game_names, game_names_abbr):
        """ """
        self.games_per_slot = games_per_slot
        self.game_names = game_names
        self.game_names_abbr = game_names_abbr
        self.number_of_participants = self.games_per_slot*2
        return
        
        
class TimeSlot1(TimeSlot):
    """ """
    
    GAMES_PER_SLOT = 7
    GAME_NAMES = [
        'Football',
        'Volleyball',
        'Unihockey',
        'Fungame1',
        'Fungame2',
        'Fungame3',
        'Fungame4',
    ]
    GAME_NAMES_ABBR = [
        'F',
        'V',
        'U',
        'F1',
        'F2',
        'F3',
        'F4',
    ]
    
    def __init__(self):
        """ """
        super().__init__(TimeSlot1.GAMES_PER_SLOT, 
                         TimeSlot1.GAME_NAMES,
                         TimeSlot1.GAME_NAMES_ABBR)
        return
        
        


#==============================================================================
# functions
#==============================================================================


def plot_nice(arr):
    """ """
    
    for row in range(arr.shape[0]):
        st = ['{:{width}}'.format(l, width=5) for l in arr[row]]
        
        print_string = ''
        for s in st:
            if np.float(s.split('-')[0]) < 10:
                print_string += '   ' + s
            else:
                print_string += '  ' + s + ' '
#            if np.float(s.split('-')[1]) > 10:
#                print_string += ' '
            
        print(print_string)
    return





#==============================================================================
# first try
#==============================================================================
#n= 14
#ll = list(itertools.combinations(players, 2))
#
#ll_  =np.zeros([7, 13], dtype='>U7')
#for i in range(len(ll)):
#    ll_[i//13][i%13] = str(ll[i])[1:-1].replace(', ','-')
#





#==============================================================================
# main function
#==============================================================================
if __name__ == "__main__":
    tt = TournamentTable(10)
    print(tt.av)
    tt.search_conflicts()
    pass


