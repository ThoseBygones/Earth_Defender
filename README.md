# Earth_Defender

Developed using Python + Pygame

Language: Python

## 说明

- Python 小游戏《地球保卫者》，游戏方式类似于小时候玩过的街机游戏《雷霆战机》。
- 编程语言：Python 3.6
- 使用 Python 中的 Pygame 编写。
- 项目基础（代码和框架等）来自于人民邮电出版社**《Python编程从入门到实践》**书中第二部分的项目1 “外星人入侵”（第12章 ~ 第14章）。代码有部分改动，游戏功能也有一定的改动。

## 版本及更新

- #### 2.1版本已更新

  > + 增加了游戏的暂停功能，暂停后能恢复之前的游戏状态。
  > + 在暂停界面添加了“继续游戏”的按钮。
  
- #### 2.0版本已更新

  > + 添加了太空图片作为游戏背景。
  > + 修改部分游戏机制：
  >   + 取消了外星人的行列编组，改为按照一定频率在屏幕顶部随机位置出现；
  >   + 修改了外星人的移动方式，取消横向移动，改为垂直向下移动；
  >   + 修改了外星人碰到屏幕底部的判定，外星人碰到屏幕底部以后玩家的飞船数不会减少。
  > + 修改了得分面板文字的显示，英文改为中文且修改了字体和字体大小。
  > + 修改了 “开始游戏” 按钮的背景颜色、字体、字体大小和字体颜色。
  > + 更换了外星人的图片和玩家飞船的图片。

- #### 1.0版本已发布

  > - 大部分代码按照书中所给代码编写，仅有部分改动。
  > - 在得分板部分增加了 "High Score", "Score", "Level" 等文字说明。
  > - 修改了部分游戏参数，例如子弹的大小、子弹飞行速度、游戏得分计算方式等。

## 程序展示

- #### 游戏开始前的主界面

  ![](https://github.com/ThoseBygones/Earth_Defender/raw/master/images/img01.jpg)

- #### 游戏进行中的界面

  ![](https://github.com/ThoseBygones/Earth_Defender/raw/master/images/img02.jpg)
  
- #### 游戏暂停时的界面

  ![](https://github.com/ThoseBygones/Earth_Defender/raw/master/images/img03.jpg)