#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File: count.py
# Author: Qian Ge <geqian1001@gmail.com>

import numpy as np
from src.lstm import LSTMcell

import src.assign as assign


def count_0_in_seq(input_seq, count_type):
    """ count number of digit '0' in input_seq

    Args:
        input_seq (list): input sequence encoded as one hot
            vectors with shape [num_digits, 10].
        count_type (str): type of task for counting.
            'task1': Count number of all the '0' in the sequence.
            'task2': Count number of '0' after the first '2' in the sequence.
            'task3': Count number of '0' after '2' but erase by '3'.

    Return:
        counts (int)
    """

    if count_type == 'task1':
        # Count number of all the '0' in the sequence.
        # create LSTM cell
        cell = LSTMcell(in_dim=10, out_dim=1)
        # assign parameters
        assign.assign_weight_count_all_0_case_1(cell, in_dim=10, out_dim=1)
        # initial the first state
        prev_state = [0.]
        # read input sequence one by one to count the digits
        for idx, d in enumerate(input_seq):
            prev_state = cell.run_step([d], prev_state=prev_state)
        count_num = int(np.squeeze(prev_state))
        return count_num

    if count_type == 'task2':
        # Count number of '0' after the first '2' in the sequence.
        # print('Not implemented.')
        cell = LSTMcell(in_dim=10, out_dim=2)
        # assign parameters
        assign.assign_weight_count_all_case_2(cell, in_dim=10, out_dim=2)
        # initial the first state
        prev_state = [0., 0.]
        # read input sequence one by one to count the digits
        for idx, d in enumerate(input_seq):
            print([d])
            print('previous state = ')
            print(prev_state)
            prev_state = cell.run_step([d], prev_state=prev_state)

            if(prev_state[0, 1] == 0.):
                prev_state = [0., 0.]

        count_num = int(prev_state[0, 0])

        return count_num

    if count_type == 'task3':
        # Count number of '0' in the sequence when receive '2', but erase
        # the counting when receive '3', and continue to count '0' from 0
        # until receive another '2'.
        # Count number of '0' after the first '2' in the sequence.
        # print('Not implemented.')
        cell = LSTMcell(in_dim=10, out_dim=3)
        # assign parameters
        assign.assign_weight_count_all_case_4(cell, in_dim=10, out_dim=3)
        # initial the first state
        prev_state = [[0., 0., 0.]]
        # read input sequence one by one to count the digits
        for idx, d in enumerate(input_seq):
            print([d])
            print('previous state = ')
            print(prev_state)
            prev_state = cell.run_step([d], prev_state=prev_state)

            if(prev_state[0, 1] < 1.):
                prev_state = [[0., 0., 0.]]
            elif(prev_state[0, 2] >= 1.):
                prev_state = [[0., 0., 0.]]

        prev_state = np.array(prev_state)
        count_num = int(prev_state[0, 0])

        return count_num
