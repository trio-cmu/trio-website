---
layout: project
permalink: /projects/sensors/
title: Non-common sensors for robotics
subtitle: ... enabling more robust spatial intelligence 
description: We use sound, radio frequencies, and other modalities for spatial perception for redundancy and robustness in challenging environments.
image: images/photo.jpg
#external_link: https://github.com/
#repo: greenelab/lab-website-template
featured: false
tags:
  - robotics
  - optimization
  - intelligence
#More details are available in our [paper](https://ieeexplore.ieee.org/document/9844245) (also available on [arXiv](https://arxiv.org/abs/2209.04266)), published in RA-L 2022 and presented at IROS 2022 in Kyoto, and in our [blogpost](https://www.bitcraze.io/2023/01/from-crazyflies-to-crazybats/) on the Crazyflie website.
---

In past research we showed that walls can be reliably detected and avoided, based on sound only, on small robots such as the [Crazyflie](https://www.bitcraze.io/products/crazyflie-2-1/) drone, and the [e-puck2](https://e-puck.gctronic.com/) education robot, using only low-cost MEMS microphones and simple buzzers as audio signals. For reproducibility, we made the custom extension deck with microphones and a buzzer for the Crazyflie drone available open-source. 

In parallel research, we developed localization strategies for smartphones and connected devices based on radio frequencies -- WiFi, Bluetooth, and Ultra-Wideband. 

A shared problem of these non-common sensors is that they are more sparse in information than other sensors such as cameras and lidars, and thus require more careful modeling and optimization to be useful for spatial perception. We are actively exploring how to use tools from global optimization to make the most out of these non-common sensors.