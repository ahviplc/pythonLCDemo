
## Data description

**4 Classes about car's condition:**
* unacc: unaccepted condition
* acc:  accepted condition
* good: good condition
* vgood: very good condition

**Features:**
* buying: vhigh, high, med, low.
* maint: vhigh, high, med, low.
* doors: 2, 3, 4, 5more.
* persons: 2, 4, more.
* lug_boot: small, med, big.
* safety: low, med, high.

## Training
**Files:**
* [data_processing.py](./data_processing.py) : download data and process to an accepted format
* [model.py](./model.py) : training model and view result

![Training result](./result.png)


## Dependencies
* Python
* tensorflow
* pandas
* numpy
* matplotlib

You can view more tutorials(教程) on [this page](https://morvanzhou.github.io/) or know more about me on [here](https://github.com/ahviplc/pythonLCDemo).

从头开始做一个汽车状态分类器1: 分析数据 - 机器学习实战 | 莫烦Python
https://morvanzhou.github.io/tutorials/machine-learning/ML-practice/build-car-classifier-from-scratch1/

从头开始做一个汽车状态分类器2: 搭建模型 - 机器学习实战 | 莫烦Python
https://morvanzhou.github.io/tutorials/machine-learning/ML-practice/build-car-classifier-from-scratch2/