[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

The distribution is indeed uniform as demonstrated by the nearly straight line generated from the CDF

  
  import thinkstats2
  import thinkplot
  import random
  
  random_sample = [random.random() for i in range(1000)] #page 61
  pmf = thinkstats2.pmf(random_sample)
  thinkplot.pmf(pmf)
  thinkplot.show(xlabel = 'random number', ylabel = 'PMF')
  
  cdf = thinkstats2.cdf(random_sample)
  thinkplot.cdf(cdf)
  thinkplot.show(xlabel='random number', ylabel='CDF')
