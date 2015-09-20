[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)


Code

    from __future__ import print_function
    
    import thinkstats2
    import thinkplot
    
    import math
    import random
    import numpy as np
    
    from scipy import stats
    from estimation import RMSE, MeanError
    
    def SimulateSample(lam=2, n=10, m=1000):
        """Sampling distribution of L as an estimator of exponential parameter.
    
        lam: parameter of an exponential distribution
        n: sample size
        m: number of iterations
        """
        def VertLine(x, y=1):
            thinkplot.Plot([x, x], [0, y], color='0.8', linewidth=3)
    
        estimates = []
        for j in range(m):
            xs = np.random.exponential(1.0/lam, n)
            lamhat = 1.0 / np.mean(xs)
            estimates.append(lamhat)
    
        stderr = RMSE(estimates, lam)
        print('standard error', stderr)
    
        cdf = thinkstats2.Cdf(estimates)
        ci = cdf.Percentile(5), cdf.Percentile(95)
        print('confidence interval', ci)
        VertLine(ci[0])
        VertLine(ci[1])
    
        # plot the CDF
        thinkplot.Cdf(cdf)
        thinkplot.Save(root='estimation2',
                       xlabel='estimate',
                       ylabel='CDF',
                       title='Sampling distribution')
    
        return stderr
    
    SimulateSample(n=10)
    SimulateSample(n=100)
    SimulateSample(n=1000)

Results

n = 10

standard error 0.85768408612

confidence interval (1.2880686136508015, 3.8569911842460094)

n = 100

standard error 0.201805860651

confidence interval (1.7241744737850309, 2.3914354131441189)

n = 1000

standard error 0.0628659708589

confidence interval (1.9002097617881133, 2.1046672921944518)
