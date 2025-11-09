
当前模板已经预置了丰富的pytorch学习代码，非常适合pytorch入门学习！
***
拉取代码后需要在终端安装一些库，可按Ctrl+ ` 来调出终端，在终端中输入以下命令
*安装torch库  
``pip install torch touchvision torchaudio -i https://pypi.tuna.tsinghua.edu.cn/simple``
*安装scipy库  
``pip install scipy -i https://pypi.tuna.tsinghua.edu.cn/simple``
*安装open-cv库  
 ``pip install opencv-python -i https://pypi.tuna.tsinghua.edu.cn/simple``
 
 ***

 **关于部分文件夹需要修改的内容（根据安装的实际路径来决定）**

 datasets文件夹是数据集和标注集存放的地方

test是测试集，用于最终评估模型性能。它是一个完全独立、未被模型训练和超参数调整过程接触过的数据集。使用测试集评估的目的是为了获得模型在真实世界新数据上的泛化能力（Generalization Ability）的无偏估计，占 10%-20%

验证集用于调整模型的超参数（Hyperparameters）和进行早期停止 (Early Stopping)。它在训练过程中扮演着“模拟考试”的角色，帮助我们评估模型在未见过的数据上的表现，并根据表现调整模型结构或训练策略，而不是直接修改模型参数，占 10%-20%。

训练集是用于训练模型的核心数据。模型通过学习训练集中的数据模式、特征与标签之间的关系来调整其内部参数（如神经网络中的权重和偏置），占 60%-80%。

images放置原图，labels放置标签
注：图像命名和标命名要一一对应
![Alt text](image-2.png)

datasets文件夹的data.yaml是配置相关路径的地方
![Alt text](image-3.png)
***