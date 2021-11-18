# coding: utf-8
# Crie um programa para encontrar a sub-sequência contínua dentro do array A que possua maior soma:
# Exemplo 1:
#     - Input: [-1,5,2,1,4,-7,8,-3,-4,2]
#     - Output:
def seq_max_sum(seq):
    seq_len = len(seq)
    max_sub_seq_arr = []
    max_sub_seq_sum = 0
    sub_seq_len = 2
    for num in seq:
        for e in range(0, seq_len-sub_seq_len+1):
            seq_local = seq[e:e+sub_seq_len]
            seq_local_sum = sum(seq_local)
            if sub_seq_len < seq_len and seq_local_sum > max_sub_seq_sum:
                max_sub_seq_arr = seq_local
                max_sub_seq_sum = seq_local_sum
        sub_seq_len = sub_seq_len+1
    return max_sub_seq_arr, max_sub_seq_sum;

sub_seq, sum = seq_max_sum([-1, 5, 2, 1, 4, -7, 8, -3, -4, -2]);
print('Exemplo 01: maior soma ({}) é do seq: {}'.format(sum, str(sub_seq)))

sub_seq, sum = seq_max_sum([-1, 5, 2, 1, 4, -7, 8, -3, -4, -2]);
print('Exemplo 02: maior soma ({}) é da seq: {}'.format(sum, str(sub_seq)))