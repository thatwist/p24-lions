# p24-lions

[Link to Trello board](https://trello.com/b/FtCbqxlQ/p24-lions)

Software / Stack

 * Python3
 * OpenCV 3.4
 * Google Collab integration
 
## Training on depth labels
[Tutorial](https://becominghuman.ai/tensorflow-object-detection-api-tutorial-training-and-evaluating-custom-object-detector-ed2594afcf73)

* Dataset - https://www.albert.cm/projects/viewpoint_3d_pose/

### Generating TFRecords

python generate_tfrecord.py --csv_input=data/train.csv  --output_path=data/train.record

### Preparing data

1. download and put training / testing data into depth-train/data 
2. 

### Run training 

``` bash
python legacy/train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/ssd_mobilenet_v1_coco.config
```

### Run eval

``` bash
python legacy/eval.py --logtostderr --pipeline_config_path=training/ssd_mobilenet_v1_coco.config --checkpoint_dir=training/ --eval_dir=eval/
```

## Python

 - locale problem
``` bash
export LC_ALL="en_US.UTF-8"
export LC_CTYPE="en_US.UTF-8"
sudo dpkg-reconfigure locales
```
