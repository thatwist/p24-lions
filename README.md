# p24-lions

[Link to Trello board](https://trello.com/b/FtCbqxlQ/p24-lions)

## Software / Stack

 * Python3
 * OpenCV 3.4
 * GCP with GPUs
 
## Dataset

 1. https://www.albert.cm/projects/viewpoint_3d_pose/
 2. http://vrai.dii.univpm.it/re-id-dataset
 3. https://www.albert.cm/projects/ram_person_id/
 
 dataset/ - cut heads dataset
 
## Final pipeline
final-take2/
 
## Presentation

https://docs.google.com/presentation/d/14u4VbT3fY137V4mZnPOO8NkiWFpT-450tGD39dheFoE/edit?usp=sharing
 
## Tensorflow Object Detection API
[Tutorial](https://becominghuman.ai/tensorflow-object-detection-api-tutorial-training-and-evaluating-custom-object-detector-ed2594afcf73)

[Installation](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md)

* Dataset - https://www.albert.cm/projects/viewpoint_3d_pose/

### Generating TFRecords

python generate_tfrecord.py --csv_input=data/train.csv  --output_path=data/train.record

### Preparing data

1. download and put training / testing data into depth-train/data  (h5 files for depth-map, labels for train/test - 4 files)
2. generate csv files using `generate_csv_labels` function from prepare-dataset.ipynb
3. generate tfrecord files from csvs using generate_tfrecord.py (see above)
4. follow tutorial to prepare config files

### Run training 

``` bash
python legacy/train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/ssd_mobilenet_v1_coco.config
```

### Run eval

``` bash
python legacy/eval.py --logtostderr --pipeline_config_path=training/ssd_mobilenet_v1_coco.config --checkpoint_dir=training/ --eval_dir=eval/
```
eval parameters:
https://github.com/tensorflow/models/blob/abd504235f3c2eed891571d62f0a424e54a2dabc/research/object_detection/protos/eval.proto#L8

### Run tensorboard monitoring (for evaluation)

``` bash
tensorboard --logdir=eval
```

### Export model

``` bash
python export_inference_graph.py --input_type image_tensor --pipeline_config_path=training/ssd_mobilenet_v1_coco.config --trained_checkpoint_prefix=training/model.ckpt-400 --output_directory output
```

## Python

 - locale problem
``` bash
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales
```

###
