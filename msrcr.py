import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--input', required=True, help='Input image path')
parser.add_argument('-o', '--output', required=True, help='Output image path')
parser.add_argument('-s', default=300, type=float, help='The scale (reference value)')
parser.add_argument('-n', default=3, type=int, help='The number of scale')
parser.add_argument('-d', default=2, type=float, help='The dynamic, the smaller the value, the higher the contrast')


def retinex_scales_distribution(max_scale, nscales):
    scales = []
    scale_step = max_scale / nscales
    for s in range(nscales):
        scales.append(scale_step * s + 2.0)
    return scales


def CR(im_ori, im_log, alpha=128., gain=1., offset=0.):
    im_cr = im_log * gain * (
            np.log(alpha * (im_ori + 1.0)) - np.log(np.sum(im_ori, axis=2) + 3.0)[:, :, np.newaxis]) + offset
    return im_cr


def MSRCR(image_path, max_scale, nscales, dynamic=2.0, do_CR=True):
    im_ori = np.float32(cv2.imread(image_path)[:, :, (2, 1, 0)])
    scales = retinex_scales_distribution(max_scale, nscales)

    im_blur = np.zeros([len(scales), im_ori.shape[0], im_ori.shape[1], im_ori.shape[2]])
    im_mlog = np.zeros([len(scales), im_ori.shape[0], im_ori.shape[1], im_ori.shape[2]])

    for channel in range(3):
        for s, scale in enumerate(scales):
            # If sigma==0, it will be automatically calculated based on scale
            im_blur[s, :, :, channel] = cv2.GaussianBlur(im_ori[:, :, channel], (0, 0), scale)
            im_mlog[s, :, :, channel] = np.log(im_ori[:, :, channel] + 1.) - np.log(im_blur[s, :, :, channel] + 1.)

    im_retinex = np.mean(im_mlog, 0)
    if do_CR:
        im_retinex = CR(im_ori, im_retinex)

    im_rtx_mean = np.mean(im_retinex)
    im_rtx_std = np.std(im_retinex)
    im_rtx_min = im_rtx_mean - dynamic * im_rtx_std
    im_rtx_max = im_rtx_mean + dynamic * im_rtx_std

    im_rtx_range = im_rtx_max - im_rtx_min

    im_out = np.uint8(np.clip((im_retinex - im_rtx_min) / im_rtx_range * 255.0, 0, 255))

    return im_out


if __name__ == '__main__':
    ####################################################################################
    # plt.close('all')
    # image_path = r'C:\pwt\图像处理\equalization\z2.jpg'
    # out_msrcr = MSRCR(image_path, max_scale=300, nscales=3, dynamic=2, do_CR=True)
    # cv2.imshow('MSRCR', out_msrcr[:, :, (2, 1, 0)])
    # out_msr = MSRCR(image_path, max_scale=300, nscales=3, dynamic=2, do_CR=False)
    # cv2.imshow('MSR', out_msr[:, :, (2, 1, 0)])
    ####################################################################################
    args = parser.parse_args()
    im_out = MSRCR(args.input, args.s, args.n, args.d)
    cv2.imwrite(args.output, im_out[:, :, (2, 1, 0)])
