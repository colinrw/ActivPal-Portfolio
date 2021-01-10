# Data Cleaning

#### Introduction

Since CBS provided us already cleaned data, it was not possible to do a lot of data cleaning for this project. 

<details><summary>Fixing timestamps</summary>

One of the issues with the data provided by CBS was the timestamps were not converted to readable and useful times yet. 

Example of the unconverted timestamp. The 2 long integers should be together and converted to a readable timestamp.

|Before Convertion|After Convertion|
|------|------|
|![](../Images/Data%20Preprocessing/timestamp_issue.png)| ![](../Images/Data%20Preprocessing/timestamp_fixed.PNG) |

The following function has been used to convert the unreadable timestamps.

![](../Images/Data%20Preprocessing/timestamp_function.PNG)

</details>

---

<details><summary>Switching Diceface</summary>

A Diceface is the direction the activPAL is facing. The issue we are facing is when a respondent flips from its front to the back, the measured X, Y and Z values also flip sides. To solve this, we changed to X, Y and Z values according the switch in diceface value. 

Example of the diceface directions [found here](http://docs.palt.com/display/AL/MORA):
![](../Images/Data%20Preprocessing/diceface-directions.PNG)

The following images were provided by Brian Keijzer and has been used to determine how to flip the dicefaces. 

|Diceface Physical |Diceface Numerical|
|------|------|
|![](../Images/Data%20Preprocessing/diceface-physical.jpg)| ![](../Images/Data%20Preprocessing/diceface-numerical.jpg) |

Here is an example how this transformation has been done in code. We used diceface `1` as a baseline to convert to. These convertion functions are written by Adnan and me.

![](../Images/Data%20Preprocessing/diceface-function.PNG)

*During the MET model creation the feature `sum of magnitude of acceleration (sum_mag_acc)` was used, this feature adds the X, Y and Z values together. Therefore, the diceface convertion was not needed in the end.*

The entire notebook can be found [here](../Images/Data%20Preprocessing/Code/normalize_diceface_values-v3.py).

</details>

---

[<  Data Exploration](data_exploration.md) — [Data Preparation >](data_preparation.md) 