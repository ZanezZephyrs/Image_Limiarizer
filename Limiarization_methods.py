import numpy as np
import cv2


def global_method(img):
    return np.where(img < 128, 0, 1)


def global_method_adjustive_treshold(img, treshold):
    return np.where(img < treshold, 0, 1)


def mean(vetor):
    return np.mean(vetor)


def standart_deviation(vetor):
    return np.std(vetor)


def mean_method(img, size=3):
    img = np.float32(img)
    pad_size = size // 2
    res = np.ones(
        (img.shape[0], img.shape[1]),
        dtype="uint16") * -1  #resultado criado com matriz composta de -1
    img = cv2.copyMakeBorder(img, pad_size, pad_size, pad_size, pad_size,
                             cv2.BORDER_REPLICATE)
    for i in range(pad_size, img.shape[0] - pad_size):
        for j in range(pad_size, img.shape[1] - pad_size):
            roi = img[i - pad_size:i + pad_size + 1,
                      j - pad_size:j + pad_size + 1]
            res[i - pad_size][j -
                              pad_size] = 0 if img[i][j] <= roi.mean() else 1
    res = np.uint8(res)
    return res


def bernsen(img, size=3):
    img = np.float32(img)
    pad_size = size // 2
    res = np.ones(
        (img.shape[0], img.shape[1]),
        dtype="uint16") * -1  #resultado criado com matriz composta de -1
    img = cv2.copyMakeBorder(img, pad_size, pad_size, pad_size, pad_size,
                             cv2.BORDER_REPLICATE)
    for i in range(pad_size, img.shape[0] - pad_size):
        for j in range(pad_size, img.shape[1] - pad_size):
            roi = img[i - pad_size:i + pad_size + 1,
                      j - pad_size:j + pad_size + 1]
            treshold = (roi.min() + roi.max()) // 2
            res[i - pad_size][j - pad_size] = 0 if img[i][j] < treshold else 1
    res = np.uint8(res)
    return res


def Phansalskar(img, size=11, k=0.25, R=0.5, p=2, q=10):
    img = np.float32(img)
    img = cv2.normalize(img,
                        None,
                        alpha=0,
                        beta=1,
                        norm_type=cv2.NORM_MINMAX,
                        dtype=cv2.CV_32F)
    pad_size = size // 2
    res = np.ones((img.shape[0], img.shape[1]), dtype="uint16")
    img = cv2.copyMakeBorder(img, pad_size, pad_size, pad_size, pad_size,
                             cv2.BORDER_REPLICATE)
    for i in range(pad_size, img.shape[0] - pad_size):
        for j in range(pad_size, img.shape[1] - pad_size):
            roi = img[i - pad_size:i + pad_size + 1,
                      j - pad_size:j + pad_size + 1]
            treshold = mean(roi) * (1 + (p**(-q * mean(roi))) +
                                    (k * ((standart_deviation(roi) / R) - 1)))
            res[i - pad_size][j - pad_size] = 0 if img[i][j] <= treshold else 1
    res = np.uint8(res)
    return res