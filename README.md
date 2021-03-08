# STTN for Video Inpainting
![teaser](https://github.com/researchmm/STTN/blob/master/docs/teaser.png?raw=true)

### [Paper](https://arxiv.org/abs/2007.10247) | [Demo](https://www.youtube.com/watch?v=tgiWGdr1SnE&feature=youtu.be) | [Video](https://drive.google.com/file/d/19eKm4AJhIbJAbvXyA-HTQHFdia7XcN6H/view?usp=sharing) | [Slides](https://drive.google.com/file/d/1y09-SLcTadqpuDDLSzFdtr3ymGbjrmyi/view?usp=sharing) |[BibTex](https://github.com/researchmm/STTN#citation)

Learning Joint Spatial-Temporal Transformations for Video Inpainting<br>

[Yanhong Zeng](https://sites.google.com/view/1900zyh),  [Jianlong Fu](https://jianlong-fu.github.io/), and [Hongyang Chao](https://scholar.google.com/citations?user=qnbpG6gAAAAJ&hl).<br>
In ECCV 2020.


## Installation  

Clone this repo.

```
git clone git@github.com:researchmm/STTN.git
cd STTN/
```

**MTL Note**
  - Installing with the provided environment.yml does not work for me. It's probably the issue with the different version of Ubuntu and packes.
    - So first create a new conda environment (e.g. named `sttn`)
    - Run the test script and install missing packes until it can run

<details>

  <summary> Original Instruction</summary>
We build our project based on Pytorch and Python. For the full set of required Python packages, we suggest create a Conda environment from the provided YAML, e.g.

```
conda env create -f environment.yml 
conda activate sttn
```

</details>

<!-- ---------------------------------------------- -->
## Completing Videos Using Pretrained Model

The result videos can be generated using pretrained models. 
For your reference, we provide a model pretrained on Youtube-VOS([Google Drive Folder](https://drive.google.com/file/d/1ZAMV8547wmZylKRt5qR_tC5VlosXD4Wv/view?usp=sharing)). 

1. Download the pretrained models from the [Google Drive Folder](https://drive.google.com/file/d/1ZAMV8547wmZylKRt5qR_tC5VlosXD4Wv/view?usp=sharing), save it in ```checkpoints/```. 

2. Complete videos using the pretrained model. For example, 

```
python test.py --video examples/schoolgirls_orig.mp4 --mask examples/schoolgirls  --ckpt checkpoints/sttn.pth 
```
The outputs videos are saved at ```examples/```. 

**MTL Notes**
  - The provided code use GPU ID = 1 by default. That will cause error if run on machine with only one GPU.
    - Fix code in the test.py file

<!-- ---------------------------------------------- -->

<details>
  <summary>Instructions for preparing the dataset and training the model</summary>

## Dataset Preparation

We provide dataset split in ```datasets/```. 

**Preparing Youtube-VOS (2018) Dataset.** The dataset can be downloaded from [here](https://competitions.codalab.org/competitions/19544#participate-get-data). In particular, we follow the standard train/validation/test split (3,471/474/508). The dataset should be arranged in the same directory structure as 

```
datasets
    ｜- youtube-vos
        |- JPEGImages
           |- <video_id>.zip
           |- <video_id>.zip
        |- test.json 
        |- train.json 
``` 

**Preparing DAVIS (2018) Dataset.** The dataset can be downloaded from [here](https://davischallenge.org/davis2017/code.html). In particular, there are 90 videos with densely-annotated object masks and 60 videos without annotations. The dataset should be arranged in the same directory structure as

```
datasets
    ｜- davis
        |- JPEGImages
          |- cows.zip
          |- goat.zip
        |- Annoatations
          |- cows.zip
          |- goat.zip
        |- test.json 
        |- train.json 
``` 


<!-- ---------------------------------------------- -->
## Training New Models
Once the dataset is ready, new models can be trained with the following commands. For example, 

```
python train.py --config configs/youtube-vos.json --model sttn 
```

<!-- ---------------------------------------------- -->
## Testing

Testing is similar to [Completing Videos Using Pretrained Model](https://github.com/researchmm/STTN#completing-videos-using-pretrained-model).

```
python test.py --video examples/schoolgirls_orig.mp4 --mask examples/schoolgirls  --ckpt checkpoints/sttn.pth 
```
The outputs videos are saved at ```examples/```. 

<!-- ---------------------------------------------- -->
## Visualization 

We provide an example of visualization attention maps in ```visualization.ipynb```. 


<!-- ---------------------------------------------- -->
## Training Monitoring  

We provide traning monitoring on losses by running: 
```
tensorboard --logdir release_mode                                                    
```

<!-- ---------------------------------------------- -->
## Contact
If you have any questions or suggestions about this paper, feel free to contact me (zengyh7@mail2.sysu.edu.cn).

</details>