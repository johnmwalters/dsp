[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

First I converted the height range to cm
5 Feet 10 inches = 177.8 cm 
6 feet 1 inch = 185.42 cm

Approximately 34.27% of men are eligable to join Blue Man Group

    import scipy.stats
    
    mu = 178
    sigma = 7.7
    dist = scipy.stats.norm(loc = mu, scale = sigma)
    
    bottom = dist.cdf(177.8)
    top = dist.cdf(185.4)
    
    percent_eligable = (top - bottom) * 100
    
    print percent_eligable
