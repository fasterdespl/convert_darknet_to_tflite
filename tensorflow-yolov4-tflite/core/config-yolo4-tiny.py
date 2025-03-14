from easydict import EasyDict as edict

__C                           = edict()
cfg                           = __C

# YOLO options
__C.YOLO                      = edict()

__C.YOLO.CLASSES              = "./data/classes/coco.names"

# Anchors adaptados a tu configuración personalizada
__C.YOLO.ANCHORS              = [10,14, 23,27, 37,58, 81,82, 135,169, 344,319]
__C.YOLO.ANCHORS_TINY         = [10,14, 23,27, 37,58, 81,82, 135,169, 344,319]

# Strides para dos escalas (porque tienes dos capas YOLO)
__C.YOLO.STRIDES              = [16, 32]
__C.YOLO.STRIDES_TINY         = [16, 32]

# XYSCALE ajustado a tus capas
__C.YOLO.XYSCALE              = [1.05, 1.05]
__C.YOLO.XYSCALE_TINY         = [1.05, 1.05]

# Configuración de las máscaras
__C.YOLO.MASKS                = [[3,4,5], [0,1,2]]

__C.YOLO.ANCHOR_PER_SCALE     = 3
__C.YOLO.IOU_LOSS_THRESH      = 0.5


# Train options
__C.TRAIN                     = edict()

__C.TRAIN.ANNOT_PATH          = "./data/dataset/val2017.txt"
__C.TRAIN.BATCH_SIZE          = 2
__C.TRAIN.INPUT_SIZE          = 416
__C.TRAIN.DATA_AUG            = True
__C.TRAIN.LR_INIT             = 1e-3
__C.TRAIN.LR_END              = 1e-6
__C.TRAIN.WARMUP_EPOCHS       = 2
__C.TRAIN.FISRT_STAGE_EPOCHS  = 20
__C.TRAIN.SECOND_STAGE_EPOCHS = 30


# TEST options
__C.TEST                      = edict()

__C.TEST.ANNOT_PATH           = "./data/dataset/val2017.txt"
__C.TEST.BATCH_SIZE           = 2
__C.TEST.INPUT_SIZE           = 416
__C.TEST.DATA_AUG             = False
__C.TEST.DECTECTED_IMAGE_PATH = "./data/detection/"
__C.TEST.SCORE_THRESHOLD      = 0.25
__C.TEST.IOU_THRESHOLD        = 0.5
