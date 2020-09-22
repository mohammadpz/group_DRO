#!/bin/bash

cd $SLURM_TMPDIR
mkdir celebA
cd celebA
mkdir data
cd data
cp /home/askarihr/scratch/img_align_celeba.zip .
unzip img_align_celeba.zip -qq
cp /home/askarihr/scratch/GS/group_DRO/celebA/data/*.csv .
cd /home/askarihr/scratch/GS/group_DRO

~/miniconda/bin/python run_expt.py -s confounder -d CelebA -t Blond_Hair -c Male --model resnet50 --batch_size 128 --n_epochs 50 --alpha 0.01 --gamma 0.1 --generalization_adjustment 0 --show_progress --weight_decay 0.1 --lr 1e-05 --reweight_groups --robust --log_dir ./logs_test --data_dir $SLURM_TMPDIR


# sbatch --time=23:00:0 --gres=gpu:1 --mem=32G --account=rrg-bengioy-ad_gpu --cpus-per-task=4 --output=/home/askarihr/scratch/logs/slurm-%j.out /home/askarihr/scratch/GS/group_DRO/run_1.sh