[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

The problem wants to find if there is a difference between the first born and all other born children relative to the variability within the groups.

The Cohen's D when comparing first born to all other babies is "-0.0886729270726" which is relatively small which suggest there is not a significatn difference between when a baby is born in relation to their siblings.

Cohen's D was calculated by taking the difference between the means of the first born and all other born childen and dividing it by the pooled standard deviation.

Code

    def WeightDifference(live, firsts, others):
        """Explore the difference in weight between first babies and others.
    
        live: DataFrame of all live births
        firsts: DataFrame of first babies
        others: DataFrame of others
        """
        mean0 = live.totalwgt_lb.mean()
        mean1 = firsts.totalwgt_lb.mean()
        mean2 = others.totalwgt_lb.mean()
    
        var1 = firsts.totalwgt_lb.var()
        var2 = others.totalwgt_lb.var()
    
        print('Mean')
        print('First babies', mean1)
        print('Others', mean2)
    
        print('Variance')
        print('First babies', var1)
        print('Others', var2)
    
        print('Difference in lbs', mean1 - mean2)
        print('Difference in oz', (mean1 - mean2) * 16)
    
        print('Difference relative to mean (%age points)', 
              (mean1 - mean2) / mean0 * 100)
    
        d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
        print('Cohen d', d)
