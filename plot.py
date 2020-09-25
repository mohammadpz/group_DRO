import matplotlib.pyplot as plt

# for job in [
#     'logs_dro',
#     'logs_lr1e-5_adam_sp0.0',
#     # 'logs_rw_lr1e-4_sp0.001',
#     # 'logs_lr1e-5_adam_sp0.0001',
#     # 'logs_rw_lr1e-4_sp0.01',
#     # 'logs_lr1e-5_adam_sp0.001',
#     # 'logs_rw_lr1e-4_sp0.1',
#     # 'logs_lr1e-5_adam_sp0.01',
#     # 'logs_rw_lr1e-4_sp1.0',
#     # 'logs_lr1e-5_adam_sp0.1',
#     # 'logs_rw_lr1e-4_sp10.0',
#     # 'logs_lr1e-5_adam_sp1.0',
#     'logs_rw_lr1e-5_adam_sp0.0',
#     'logs_lr1e-5_sp0.0',
#     # 'logs_rw_lr1e-5_adam_sp0.0001',
#     # 'logs_lr1e-5_sp0.0001',
#     # 'logs_rw_lr1e-5_adam_sp0.001',
#     # 'logs_lr1e-5_sp0.001',
#     # 'logs_rw_lr1e-5_adam_sp0.01',
#     'logs_lr1e-4_adam_sp0.0',
#     # 'logs_lr1e-5_sp0.01',
#     # 'logs_rw_lr1e-5_adam_sp0.1',
#     # 'logs_lr1e-4_adam_sp0.0001',
#     # 'logs_lr1e-5_sp0.1',
#     # 'logs_rw_lr1e-5_adam_sp1.0',
#     # 'logs_lr1e-4_adam_sp0.001',
#     # 'logs_lr1e-5_sp1.0',
#     # 'logs_rw_lr1e-5_adam_sp10.0',
#     # 'logs_lr1e-4_adam_sp0.01',
#     # 'logs_lr1e-5_sp10.0',
#     'logs_rw_lr1e-5_sp0.0',
#     # 'logs_lr1e-4_adam_sp0.1',
#     'logs_rw_lr1e-4_adam_sp0.0',
#     # 'logs_rw_lr1e-5_sp0.0001',
#     # 'logs_lr1e-4_adam_sp1.0',
#     # 'logs_rw_lr1e-4_adam_sp0.0001',
#     # 'logs_rw_lr1e-5_sp0.001',
#     'logs_lr1e-4_sp0.0',
#     # 'logs_rw_lr1e-4_adam_sp0.001',
#     # 'logs_rw_lr1e-5_sp0.01',
#     # 'logs_lr1e-4_sp0.0001',
#     # 'logs_rw_lr1e-4_adam_sp0.01',
#     # 'logs_rw_lr1e-5_sp0.1',
#     # 'logs_lr1e-4_sp0.001',
#     # 'logs_rw_lr1e-4_adam_sp0.1',
#     # 'logs_rw_lr1e-5_sp1.0',
#     # 'logs_lr1e-4_sp0.01',
#     # 'logs_rw_lr1e-4_adam_sp1.0',
#     # 'logs_rw_lr1e-5_sp10.0',
#     # 'logs_lr1e-4_sp0.1',
#     # 'logs_rw_lr1e-4_adam_sp10.0',
#     # 'logs_lr1e-4_sp1.0',
#     'logs_rw_lr1e-4_sp0.0',
#     # 'logs_lr1e-4_sp10.0',
#     # 'logs_rw_lr1e-4_sp0.0001',
#             ]:

accs = {}
for job in [
    'logs_dro',
    # 'logs_rw_lr1e-4_adam_sp0.0',
    # 'logs_rw_lr1e-4_adam_sp0.0001',
    # 'logs_rw_lr1e-4_adam_sp0.001',
    # 'logs_rw_lr1e-4_adam_sp0.01',
    # 'logs_rw_lr1e-4_adam_sp0.1',
    # 'logs_rw_lr1e-4_adam_sp1.0',
    # 'logs_rw_lr1e-4_adam_sp10.0',
    # 'logs_rw_lr1e-4_sp0.0',
    # 'logs_rw_lr1e-4_sp0.0001',
    # 'logs_rw_lr1e-4_sp0.001',
    # 'logs_rw_lr1e-4_sp0.01',
    # 'logs_rw_lr1e-4_sp0.1',
    # 'logs_rw_lr1e-4_sp1.0',
    # 'logs_rw_lr1e-4_sp10.0',
    # 'logs_rw_lr1e-5_adam_sp0.0',
    # 'logs_rw_lr1e-5_adam_sp0.0001',
    # 'logs_rw_lr1e-5_adam_sp0.001',
    # 'logs_rw_lr1e-5_adam_sp0.01',
    # 'logs_rw_lr1e-5_adam_sp0.1',
    # 'logs_rw_lr1e-5_adam_sp1.0',
    # 'logs_rw_lr1e-5_adam_sp10.0',
    # 'logs_rw_lr1e-5_sp0.0',
    # 'logs_rw_lr1e-5_sp0.0001',
    # 'logs_rw_lr1e-5_sp0.001',
    # 'logs_rw_lr1e-5_sp0.01',
    # 'logs_rw_lr1e-5_sp0.1',
    # 'logs_rw_lr1e-5_sp1.0',
    # 'logs_rw_lr1e-5_sp10.0'
            ]:
    val = False
    file1 = open('/home/askarihr/scratch/GS/group_DRO/' + job + '/log.txt', 'r')
    Lines = file1.readlines()
    accs[job] = []
    for line in Lines:
        if 'Validation:' in line:
            val = True
        if val and 'Blond_Hair = 1, Male = 1  [n = 182]:' in line:
        # if val and 'Average acc:' in line:
            accs[job] += [float(line.split(' ')[-1].strip())]
            # accs[job] += [float(line.split(' ')[-3].strip())]
        if 'Current lr:' in line:
            val = False
    plt.plot(accs[job], label=job)

plt.legend()
plt.savefig('plot.png')
