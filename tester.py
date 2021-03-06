import os
import numpy as np
import tensorflow as tf
import lib.dataset as dataset
import lib.network as network
import lib.utils as utils
import lib.vis as vis


if __name__ == '__main__':

    EPOCH_DIR = "/Users/micmelesse/Documents/3D-reconstruction-with-neural-networks/aws/model_2018-03-15_18:04:43_L:0.001_E:10_B:16/epoch_5"

    # X_test, y_test = dataset.load_model_testset(EPOCH_DIR)
    X_test, y_test = dataset.get_preprocessed_dataset()

    # network restore to specific epoch
    net = network.Network_restored(EPOCH_DIR)
    batch_size = utils.read_params()["TRAIN_PARAMS"]["BATCH_SIZE"]
    # split test set into batchs
    X_test_batchs, y_test_batchs = dataset.get_suffeled_batchs(
        X_test, y_test, batch_size)

    print("testing network ...")
    # test network
    i = 0
    while X_test_batchs and y_test_batchs:
        i += 1
        X = dataset.from_npy(X_test_batchs.popleft())
        y = dataset.from_npy(y_test_batchs.popleft())
        y_hat = net.predict(X)

        vis.multichannel(
            X[0][1], "feature_maps_{}.png".format(i))
        vis.voxel(
            y[0], "/target_{}.png".format(i))
        vis.voxel(
            y_hat[0], "/prediction_{}.png".format(i))
    print("... done")
