<div style="text-align: center; "><img src="https://github.com/Buelie/Kothonva/blob/main/image/IconOne.png"><img src="https://github.com/Buelie/Kothonva/blob/main/image/TitleS.png?raw=true"></div>

# English | [简体中文](https://github.com/Buelie/Kothonva/tree/main/zh-cn)
## 中文插话[欢迎大家来提交你的创意]

# Check for updates within KOOK

***If you are a KOOK user (note that this method only works with KOOK), you can invite the KOOK bot: [GitHub HOOK]() to view the repository update, note that before that, you need to enter the following command to bind:***
```
g.bind Buelie/Kothonva
```
***As for Discord users, we will soon develop related bots (or adaptations & bindings), KOOK bots are developed by users with the username: 小夜#8801, see [BotMarket](https://www.botmarket.cn/bots?id=100) for bot details***

# What is Kothonva?
***Kothonva is based on Python, and our approved compilers are limited to Python or C/C++. Kothonva is a lightweight language that is simple and easy to use, and the syntax retains most of Python's original functions, but also adds a large number of new functions.***

## Features of Kothonva:
* [x] **Ability to run directly with Py**
* [x] **Fast running speed and compilation speed**
* [x] **Lightweight, small footprint or memory**
* [x] **The syntax is concise and clear**
* [x] **(Obsolete)It is used more like a language than a superset**

# documentation
***Under construction, maybe you can join our [KOOK community]() first***

| version | Write status | Estimated time to completion | remark | link |
| --- | --- | --- | --- | --- |
| 0.0.1 | Under construction (not started writing) | 2023/7/5 | not | not | 
| 0.0.2 | Under construction (not started writing) | 2023/12/6 | not | not |
| 0.0.3 | Under construction (not started writing) | 2024/7/12 | not | not |
| 0.0.4 | Under construction (not started writing) | 2024/12/26 | not | not |
| 0.0.5 | Under construction (not started writing) | 2025/7/10 | not | not |
| 0.0.6 | Under construction (not started writing) | 2025/12/2 | not | not |

# Installation method
* **Just because it's a Python project doesn't mean it's downloadable with the pip command!**
  * **You should use git or download and apply the main.py file globally**
    * **The following installation method will not work:**
    ```
    pip install Kothonva #one
    git clone https://github.com/Buelie/Kothonva #two
    ```
    * **Why doesn't it work?**
      * **1.The first one, because we didn't upload Kothonva to Pypi(Because the author encountered an error when uploading, it cannot be deleted, and it will be supported in the future, of course, you can also upload instead of the author, maybe the author will directly approve it)**
      * **Second, because our repository contains all the Kothonva versions(The author's hard drive storage is not enough, woo-woo)**

# Focus on to-dos
* Focus on to-dos
 * [ ] **The suffix name can be submitted to the question-suffix to submit your idea**
 * [ ] **Independent into a programming language**
 * [x] **Language compiler**

# contribute
***You can save your contribution to your own repository (you can create a pull request) and then create a merge request***

# Use on the IDE
***At present, we can only provide code completion function of IDE VSCode, if you want to use it in other IDEs, you can send a private message to the author (need to provide the name and details of the IDE, and the IDE needs to support the use of plugins), we will make plugins as soon as possible according to the needs.Oh, and the good news is that we will be implementing our compiler and IDE in 2023!!!***

# How Kothonva files are used in VSCode
***You just need to download the corresponding version of Kothonva and drag it into a folder, here's how to do it:***
+ ***To create a new folder in the production folder, it is recommended to mak:***

+ Folder structure:
```
  --src
   --Kothonva (This is a newly created folder to hold .py files)
    --main.py
   --Main.py
```
+ ***Next, enter the following command in the Main.py (i.e. production file) file:***
```python
import Kothonva.main
```
***Then, you can use it, and of course you can import it as follows (but we don't recommend it):***
```python
from Kothonva.main import *
```
