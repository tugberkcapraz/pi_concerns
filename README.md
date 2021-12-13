# Modelling Concerns About Personal Information with Structural Equation Modelling

This repository contains the underlying code for my analysis that I shared on medium.com [post](LINK HERE).

## Contents of this Repository
1) [The jupyter notebook](https://github.com/tugberkcapraz/pi_concerns/blob/main/Post.ipynb) contains the code and
explanations of my design choices. 
2) [Europinions.pdf](https://github.com/tugberkcapraz/pi_concerns/blob/main/europinions.pdf) is the file that you can 
find the survey report and the questionnaire that I used in this project. As
you see in the notebook, the variable naming convention of the market research company who conducted this survey is
really vague and _it is almost impossible to work without referring to this document._
3) [plots](https://github.com/tugberkcapraz/pi_concerns/tree/main/plots) is the directory where I saved the plots for further use.
4) **[sem_report](https://github.com/tugberkcapraz/pi_concerns/tree/main/sem_report)** is the report that is automatically
created by semopy package. 

## Research Questions
In this analysis
I tried to approach the matter from three different levels, respectively, _micro_, _interaction_ and _macro_ levels. Each level
has it's own unique research question.

**First** question concerning the _micro_ level is whether _personality traits_ have any
impact on concerns about personal information. 

The **second** question in on _macro_ level. What I question is if trust in political institutions
have any impact on concerns about personal information. 

And **lastly**, what in what I call the _interaction_ level, I question
if impact of personality traits on the dependent variable is being moderated by trust in political institutions or not.

## Methodology
The variables that I mentioned above are not directly measured in the survey. They are estimated as latent constructs by
several distinct sub-items. For this reason, I chose structural equation modelling as it provides necessary flexibility
working with several latent constructs. 

The structural equation modelling part is carried out with **semopy** package. For the visualisations, I used two distinct
packages, **matplotlib** and **plotnine**. Data pre-processing operations are handled with **pandas** package.

For Further explanations please refer to the notebook.

## Notes:

I don't provide the dataset here for **two** reasons. 
1) The data is in .dta (Stata format) format and it is over 100 mb. Github complains about it. Even though there are ways
to bypass this I don't think it makes sense to upload that big file here.
2) I downloaded the data from [GESIS](LINK HERE) archive and anyone who creates a free account on their website can access
the files just like I did. They want to know which accounts download their data for what purposes and I respect their decision.
So you can follow the link and download the data by yourself. 

