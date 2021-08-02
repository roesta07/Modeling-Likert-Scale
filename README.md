

## Introduction
Every now and then; researchers have to use Likert scale for measuring some variables because not all variables can be measured through engineering devices.For Example lets consider variable 'Happiness'. How can we measure Happiness? There is no reliable psychiyatric devices that can measure somebody's happiness.Even though no pshchyatric diagnosis are reliable one way to attempt measuring happiness is to use likert scale which is just asking the participants from some number range let say 1-3; how happy are you? But these numbers cannot be interpreted as numbers from normal number scales we had witnessed. Indeed these numbers are defined by us and remains in the boundry defined by us i.e every other numbers are squeezed and limited into these scale. For Example Even though I fell immensly happy today I cannot say 100; i have to choose 3. 
One other thing we know about these variable is that its not categories as $3>2>1$. It means that it preserves monotonic assumption i.e I am happier than people who select 1 and 2 if I had selected 3. With these challenges and problems someone already came up with methods to model such variables.

# How satisfied are you?:
Dataset contains a likert scale values collected on a different time-scale from each employees.The scales are from 1-7 and you as a Manager want to know that
### Hypothesis
>how satisfied are your employees compared to other departments?

## Cummulative log odds and GLM
One of the complexities arises when trying to identify distances between categories. These informations are stored as the ferequecies in the data. And as these variables maintain monotonic assumptions we take cummulative of such frequencies normalized.A cummulative log-odds are just the log of such frequencies. Why use Cummulative log-odds; because we can add linear model to it.

Mathematically;
$$\log(\frac{Pr(y_{i}<k)}{1-Pr(y_{i}<k})=\alpha_{k}-\phi_{i}$$
where,
$k$:1-7 for this problem<br>
$\alpha$: intercept for ordered-categories<br>
$\phi$ : Linear Model

## Model
$$R_{i} \sim ordered-logit(\phi_{i},k)$$


where,
$R_{i}$ be the observed ratings
$$\phi_{i}=\beta_{A} * Department_{A}$$
$$\beta_{A}=Normal(0,1)$$
$$k\sim Normal(0,1.5)$$
*Note the code to run this model can be found in this [notebook](https://github.com/roesta07/Modeling-Likert-Scale/blob/main/Likert_scale_notebook.ipynb).

After running the model we get
|  | mean|   sd  |hdi_3%     |hdi_97% |
|--:|--: |--:	 |--:        |--:     |
|$beta_{A}$   |-1.94    | 0.14   |2.21      | 0.-1.68  |

## What does this mean?
Now this can be explained with simple plot.
<div><img src="fig//result.png" width="820"  class="inline"> </div>
*fig: Change in satisfaction levels*

The plot (on the right) indicates is basically our predictions. In terms of ordered categories you not just get the distribution for a point but you get the distribution for whole vector i.e for all categories. Here the line represent the change in satisfaction level between department A and other, but an interesting thing to notice here is the distance between each categories for both cases. If you do not understand plot on the left then the plot on the right is the histogram representation of our predection 





