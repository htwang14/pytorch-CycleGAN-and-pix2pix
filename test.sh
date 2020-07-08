#!/bin/bash

# python test.py --dataroot datasets/summer2winter_yosemite/testA --name summer2winter_yosemite_pretrained \
#     --model test --no_dropout --num_test 10000 --results_dir results/summer2winter
python test.py --dataroot datasets/summer2winter_yosemite/testB --name winter2summer_yosemite_pretrained \
    --model test --no_dropout --num_test 10000 --results_dir results/winter2summer


# python test.py --dataroot datasets/summer2winter_yosemite/trainA --name summer2winter_yosemite_pretrained \
#     --model test --no_dropout --num_test 10000 --results_dir results_trainset/summer2winter
python test.py --dataroot datasets/summer2winter_yosemite/trainB --name winter2summer_yosemite_pretrained \
    --model test --no_dropout --num_test 10000 --results_dir results_trainset/winter2summer
