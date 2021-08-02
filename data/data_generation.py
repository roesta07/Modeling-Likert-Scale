import pandas as pd
import numpy as np
import scipy.stats as stats

from scipy.special import expit,logit,softmax
import pymc3 as pm
import arviz as az


#helper function
def normalize(array):
  return array/np.sum(array)

def cut_points(p):
  cum_p=np.cumsum(p)
  log_odds_cum_p=logit(cum_p[:-1]) ## not need to do it for the last
  return log_odds_cum_p ## for 6 you get one fro free as we know last one will be 1

def generate_cutpoints(n_samples):
  initial_cutpoints=np.zeros((n_samples,6))
  for i in range(n_samples):
    initial_dist=np.array([1,3,5,7,6,5,4]) # this when dep A is 0
    p_dist_norm=normalize(initial_dist)
    initial_cutpoints[i]=cut_points(p_dist_norm)
  return initial_cutpoints

def ordered_logistic_proba(a):
  p_dist_cum=expit(a)
  p_dist_cum=np.concatenate(([0.0],p_dist_cum,[1.0]))
  p_dist=p_dist_cum[1:]-p_dist_cum[:-1]
  return p_dist


def generate_data(n_samples=None,to_df=True):
  scales=[]
  bA=-2 ## our pressumed parameters
  depart=stats.multinomial(1,[0.5,0.5]).rvs(n_samples) # Split detart
  initial_cutpoints=generate_cutpoints(n_samples)
  for dep,cutpoint in zip(depart,initial_cutpoints):

    phi=bA*dep[0]
    
    p_dist_ods=cutpoint-phi
    #print(f'dep:{dep[0]},phi:{phi},p_distods{p_dist_ods}')
    p_dist=ordered_logistic_proba(p_dist_ods)
    scale=stats.multinomial(1,p_dist).rvs()
    scales.append(np.where(scale==1)[1][0])
  scales=np.array(scales)
  if to_df==True:
    df=pd.DataFrame(depart,columns=['depA','other_dep'])
    df['ratings']=scales
    return df
  else:
    return scales

if __name__=="__main__":
    df=df=generate_data(800)
    df.to_csv('data_likert.csv',index=None)