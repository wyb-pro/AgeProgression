import re
IMAGE_PATH = "./data/UTKFace"
EPOCHS = 100
IMAGE_LENGTH = 128
IMAGE_DEPTH = 3


IMAGE_LENGTH = 128
IMAGE_DEPTH = 3


BATCH_SIZE = 64
KERNEL_SIZE = 2
STRIDE_SIZE = 2

NUM_ENCODER_CHANNELS = 64
NUM_Z_CHANNELS = 100
NUM_GEN_CHANNELS = 1024
NUM_AGES = 10

UTKFACE_ORIGINAL_IMAGE_FORMAT = re.compile('^(\d+)_(\d+)_\d+_(\d+)\.jpg\.chip\.jpg$')

NUM_GENDERS = 2
UTKFACE_ORIGINAL_IMAGE_FORMAT = re.compile('^(\d+)_(\d+)_\d+_(\d+)\.jpg\.chip\.jpg$')
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

MALE = 0
FEMALE = 1

UTKFACE_DEFAULT_PATH = './data/UTKFace'
