# satellite-image-mapper-3000

## Table of Contents
- [Introduction](#introduction)
- [Training](#training)
- [Results](#results)
- [Dataset](#dataset)
- [Inspiration](#inspiration)

## Introduction

This project involves the transformation of satellite images into detailed maps using various neural network techniques. The primary goal is to leverage Generative Adversarial Networks (GANs) to accurately convert satellite imagery into useful map data. The project explores several GAN architectures, including Cycle-GAN, SAM-GAN, [Pix2Pix](https://arxiv.org/pdf/1611.07004) and Geo-GAN.

## Training

We trained our models on pictures resized to 256x256 px.


## Results

Below are examples of the model's output at various epochs during the training process.

### CycleGAN
| real satellite image | real maps image                                          | 5th epoch | 50th epoch                                    | 100th epoch                                    | 150th epoch                                    | 200th epoch                                    | 
|----------------------|----------------------------------------------------------|-----------|-----------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|
| ![real_satellite_image](docs/images/cycle-gan/real-0.png) | ![real_maps_image](docs/images/cycle-gan/real-map-0.png) | ![5th_epoch](docs/images/cycle-gan/5-0.png) | ![10th_epoch](docs/images/cycle-gan/50-0.png) | ![15th_epoch](docs/images/cycle-gan/100-0.png) | ![20th_epoch](docs/images/cycle-gan/150-0.png) | ![25th_epoch](docs/images/cycle-gan/200-0.png) |
| ![real_satellite_image](docs/images/cycle-gan/real-1.png) | ![real_maps_image](docs/images/cycle-gan/real-map-1.png) | ![5th_epoch](docs/images/cycle-gan/5-1.png) | ![10th_epoch](docs/images/cycle-gan/50-1.png) | ![15th_epoch](docs/images/cycle-gan/100-1.png) | ![20th_epoch](docs/images/cycle-gan/150-1.png) | ![25th_epoch](docs/images/cycle-gan/200-1.png) |

### SamGAN
| real satellite image | real maps image                                          | 5th epoch | 50th epoch                                    | 100th epoch                                    | 150th epoch                                    | 200th epoch                                    | 
|----------------------|----------------------------------------------------------|-----------|-----------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|
| ![real_satellite_image](docs/images/sam-gan/epoch_1_last_batch.png) | ![real_maps_image](docs/images/sam-gan/org_map2.png) | ![5th_epoch](docs/images/sam-gan/epoch_1_last_batchgen2.png) | ![10th_epoch](docs/images/sam-gan/epoch_5_last_batchgen2.png) | ![15th_epoch](docs/images/sam-gan/epoch_50_last_batchgen2.png) | ![20th_epoch](docs/images/sam-gan/epoch_100_last_batchgen2.png) | ![25th_epoch](docs/images/sam-gan/epoch_199_last_batchgen2.png) |
| ![real_satellite_image](docs/images/sam-gan/epoch_1_last_batch2.png) | ![real_maps_image](docs/images/sam-gan/org_map.png) | ![5th_epoch](docs/images/sam-gan/epoch_1_last_batchgen.png) | ![10th_epoch](docs/images/sam-gan/epoch_5_last_batchgen.png) | ![15th_epoch](docs/images/sam-gan/epoch_50_last_batchgen.png) | ![20th_epoch](docs/images/sam-gan/epoch_100_last_batchgen.png) | ![25th_epoch](docs/images/sam-gan/epoch_199_last_batchgen.png) |

### pix2pix
| real satellite image | real maps image                                          | 5th epoch | 50th epoch                                    | 100th epoch                                    | 150th epoch                                    | 200th epoch                                    | 
|----------------------|----------------------------------------------------------|-----------|-----------------------------------------------|------------------------------------------------|------------------------------------------------|------------------------------------------------|
| ![real_satellite_image](docs/images/pix2pix/sample1_input.png) | ![real_maps_image](docs/images/pix2pix/sample1_output.png) | ![5th_epoch](docs/images/pix2pix/sample1_epoch_5.png) | ![10th_epoch](docs/images/pix2pix/sample1_epoch_50.png) | ![15th_epoch](docs/images/pix2pix/sample1_epoch_100.png) | ![20th_epoch](docs/images/pix2pix/sample1_epoch_150.png) | ![25th_epoch](docs/images/pix2pix/sample1_epoch_200.png) |
| ![real_satellite_image](docs/images/pix2pix/sample2_input.png) | ![real_maps_image](docs/images/pix2pix/sample2_output.png) | ![5th_epoch](docs/images/pix2pix/sample2_epoch_5.png) | ![10th_epoch](docs/images/pix2pix/sample2_epoch_50.png) | ![15th_epoch](docs/images/pix2pix/sample2_epoch_100.png) | ![20th_epoch](docs/images/pix2pix/sample2_epoch_150.png) | ![25th_epoch](docs/images/pix2pix/sample2_epoch_200.png) |

## Dataset
The dataset used in this project consists of satellite images and their corresponding maps. The data was sourced from https://www.kaggle.com/datasets/vikramtiwari/pix2pix-dataset, which provides high-resolution (1200x1200) satellite imagery and accurately annotated maps. The dataset is organized into training and validation sets.

## Inspiration

We were inspired by https://arxiv.org/pdf/1703.10593


