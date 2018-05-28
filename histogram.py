#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

#No.0

X0 = [0.015625, 0.01513671875, 0.01318359375, 0.01416015625, 0.0166015625, 0.01025390625, 0.0166015625, 0.01220703125, 0.0068359375, 0.015625, 0.01806640625, 0.013671875, 0.0146484375, 0.01416015625, 0.01318359375, 0.01123046875, 0.01171875, 0.01513671875, 0.017578125, 0.0146484375, 0.017578125, 0.015625, 0.01025390625, 0.0205078125, 0.01513671875, 0.015625, 0.01025390625, 0.0107421875, 0.01318359375, 0.00927734375, 0.0146484375, 0.01513671875, 0.01220703125, 0.01318359375, 0.01611328125, 0.013671875, 0.0205078125, 0.01953125, 0.0146484375, 0.01708984375, 0.01708984375, 0.01611328125, 0.015625, 0.0185546875, 0.0185546875, 0.01611328125, 0.009765625, 0.015625, 0.01611328125, 0.01953125, 0.015625, 0.017578125, 0.01953125, 0.015625, 0.0185546875, 0.01806640625, 0.0166015625, 0.017578125, 0.015625, 0.01416015625, 0.0166015625, 0.01953125, 0.0166015625, 0.017578125, 0.0166015625, 0.015625, 0.0166015625, 0.01513671875, 0.0166015625, 0.01416015625, 0.017578125, 0.017578125, 0.017578125, 0.0146484375, 0.0166015625, 0.01611328125, 0.01318359375, 0.013671875, 0.015625, 0.01220703125, 0.0087890625, 0.01123046875, 0.017578125, 0.0087890625, 0.0146484375, 0.01171875, 0.0146484375, 0.015625, 0.01513671875, 0.0166015625, 0.0166015625, 0.015625, 0.0146484375, 0.0166015625, 0.013671875, 0.01318359375, 0.015625, 0.01513671875]
Y0 = [0.00048828125, -0.0048828125, -0.0029296875, -0.0029296875, -0.0048828125, 0.00146484375, -0.0029296875, -0.00390625, 0.00341796875, 0.00048828125, -0.00390625, -0.00146484375, -0.001953125, -0.001953125, -0.0029296875, -0.0009765625, -0.009765625, -0.0029296875, -0.00390625, 0.00146484375, 0.001953125, -0.0029296875, -0.001953125, -0.005859375, -0.00048828125, -0.0009765625, 0.00341796875, -0.00048828125, -0.00244140625, -0.00048828125, -0.001953125, 0.001953125, 0.00146484375, -0.00244140625, -0.009765625, -0.0078125, -0.00048828125, -0.00048828125, -0.00146484375, 0.001953125, -0.001953125, -0.005859375, -0.0029296875, -0.0029296875, -0.0029296875, -0.001953125, 0.00146484375, -0.00390625, -0.00146484375, 0.0, -0.0029296875, -0.00146484375, 0.00146484375, -0.0009765625, -0.00244140625, 0.0, -0.005859375, -0.0078125, 0.0029296875, -0.001953125, 0.00146484375, -0.00390625, -0.00048828125, -0.00390625, -0.00244140625, 0.00048828125, -0.00341796875, 0.00146484375, 0.00048828125, -0.00390625, -0.0009765625, 0.00048828125, 0.00390625, 0.00146484375, -0.00390625, 0.0, 0.00146484375, 0.0029296875, -0.0009765625, -0.00390625, -0.00146484375, -0.0029296875, -0.0009765625, -0.00048828125, -0.00048828125, -0.001953125, 0.00244140625, 0.0068359375, 0.00048828125, -0.00048828125, 0.00341796875, -0.00048828125, 0.00146484375, -0.00390625, -0.0029296875, -0.001953125, -0.00390625, -0.00048828125]
Z0 = [0.986328125, 0.98779296875, 0.99169921875, 0.98828125, 0.9892578125, 0.9833984375, 0.982421875, 0.9833984375, 0.982421875, 0.98876953125, 0.98388671875, 0.98681640625, 0.974609375, 0.9912109375, 0.984375, 0.98828125, 0.9892578125, 0.98681640625, 0.99072265625, 0.98876953125, 0.98046875, 0.9853515625, 0.98095703125, 0.9833984375, 0.986328125, 0.986328125, 0.98779296875, 0.9853515625, 0.9873046875, 0.986328125, 0.9853515625, 0.982421875, 0.982421875, 0.9853515625, 0.98681640625, 0.9833984375, 0.99169921875, 0.9736328125, 0.9853515625, 0.97705078125, 0.9853515625, 0.986328125, 0.98828125, 0.99169921875, 0.98974609375, 0.9912109375, 0.99365234375, 0.99072265625, 0.98828125, 0.99169921875, 0.98876953125, 0.98876953125, 0.99755859375, 0.98681640625, 0.98876953125, 0.99169921875, 0.9951171875, 0.98828125, 0.9853515625, 0.98828125, 0.99072265625, 0.98828125, 0.98876953125, 0.98974609375, 0.986328125, 0.986328125, 0.9892578125, 0.98974609375, 0.98828125, 0.98583984375, 0.98095703125, 0.99951171875, 0.986328125, 0.97900390625, 0.9853515625, 0.986328125, 0.98681640625, 0.99267578125, 0.97998046875, 0.98828125, 0.984375, 0.9931640625, 0.9853515625, 0.98974609375, 0.9912109375, 0.9892578125, 0.986328125, 0.9892578125, 0.9853515625, 0.9853515625, 0.98828125, 0.98828125, 0.982421875, 0.98974609375, 0.9833984375, 0.986328125, 0.99609375, 0.9873046875]
#Xµ = 0.0151; Xσ = 0.0027
#Yµ = -0.0014; Yσ = 0.0028
#Zµ = 0.9871; Zσ = 0.0042

#No.1
X1 = [0.015625, 0.01513671875, 0.01953125, 0.017578125, 0.01953125, 0.0185546875, 0.0205078125, 0.01953125, 0.01123046875, 0.0205078125, 0.015625, 0.01611328125, 0.01318359375, 0.0244140625, 0.017578125, 0.01025390625, 0.017578125, 0.0185546875, 0.0146484375, 0.017578125, 0.017578125, 0.021484375, 0.01611328125, 0.01953125, 0.01318359375, 0.009765625, 0.017578125, 0.01318359375, 0.01123046875, 0.021484375, 0.0185546875, 0.01513671875, 0.01220703125, 0.017578125, 0.01123046875, 0.0146484375, 0.0185546875, 0.01318359375, 0.0146484375, 0.01708984375, 0.01318359375, 0.01416015625, 0.01953125, 0.017578125, 0.01513671875, 0.0126953125, 0.015625, 0.017578125, 0.015625, 0.01513671875, 0.0146484375, 0.01025390625, 0.01416015625, 0.01025390625, 0.0185546875, 0.01123046875, 0.01025390625, 0.01513671875, 0.017578125, 0.01416015625, 0.01611328125, 0.009765625, 0.013671875, 0.01416015625, 0.015625, 0.0166015625, 0.01513671875, 0.01220703125, 0.0126953125, 0.015625, 0.0166015625, 0.017578125, 0.015625, 0.015625, 0.01318359375, 0.0146484375, 0.0166015625, 0.01953125, 0.01318359375, 0.01025390625, 0.01953125, 0.01318359375, 0.01513671875, 0.017578125, 0.01025390625, 0.01220703125, 0.0146484375, 0.01171875, 0.0146484375, 0.015625, 0.01806640625, 0.01416015625, 0.01171875, 0.01318359375, 0.01025390625, 0.0185546875, 0.01513671875, 0.0205078125]
Y1 = [-0.00146484375, -0.00146484375, -0.00390625, -0.00146484375, -0.0068359375, -0.005859375, -0.001953125, -0.00146484375, -0.0048828125, -0.00341796875, 0.00048828125, -0.0009765625, -0.001953125, -0.0029296875, -0.00146484375, -0.001953125, -0.001953125, -0.00439453125, -0.0029296875, -0.001953125, 0.0, -0.001953125, -0.001953125, -0.00146484375, -0.00390625, 0.00146484375, -0.00146484375, -0.00390625, -0.0009765625, -0.001953125, -0.0029296875, 0.00146484375, -0.001953125, -0.00146484375, 0.00048828125, -0.001953125, 0.0, -0.00390625, -0.005859375, 0.00048828125, 0.00048828125, -0.00146484375, -0.001953125, 0.0048828125, 0.001953125, -0.00048828125, 0.00244140625, 0.00244140625, -0.0029296875, 0.00146484375, 0.0009765625, 0.00048828125, -0.00146484375, 0.0, 0.00146484375, -0.00390625, -0.001953125, -0.00048828125, -0.00244140625, 0.001953125, 0.0048828125, -0.00390625, -0.001953125, 0.00341796875, -0.001953125, 0.001953125, -0.00146484375, -0.00048828125, -0.00390625, -0.0029296875, -0.005859375, 0.00048828125, -0.00048828125, -0.0029296875, -0.001953125, 0.0, 0.00048828125, -0.001953125, 0.00048828125, -0.00048828125, -0.0009765625, 0.00048828125, -0.001953125, -0.00146484375, 0.00048828125, 0.00146484375, -0.0029296875, -0.00390625, -0.00244140625, -0.00390625, -0.001953125, -0.001953125, -0.001953125, 0.00244140625, -0.001953125, -0.00244140625, 0.005859375, -0.00048828125]
Z1 = [0.99169921875, 0.99267578125, 0.99267578125, 0.98193359375, 0.98974609375, 0.98876953125, 0.97998046875, 0.99169921875, 0.99560546875, 0.9853515625, 0.99267578125, 0.9921875, 0.99072265625, 0.99365234375, 0.98681640625, 0.9931640625, 0.990234375, 0.9931640625, 0.99609375, 0.9921875, 0.9921875, 0.984375, 0.98828125, 0.990234375, 0.98291015625, 0.9873046875, 0.9853515625, 0.98876953125, 1.00244140625, 0.9931640625, 0.990234375, 0.986328125, 0.9892578125, 0.986328125, 0.98974609375, 0.984375, 0.9873046875, 0.9833984375, 0.9853515625, 0.984375, 0.98681640625, 0.97802734375, 0.98828125, 0.9794921875, 0.9931640625, 0.9775390625, 0.984375, 0.9892578125, 0.98779296875, 0.984375, 0.9912109375, 0.98974609375, 0.990234375, 0.9873046875, 0.98779296875, 0.984375, 0.98779296875, 0.984375, 0.984375, 0.98046875, 0.98974609375, 0.98974609375, 0.99169921875, 0.9853515625, 0.98779296875, 0.9833984375, 0.986328125, 0.9873046875, 0.98681640625, 0.99462890625, 0.9873046875, 0.9873046875, 0.99072265625, 0.9892578125, 0.98974609375, 0.9853515625, 0.9892578125, 0.982421875, 0.98583984375, 0.98828125, 0.9833984375, 0.9853515625, 0.9873046875, 0.98486328125, 0.98046875, 0.98046875, 0.9892578125, 0.98779296875, 0.98974609375, 0.98828125, 0.984375, 0.98828125, 0.98876953125, 0.99169921875, 0.9951171875, 0.99267578125, 0.9833984375, 0.99072265625]
#Xµ = 0.0154; Xσ = 0.0031
#Yµ = -0.0012; Yσ = 0.0023
#Zµ = 0.9880; Zσ = 0.0042

#No. 2
X2 = [0.0146484375, 0.015625, 0.0166015625, 0.015625, 0.01416015625, 0.0166015625, 0.015625, 0.0166015625, 0.015625, 0.015625, 0.01513671875, 0.0185546875, 0.01416015625, 0.01025390625, 0.0166015625, 0.009765625, 0.0166015625, 0.015625, 0.01611328125, 0.01123046875, 0.0146484375, 0.01611328125, 0.017578125, 0.01220703125, 0.015625, 0.0166015625, 0.015625, 0.01318359375, 0.01953125, 0.01611328125, 0.01416015625, 0.01220703125, 0.01953125, 0.0166015625, 0.02294921875, 0.015625, 0.01953125, 0.017578125, 0.0224609375, 0.0185546875, 0.0185546875, 0.015625, 0.01513671875, 0.01318359375, 0.0166015625, 0.015625, 0.01953125, 0.0146484375, 0.0185546875, 0.01513671875, 0.0166015625, 0.015625, 0.01611328125, 0.02099609375, 0.0166015625, 0.015625, 0.0166015625, 0.017578125, 0.0107421875, 0.01123046875, 0.021484375, 0.01416015625, 0.017578125, 0.01318359375, 0.017578125, 0.01416015625, 0.01611328125, 0.0146484375, 0.01123046875, 0.01416015625, 0.01416015625, 0.01318359375, 0.0185546875, 0.015625, 0.015625, 0.01416015625, 0.009765625, 0.015625, 0.01611328125, 0.01220703125, 0.0166015625, 0.015625, 0.015625, 0.015625, 0.01025390625, 0.01416015625, 0.01318359375, 0.015625, 0.01318359375, 0.0146484375, 0.01220703125, 0.0166015625, 0.0185546875, 0.01611328125, 0.017578125, 0.0166015625, 0.015625, 0.015625]
Y2 = [-0.00244140625, -0.001953125, -0.001953125, 0.00244140625, -0.0029296875, -0.01171875, -0.00390625, -0.00146484375, -0.005859375, -0.00244140625, 0.001953125, -0.00146484375, -0.005859375, -0.0029296875, 0.001953125, 0.00048828125, -0.00390625, -0.0048828125, -0.0068359375, -0.00048828125, -0.001953125, -0.0029296875, -0.00048828125, -0.0029296875, -0.001953125, -0.00048828125, -0.0068359375, -0.001953125, -0.00146484375, -0.00146484375, -0.001953125, -0.0009765625, -0.00390625, 0.00146484375, -0.00048828125, -0.00146484375, 0.0029296875, -0.001953125, 0.00244140625, 0.00048828125, 0.00146484375, -0.00048828125, 0.00048828125, -0.00048828125, -0.0029296875, -0.0009765625, -0.00048828125, -0.00244140625, 0.00048828125, 0.0, 0.00048828125, -0.00390625, -0.0009765625, 0.00146484375, -0.0029296875, -0.00048828125, 0.00146484375, -0.0009765625, 0.0, -0.00341796875, 0.00146484375, 0.001953125, -0.0048828125, 0.0, 0.001953125, 0.001953125, 0.00146484375, -0.0048828125, -0.00048828125, -0.00048828125, 0.00048828125, -0.001953125, 0.00732421875, -0.00146484375, -0.00146484375, -0.0048828125, 0.00048828125, -0.00048828125, -0.0009765625, -0.00439453125, -0.001953125, -0.00146484375, -0.00732421875, 0.00048828125, -0.0009765625, -0.00390625, -0.00048828125, -0.00244140625, -0.00146484375, -0.00341796875, 0.001953125, -0.00146484375, 0.00146484375, 0.00048828125, -0.00244140625, -0.00048828125, -0.0009765625, 0.00146484375]
Z2 = [0.98828125, 0.98779296875, 0.99658203125, 0.984375, 0.98681640625, 0.97998046875, 0.9853515625, 0.98974609375, 0.9873046875, 0.9970703125, 0.99609375, 0.99169921875, 0.99169921875, 0.984375, 0.98828125, 0.984375, 0.986328125, 0.9873046875, 0.99072265625, 0.9853515625, 0.9814453125, 0.99072265625, 0.9951171875, 0.98583984375, 0.98828125, 0.9853515625, 0.98193359375, 0.978515625, 0.98681640625, 0.9873046875, 0.98974609375, 0.99169921875, 0.98828125, 0.9873046875, 0.9873046875, 0.986328125, 0.986328125, 0.98779296875, 0.986328125, 0.98828125, 0.98974609375, 0.984375, 0.982421875, 0.98779296875, 0.99267578125, 0.99267578125, 0.99609375, 0.99169921875, 0.99169921875, 0.99267578125, 0.99169921875, 0.98828125, 0.98974609375, 0.990234375, 0.99169921875, 0.99169921875, 0.9892578125, 0.99169921875, 0.98193359375, 0.9853515625, 0.97802734375, 0.9912109375, 0.99072265625, 0.98876953125, 0.98095703125, 0.98291015625, 0.9833984375, 0.98876953125, 0.9921875, 0.986328125, 0.98828125, 0.986328125, 0.98876953125, 0.9853515625, 0.9794921875, 0.98828125, 0.98681640625, 0.98779296875, 0.98681640625, 0.9873046875, 0.9833984375, 0.990234375, 0.9833984375, 0.984375, 0.982421875, 0.9873046875, 0.98291015625, 0.984375, 0.9873046875, 0.990234375, 0.9853515625, 0.9873046875, 0.98291015625, 0.9951171875, 0.9873046875, 0.9873046875, 0.9765625, 0.99267578125]
#Xµ = 0.0156; Xσ = 0.0025
#Yµ = -0.0013; Yσ = 0.0026
#Zµ = 0.9876; Zσ = 0.0041

#No.3
X3 = [0.017578125, 0.017578125, 0.017578125, 0.0166015625, 0.01953125, 0.0185546875, 0.01708984375, 0.01416015625, 0.0205078125, 0.01953125, 0.01611328125, 0.0205078125, 0.01220703125, 0.0185546875, 0.015625, 0.017578125, 0.0185546875, 0.00927734375, 0.0205078125, 0.01953125, 0.0185546875, 0.0185546875, 0.0185546875, 0.0185546875, 0.017578125, 0.0166015625, 0.0185546875, 0.021484375, 0.01953125, 0.015625, 0.0166015625, 0.0078125, 0.01318359375, 0.017578125, 0.01513671875, 0.01953125, 0.013671875, 0.01318359375, 0.015625, 0.01953125, 0.00927734375, 0.01025390625, 0.01318359375, 0.015625, 0.015625, 0.01611328125, 0.017578125, 0.00830078125, 0.01025390625, 0.01318359375, 0.01416015625, 0.01513671875, 0.01123046875, 0.00927734375, 0.01513671875, 0.01513671875, 0.01318359375, 0.01025390625, 0.01318359375, 0.01318359375, 0.015625, 0.0126953125, 0.0078125, 0.01513671875, 0.01025390625, 0.01171875, 0.0205078125, 0.01416015625, 0.01318359375, 0.015625, 0.0146484375, 0.0107421875, 0.0087890625, 0.0146484375, 0.01513671875, 0.01318359375, 0.015625, 0.01708984375, 0.01318359375, 0.0185546875, 0.017578125, 0.0185546875, 0.0146484375, 0.01416015625, 0.01171875, 0.0185546875, 0.01416015625, 0.0166015625, 0.0205078125, 0.01416015625, 0.017578125, 0.01318359375, 0.0205078125, 0.01806640625, 0.01171875, 0.01416015625, 0.01416015625, 0.01953125]
Y3 = [-0.0029296875, 0.00048828125, -0.00146484375, -0.001953125, -0.0029296875, -0.00390625, -0.001953125, 0.0048828125, 0.0029296875, -0.0009765625, -0.0029296875, -0.00390625, -0.0029296875, -0.00341796875, -0.00048828125, 0.00048828125, -0.00146484375, -0.00048828125, -0.00146484375, -0.0048828125, -0.0029296875, -0.00146484375, 0.0048828125, -0.0029296875, -0.00146484375, -0.00390625, 0.00048828125, 0.00146484375, -0.01123046875, -0.00830078125, -0.0048828125, -0.0048828125, -0.0029296875, 0.00244140625, -0.00341796875, -0.00341796875, 0.00244140625, 0.001953125, -0.00390625, -0.0048828125, -0.00390625, -0.0048828125, -0.00537109375, -0.00146484375, 0.00244140625, 0.00048828125, -0.001953125, -0.0048828125, 0.00390625, -0.00048828125, -0.00048828125, 0.00048828125, -0.00146484375, 0.00390625, 0.00146484375, 0.0029296875, 0.00390625, 0.00146484375, 0.00146484375, 0.00146484375, -0.00048828125, -0.0048828125, -0.0009765625, 0.00390625, 0.00390625, -0.0009765625, -0.0009765625, -0.00048828125, -0.0029296875, 0.00048828125, -0.001953125, -0.0048828125, 0.0009765625, 0.0009765625, 0.0009765625, -0.00244140625, 0.00244140625, -0.001953125, -0.00146484375, -0.00146484375, 0.00048828125, -0.0029296875, -0.0029296875, -0.001953125, 0.00048828125, 0.0, 0.00146484375, -0.00048828125, 0.0, -0.00244140625, 0.0, 0.00048828125, -0.00146484375, -0.00048828125, 0.001953125, -0.0009765625, -0.00390625, -0.0009765625]
Z3 = [0.9873046875, 0.9873046875, 0.9951171875, 0.99267578125, 0.99072265625, 0.99072265625, 0.986328125, 0.9931640625, 0.99169921875, 0.994140625, 0.98974609375, 0.99609375, 0.99169921875, 0.99072265625, 0.99365234375, 0.98974609375, 0.99072265625, 0.9892578125, 0.98779296875, 0.9931640625, 0.9931640625, 0.984375, 0.98095703125, 0.98876953125, 0.98779296875, 0.9921875, 0.9833984375, 0.9833984375, 0.984375, 0.98876953125, 0.9853515625, 0.98828125, 0.99072265625, 0.982421875, 0.98974609375, 0.9921875, 0.9873046875, 0.984375, 0.9892578125, 0.97998046875, 0.98681640625, 0.97900390625, 0.986328125, 0.97998046875, 0.9775390625, 0.98974609375, 0.98876953125, 0.99169921875, 0.990234375, 0.9833984375, 0.982421875, 0.986328125, 0.9833984375, 0.9833984375, 0.98291015625, 0.98974609375, 0.986328125, 0.97705078125, 0.97998046875, 0.984375, 0.98193359375, 0.98974609375, 0.9833984375, 0.986328125, 0.97802734375, 0.9873046875, 0.9833984375, 0.98974609375, 0.98828125, 0.984375, 0.9873046875, 0.9833984375, 0.9833984375, 0.986328125, 0.9873046875, 0.9833984375, 0.98291015625, 0.98876953125, 0.9833984375, 0.9931640625, 0.986328125, 0.99072265625, 0.99267578125, 0.98876953125, 0.9833984375, 0.98828125, 0.98974609375, 0.99072265625, 0.98681640625, 0.98974609375, 0.9833984375, 0.99169921875, 0.98974609375, 0.99169921875, 0.99365234375, 0.99951171875, 0.9951171875, 0.9829101562]
#Xµ = 0.0154; Xσ = 0.0033
#Yµ = -0.0011; Yσ = 0.0028
#Zµ = 0.9875; Zσ = 0.0044

#No 4
X4 = [0.021484375, 0.0166015625, 0.01513671875, 0.0166015625, 0.01025390625, 0.0107421875, 0.0185546875, 0.017578125, 0.01318359375, 0.013671875, 0.01416015625, 0.0146484375, 0.01416015625, 0.0166015625, 0.01123046875, 0.01123046875, 0.009765625, 0.01953125, 0.015625, 0.01318359375, 0.01220703125, 0.01220703125, 0.01220703125, 0.01123046875, 0.0107421875, 0.015625, 0.01123046875, 0.017578125, 0.017578125, 0.01025390625, 0.01318359375, 0.01513671875, 0.0166015625, 0.01513671875, 0.01708984375, 0.015625, 0.015625, 0.015625, 0.02294921875, 0.017578125, 0.0166015625, 0.017578125, 0.0185546875, 0.01953125, 0.0185546875, 0.0205078125, 0.0185546875, 0.00927734375, 0.01318359375, 0.0185546875, 0.0185546875, 0.01513671875, 0.01513671875, 0.0166015625, 0.017578125, 0.015625, 0.0205078125, 0.01513671875, 0.01513671875, 0.015625, 0.0146484375, 0.01220703125, 0.0166015625, 0.01318359375, 0.01123046875, 0.0146484375, 0.01220703125, 0.0146484375, 0.01171875, 0.01318359375, 0.0146484375, 0.01416015625, 0.01220703125, 0.015625, 0.015625, 0.0166015625, 0.01416015625, 0.017578125, 0.015625, 0.0166015625, 0.013671875, 0.0146484375, 0.01416015625, 0.01220703125, 0.0166015625, 0.017578125, 0.013671875, 0.01220703125, 0.0185546875, 0.01708984375, 0.01220703125, 0.017578125, 0.0185546875, 0.01025390625, 0.015625, 0.01318359375, 0.01025390625, 0.0185546875]
Y4 = [-0.00048828125, 0.0029296875, -0.001953125, -0.0029296875, 0.001953125, 0.00341796875, -0.0009765625, -0.00048828125, -0.0029296875, 0.00048828125, 0.00048828125, 0.00048828125, 0.00146484375, 0.00048828125, -0.0009765625, 0.00048828125, -0.0029296875, 0.00537109375, 0.00341796875, 0.00341796875, 0.00048828125, 0.0048828125, 0.00244140625, -0.00048828125, -0.00048828125, 0.00341796875, 0.00048828125, 0.001953125, 0.00048828125, -0.001953125, -0.0029296875, -0.00146484375, 0.00390625, -0.00390625, -0.00244140625, -0.00048828125, 0.0, -0.0009765625, 0.00439453125, 0.0, -0.0048828125, -0.00341796875, -0.001953125, -0.001953125, -0.0029296875, -0.0068359375, -0.009765625, -0.0048828125, -0.00244140625, -0.00244140625, -0.00830078125, 0.00048828125, -0.00390625, -0.005859375, 0.00048828125, 0.0048828125, -0.001953125, 0.0, -0.00048828125, 0.00048828125, 0.00048828125, -0.00390625, -0.0068359375, -0.0068359375, -0.00390625, -0.005859375, -0.00244140625, 0.00048828125, -0.00390625, -0.001953125, -0.00048828125, 0.001953125, 0.001953125, 0.0048828125, 0.00146484375, -0.0009765625, 0.00048828125, 0.001953125, 0.0, -0.00048828125, -0.00146484375, 0.00048828125, 0.00244140625, -0.00390625, 0.0009765625, -0.0029296875, -0.0029296875, -0.00390625, -0.001953125, 0.00341796875, 0.00048828125, 0.00244140625, 0.005859375, 0.0009765625, 0.00048828125, -0.00146484375, -0.005859375, -0.001953125]
Z4 = [0.9833984375, 0.984375, 0.9853515625, 0.97900390625, 0.986328125, 0.98779296875, 0.98583984375, 0.9853515625, 0.9853515625, 0.98779296875, 0.99609375, 0.98974609375, 0.9833984375, 0.982421875, 0.9892578125, 0.984375, 0.9873046875, 0.98828125, 0.98974609375, 0.984375, 0.9873046875, 0.99072265625, 0.9873046875, 0.9931640625, 0.9970703125, 0.98828125, 0.986328125, 0.984375, 0.98828125, 0.9853515625, 0.9873046875, 0.9853515625, 0.986328125, 0.98046875, 0.9853515625, 0.98828125, 0.982421875, 0.9853515625, 0.9873046875, 0.99169921875, 0.98193359375, 0.97900390625, 0.984375, 0.97802734375, 0.9853515625, 0.9814453125, 0.982421875, 0.98828125, 0.9931640625, 0.982421875, 0.99169921875, 0.98681640625, 0.986328125, 0.9892578125, 0.9853515625, 0.99072265625, 0.990234375, 0.982421875, 0.99072265625, 0.9931640625, 0.99267578125, 0.9931640625, 0.98583984375, 0.98974609375, 0.98974609375, 0.9873046875, 0.99072265625, 0.990234375, 0.99072265625, 0.98828125, 0.9912109375, 0.9873046875, 0.9921875, 0.986328125, 0.9873046875, 0.9892578125, 0.98681640625, 0.986328125, 0.990234375, 0.97802734375, 0.974609375, 0.9775390625, 0.98681640625, 0.98974609375, 0.98828125, 0.984375, 0.984375, 0.982421875, 0.9873046875, 0.98876953125, 0.9873046875, 0.98681640625, 0.9794921875, 0.9853515625, 0.98828125, 0.9853515625, 0.9853515625, 0.98828125]
#Xµ = 0.0151; Xσ = 0.0028
#Yµ = -0.0007; Yσ = 0.0031
#Zµ = 0.9867; Zσ = 0.0040

#No. 5
X5 = [0.009765625, 0.0205078125, 0.0146484375, 0.015625, 0.021484375, 0.0146484375, 0.015625, 0.0146484375, 0.01953125, 0.015625, 0.0126953125, 0.01416015625, 0.01171875, 0.0166015625, 0.017578125, 0.01318359375, 0.013671875, 0.01416015625, 0.01123046875, 0.01416015625, 0.01708984375, 0.015625, 0.0126953125, 0.01953125, 0.017578125, 0.01025390625, 0.017578125, 0.0107421875, 0.0107421875, 0.0146484375, 0.01025390625, 0.01416015625, 0.0078125, 0.01416015625, 0.0068359375, 0.0087890625, 0.0078125, 0.01025390625, 0.01220703125, 0.01318359375, 0.01318359375, 0.01123046875, 0.01318359375, 0.00927734375, 0.013671875, 0.01171875, 0.0126953125, 0.01318359375, 0.0087890625, 0.013671875, 0.015625, 0.01416015625, 0.01171875, 0.01318359375, 0.01318359375, 0.01220703125, 0.01513671875, 0.015625, 0.0185546875, 0.017578125, 0.01513671875, 0.0146484375, 0.01416015625, 0.013671875, 0.017578125, 0.01513671875, 0.01416015625, 0.0185546875, 0.01953125, 0.0185546875, 0.0185546875, 0.013671875, 0.017578125, 0.0224609375, 0.017578125, 0.0205078125, 0.0205078125, 0.017578125, 0.015625, 0.021484375, 0.01611328125, 0.0185546875, 0.01953125, 0.0234375, 0.0185546875, 0.0244140625, 0.02099609375, 0.0224609375, 0.02392578125, 0.0224609375, 0.015625, 0.01953125, 0.0185546875, 0.0205078125, 0.0224609375, 0.01953125, 0.0205078125, 0.0185546875]
Y5 = [0.00244140625, 0.00244140625, -0.00048828125, -0.00048828125, 0.00048828125, -0.0029296875, -0.001953125, 0.00146484375, -0.0009765625, -0.001953125, -0.001953125, -0.005859375, -0.0029296875, 0.00048828125, 0.0, 0.00244140625, 0.00390625, -0.0009765625, 0.005859375, 0.00341796875, -0.001953125, 0.0, 0.0068359375, -0.0029296875, 0.0009765625, 0.00048828125, -0.0029296875, 0.00048828125, 0.0, -0.00048828125, 0.00390625, 0.00390625, 0.001953125, 0.005859375, -0.00048828125, 0.00341796875, -0.00048828125, 0.005859375, -0.00048828125, 0.00390625, -0.00048828125, -0.001953125, 0.0029296875, 0.00244140625, -0.001953125, -0.0029296875, 0.001953125, 0.0, -0.00341796875, 0.00146484375, -0.00390625, -0.001953125, 0.00146484375, -0.00146484375, -0.00146484375, -0.00048828125, 0.0, -0.0009765625, 0.001953125, -0.0048828125, -0.005859375, -0.005859375, 0.00048828125, -0.0009765625, -0.0029296875, -0.00390625, -0.0048828125, -0.001953125, -0.0048828125, -0.005859375, 0.00146484375, -0.00048828125, -0.001953125, -0.0068359375, 0.0, -0.005859375, -0.001953125, -0.0009765625, -0.00048828125, -0.0029296875, -0.01123046875, -0.005859375, -0.00732421875, -0.00390625, -0.0048828125, -0.00048828125, -0.0029296875, -0.0048828125, 0.0, -0.00244140625, -0.001953125, -0.0048828125, -0.0068359375, -0.00048828125, -0.00390625, -0.0029296875, -0.0009765625, -0.00341796875]
Z5 = [0.994140625, 0.994140625, 0.99169921875, 0.9833984375, 0.99072265625, 0.98779296875, 0.984375, 0.9892578125, 0.98974609375, 0.982421875, 0.986328125, 0.9853515625, 0.984375, 0.986328125, 0.9833984375, 0.9892578125, 0.9833984375, 0.9833984375, 0.97998046875, 0.9814453125, 0.984375, 0.99072265625, 0.986328125, 0.9912109375, 0.986328125, 0.982421875, 0.982421875, 0.986328125, 0.990234375, 0.984375, 0.9814453125, 0.9853515625, 0.984375, 0.9892578125, 0.98193359375, 0.982421875, 0.984375, 0.98779296875, 0.982421875, 0.97998046875, 0.9833984375, 0.986328125, 0.97998046875, 0.974609375, 0.9853515625, 0.97802734375, 0.98046875, 0.986328125, 0.984375, 0.98388671875, 0.9853515625, 0.98974609375, 0.984375, 0.98095703125, 0.986328125, 0.98681640625, 0.9853515625, 0.9833984375, 0.99462890625, 0.99609375, 0.98291015625, 0.98291015625, 0.98095703125, 0.984375, 0.9853515625, 0.9921875, 0.9912109375, 0.9853515625, 0.98681640625, 0.9892578125, 0.98974609375, 0.986328125, 0.99072265625, 0.99267578125, 0.98486328125, 0.99853515625, 0.9853515625, 0.9833984375, 0.97802734375, 0.9814453125, 0.9873046875, 0.994140625, 0.98828125, 0.9873046875, 0.9873046875, 0.99169921875, 0.98828125, 0.98974609375, 0.99072265625, 0.98876953125, 0.994140625, 0.98974609375, 0.9892578125, 0.99072265625, 0.98779296875, 0.9833984375, 0.99267578125, 0.98974609375]
#Xµ = 0.0156; Xσ = 0.0039
#Yµ = -0.0011; Yσ = 0.0032
#Zµ = 0.9865; Zσ = 0.0043
def plotHist(axis, data, set):
    plt.figure(1, figsize=(10, 6))

    # the histogram of the data
    n, bins, patches = plt.hist(data, 'doane', normed=True, facecolor='green', alpha=0.75)
    bin_centres = 0.5*(bins[1:]+bins[:-1])
    print(bin_centres)


    sigma = np.std(data)
    mu = np.mean(data)

    print("µ = {:.4f}; σ = {:.4f}".format(mu, sigma))

    # add a 'best fit' line
    my_norm = norm(mu, sigma)
    l = plt.plot(bin_centres, my_norm.pdf(bin_centres), 'r--', linewidth=1)
    plt.xlabel('Values of acceleration in {}-direction, g'.format(axis))
    plt.ylabel('Frequency Density')
    plt.title('Histogram of noise in {} Axis results\n µ = {:.4f}g; σ ={:.4f}g'.format(axis, mu, sigma))

    plt.savefig("../../Figures/histogram_{}_{}.png".format(set, axis))

def plotPoints(axis, data, set):
    plt.plot(data)
    plt.plot(data, 'bo')
    plt.ylabel('{} axis acceleration in g'.format(axis))
    plt.savefig("../../Figures/time_points_{}_{}.png".format(set, axis))


#plotHist('X', X0, 0)
#plotHist('Y', Y0,  0)
#plotHist('Z', Z0, 0)

#plotPoints('X', X5, 5)
#plotPoints('Y', Y5,  5)
#plotPoints('Z', Z5, 5)
