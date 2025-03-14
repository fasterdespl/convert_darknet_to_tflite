#! /usr/bin/env python
# coding=utf-8
from easydict import EasyDict as edict


__C = edict()
# Consumers can get config by: from config import cfg
cfg = __C

# YOLO options
__C.YOLO = edict()

__C.YOLO.CLASSES = "./data/classes/coco.names"
__C.YOLO.ANCHORS = [12,16, 19,36, 40,28, 36,75, 76,55, 72,146, 142,110, 192,243, 459,401]
__C.YOLO.STRIDES = [8, 16, 32]
__C.YOLO.XYSCALE = [1.2, 1.1, 1.05]
__C.YOLO.ANCHOR_PER_SCALE = 3
__C.YOLO.IOU_LOSS_THRESH = 0.213
__C.YOLO.IOU_NORMALIZER = 0.07
__C.YOLO.CLS_NORMALIZER = 1.0
__C.YOLO.IOU_LOSS = "ciou"
__C.YOLO.NMS_KIND = "greedynms"
__C.YOLO.BETA_NMS = 0.6
__C.YOLO.MAX_DELTA = 5
__C.YOLO.CLASSES_NUM = 1

# Train options
__C.TRAIN = edict()
__C.TRAIN.ANNOT_PATH = "./data/dataset/val2017.txt"
__C.TRAIN.BATCH_SIZE = 64
__C.TRAIN.INPUT_SIZE = 608
__C.TRAIN.DATA_AUG = True
__C.TRAIN.LR_INIT = 0.001
__C.TRAIN.LR_END = 1e-6
__C.TRAIN.WARMUP_EPOCHS = 2
__C.TRAIN.FIRST_STAGE_EPOCHS = 20
__C.TRAIN.SECOND_STAGE_EPOCHS = 30
__C.TRAIN.MOSAIC = 1

# TEST options
__C.TEST = edict()
__C.TEST.ANNOT_PATH = "./data/dataset/val2017.txt"
__C.TEST.BATCH_SIZE = 2
__C.TEST.INPUT_SIZE = 608
__C.TEST.DATA_AUG = False
__C.TEST.DECTECTED_IMAGE_PATH = "./data/detection/"
__C.TEST.SCORE_THRESHOLD = 0.25
__C.TEST.IOU_THRESHOLD = 0.5