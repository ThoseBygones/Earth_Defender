# Earth_Defender

Developed using Python + Pygame 

Language: Python 3.7.3

## 项目说明

- Python 小游戏《地球保卫者》，游戏方式类似于小时候玩过的街机游戏《雷霆战机》。
- 编程语言：Python 3.7.3
- 使用 Python 中的 Pygame 编写，版本为 1.9.6 （请自行安装）。
- 项目基础（代码和框架等）来自于人民邮电出版社 **《Python编程从入门到实践》** 书中第二部分的项目1 “外星人入侵”（第12章 ~ 第14章）。代码和游戏功能都有大量的改动。

## 游戏说明

+ 运行程序后，屏幕中央会显示一个 “开始游戏” 的按钮，点击即可开始游戏。
+ 按下键盘的 “上”、“下”、“左”、“右” 键控制飞船的运动（可以按住不放以持续移动）。
+ 按下键盘的 “空格” 键发射飞船的子弹（按住不放不会连续发射子弹）。
+ 按下键盘的 “回车” 键暂停游戏；暂停游戏后屏幕中央会显示一个 “继续游戏” 的按钮，点击即可继续游戏。
+ 按下键盘的 “退出（Esc）” 键直接退出游戏。
+ 游戏开始时玩家有四艘飞船，其中一艘飞船处于战斗状态，另外三艘飞船处于待命状态。若玩家损失了所有的飞船，游戏结束，回到最开始的界面。
+ 外星人从屏幕顶端想屏幕底端飞行，飞行过程中会在水平方向上随机向左、向右移动或者不动（俗称鬼畜）。
+ 外星人从屏幕底部飞出后即消失（玩家不会损失飞船），但外星人如果与飞船发生碰撞则会损失一艘飞船。
+ 飞船发射的子弹碰到外星人后外星人会被消灭 （即外星人从屏幕上消失），同时玩家可以获得相应的分数。每消灭20艘飞船游戏等级会提升一级；游戏等级每提升一级，游戏速度会适当加快，同时玩家每消灭一个外星人会获得的分数也会适当增加；等级越高，玩家每消灭一个外星人获得的分数越高。

## 版本及更新

- #### 3.2版本已更新

  > + 增加了程序运行时的图片界面（即在 “开始游戏” 按钮后面加了一张背景图）。
  > + 设置了游戏窗口顶部导航栏的图标。

- #### 3.1版本已更新

  > + 修改了程序运行时游戏窗口弹出的位置，使其在计算机屏幕的正中间显示（由于游戏窗口蛮大的，有人反映弹出的游戏窗口的位置很尴尬，可能没有把游戏窗口在计算机屏幕上显示出来... 好吧事情真多。修改过的 3.1 版本的游戏窗口能在我的计算机屏幕【1366 * 768 的分辨率】的正中间显示。至于在你的计算机屏幕的什么位置显示，关我啥事哈哈哈 XD）。
  
- #### 3.0版本已更新

  > + 重要更新！更新了游戏的关键机制：
  >   + 增加了飞船移动自由度。现在飞船可以上下左右到处乱跑了（包括各种方向组合。当然，同时按下方向相反的按键时，飞船会选择不动 XD），但限制飞船不能移出屏幕范围（并且不能向上移动到显示游戏信息的部分）。
  >   + 增加了外星人的移动自由度。现在外星人也可以乱跑了（当然，是有限的乱跑），在保持不断向下移动的过程中，可能同时在水平方向随机向左向右移动（当然也可能不向左也不向右），但不会从左侧或者从右侧移出屏幕范围（运行的时候外星人的运动看起来很有鬼畜的感觉...）。
  > + 解决了游戏结束重开的时候等级没有恢复到 1 级的bug。
  > + 微调了飞船初始的移动速度，子弹初始飞行的速度和外星人出现的频率（稍稍增加了频率，游戏变难了有木有）。
  
- #### 2.2版本已更新

  > + 更换了游戏的背景图片，使游戏过程中的视觉效果体验更好。
  > + 更换了玩家飞船的图片，增加飞船与背景的对比度，使玩家更容易看清楚飞船的位置。
  > + 修改了子弹的颜色的尺寸，使玩家更容易看清楚子弹的位置。
  
- #### 2.1版本已更新

  > + 增加了游戏的暂停功能，暂停后能恢复之前的游戏状态。
  > + 在暂停界面添加了“继续游戏”的按钮。

- #### 2.0版本已更新

  > + 添加了太空图片作为游戏背景。
  > + 修改部分游戏机制：
  >   + 取消了外星人的行列编组，改为按照一定频率在屏幕顶部随机位置出现。
  >   + 修改了外星人的移动方式，取消横向移动，改为垂直向下移动。
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
  
- #### 飞船自由移动

  ![](https://github.com/ThoseBygones/Earth_Defender/raw/master/images/img04.jpg)