from unittest import result
import numpy as np
import cv2
import random
import math




def get_gray(image_path):
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    # 顺便归一化处理一下，效果会不会更好
    # result = np.zeros(image.shape, dtype=np.float32)
    # cv2.normalize(image, result, alpha=0, beta=1, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_32F)
    # image = np.uint8(result*255.0)
    cv2.imwrite(image_path.replace('.', '_gray.'), image)




def random_noise(image_path,noise_num):
    '''
    添加随机噪点（实际上就是随机在图像上将像素点的灰度值变为255即白色）
    :param image: 需要加噪的图片
    :param noise_num: 添加的噪音点数目，一般是上千级别的
    :return: img_noise
    '''
    #
    # 参数image：，noise_num：
    img = cv2.imread(image_path)
    img_noise = img
    # cv2.imshow("src", img)
    rows, cols, chn = img_noise.shape
    # 加噪声
    for i in range(noise_num):
        x = np.random.randint(0, rows)#随机生成指定范围的整数
        y = np.random.randint(0, cols)
        img_noise[x, y, :] = 255
    
    cv2.imwrite(image_path.replace('.', '_random.'), img_noise)
    return img_noise

# img_noise = random_noise(ImagePath,frequency00)
# cv2.imshow('random_noise',img_noise)
# cv2.waitKey(0)

def sp_noise(image_path,prob):
    '''
    椒盐噪声(salt-and-pepper noise)是指两种噪声，一种是盐噪声（salt noise），
    另一种是胡椒噪声（pepper noise）。盐=白色(0)，椒=黑色(255)。前者是高灰度噪声，后者属于低灰度噪声。
    一般两种噪声同时出现，呈现在图像上就是黑白杂点

    以下使用的是一个阈值（prob、thres）进行的噪声分布，也可以用其他方法进行
    添加椒盐噪声
    image:原始图片
    prob:噪声比例
    '''
    image = cv2.imread(image_path)
    output = np.zeros(image.shape,np.uint8)
    noise_out = np.zeros(image.shape,np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()#随机生成0-1之间的数字
            if rdn < prob:#如果生成的随机数小于噪声比例则将该像素点添加黑点，即椒噪声
                output[i][j] = 0
                noise_out[i][j] = 0
            elif rdn > thres:#如果生成的随机数大于（1-噪声比例）则将该像素点添加白点，即盐噪声
                output[i][j] = 255
                noise_out[i][j] = 255
            else:
                output[i][j] = image[i][j]#其他情况像素点不变
                noise_out[i][j] = 100
    result = [noise_out,output]#返回椒盐噪声和加噪图像
    cv2.imwrite(image_path.replace('.', '_sp.'), output)
    return result

# sp_noise,img_noise = sp_noise(ImagePath,0.1)
# cv2.imshow('sp_noise',sp_noise)
# cv2.imshow('sp_noise_img',img_noise)
# cv2.waitKey(0)

# 高斯噪声(Gaussian noise)是指它的概率密度函数服从高斯分布的一类噪声。如果一个噪声，它的幅度分布服从高斯分布，
# 而它的功率谱密度又是均匀分布的，则称它为高斯白噪声。
# 注意：“高斯白噪声的幅度服从高斯分布”的说法是错误的，高斯噪声的幅度服从瑞利分布。
# 即使是一维的高斯白噪声，其幅度也不会服从高斯分布，而应该服从瑞利分布。
# 二维不相关的复高斯白噪声包络服从指数分布（x2分布的自由度为2的特例）。
# n个不相关的复高斯白噪声序列叠加后的复信号包络服从自由度为2n的x2分 布。
# 必须区分高斯噪声和白噪声两个不同的概念。高斯噪声是指噪声的概率密度函数服从高斯分布，白噪声是指噪声的任意两个采样样本之间不相关，两者描述的角度不同。白噪声不必服从高斯分布，高斯分布的噪声不一定是白噪声。当然，实际系统中的热噪声是我们一般所说的白噪声的主要来源，它是服从高斯分布的，但一般具有有限的带宽，即常说的窄带白噪声，严格意义上它不是白噪声。
def gaussian_noise(image_path, mean=0, var=0.001):
    ''' 
        添加高斯噪声
        image:原始图像
        mean : 均值 
        var : 方差,越大，噪声越大
    '''
    image = cv2.imread(image_path)
    image = np.array(image/255, dtype=float)#将原始图像的像素值进行归一化，除以255使得像素值在0-1之间
    noise = np.random.normal(mean, var ** 0.5, image.shape)#创建一个均值为mean，方差为var呈高斯分布的图像矩阵
    out = image + noise#将噪声和原始图像进行相加得到加噪后的图像
    # if out.min() < 0:
    #     low_clip = -1.
    # else:
    #     low_clip = 0.
    out = np.clip(out, 0.0, 1.0)#clip函数将元素的大小限制在了0和1之间了，小于的用low_clip代替，大于1的用1代替
    out = np.uint8(out*255)#解除归一化，乘以255将加噪后的图像的像素值恢复
    #cv.imshow("gasuss", out)
    noise = noise*255
    cv2.imwrite(image_path.replace('.', '_gaussian.'), out)
    return [noise,out]

# noise,out = gasuss_noise(ImagePath, mean=0, var=0.003)
# cv2.imshow('noise',noise)
# cv2.imshow('out',out)
# cv2.waitKey(0)

# 一幅图像的周期噪声是在图像获取期间由电力或机电干扰产生的
# 周期噪声可以通过频率域滤波进行显著在减少
# 一般的交流电噪声为60hz
def cycle_noise(image_path, frequency=60):
    '''
    添加周期噪声
    image:原始图片
    frequency:周期噪声的频率
    '''
    image = cv2.imread(image_path)
    noise = np.zeros(image.shape, np.uint8)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            noise[i][j] = noise[i][j] + frequency*math.sin(frequency*i) + frequency*math.sin(frequency*j)
            
    output = image + noise
    cv2.imwrite(image_path.replace('.', '_cycle.'), output)
    return noise, output


def make_image(image_path):
    get_gray(image_path)
    image_path = image_path.replace('.', '_gray.')
    random_noise(image_path, 3000)
    sp_noise(image_path, 0.01)
    gaussian_noise(image_path, mean=0, var=0.01)
    cycle_noise(image_path, 10)
    image_path = image_path.replace('.', '_cycle.')
    random_noise(image_path, 3000)
    sp_noise(image_path, 0.01)
    gaussian_noise(image_path, mean=0, var=0.01)
    
if __name__=="__main__":
    noise, output = cycle_noise("Lenna_gray.png", 10)
    cv2.imwrite("noise.png", noise)
    # ImagePaths = ["Lenna.png", "Cat.jpg"]
    # for ImagePath in ImagePaths:
    #     make_image(ImagePath)
