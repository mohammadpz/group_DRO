#!/bin/bash

cd $SLURM_TMPDIR
mkdir celebA
cd celebA
mkdir data
cd data
cp /home/askarihr/scratch/img_align_celeba.zip .
unzip -q img_align_celeba.zip
cp /home/askarihr/scratch/GS/group_DRO/celebA/data/*.csv .
cd /home/askarihr/scratch/GS/group_DRO

~/miniconda/bin/python run_expt.py -s confounder -d CelebA -t Blond_Hair -c Male --show_progress --weight_decay 0.0 --lr 1e-05 --log_dir ./logs_rw_sp_0.1_lr5 --sp 0.1 --data_dir $SLURM_TMPDIR --reweight_groups

# ~/miniconda/bin/python run_expt.py -s confounder -d CelebA -t Blond_Hair -c Male --show_progress --weight_decay 0.0 --lr 1e-05 --log_dir ./logs_sp_1.0_test --sp 1.0 --data_dir $SLURM_TMPDIR --adam --reweight_groups