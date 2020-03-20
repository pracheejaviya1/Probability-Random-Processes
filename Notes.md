## Random Variables and Density functions 
---

*Random variables*
- Bernaulli
- Binomial
- Poission
- Gaussian

*CDF (Cumulative Distribution Function)*

* Used to represent continuous random variables and it is probability $\therefore$ CDF cannot be > than 1.

$$F_{X}(x)=Pr(X \leq x)$$

* $F_{X}({- \infty})= 0$ and $F_{X}({\infty})=1$
*  x1 < x2 , $F_{X}(x_{1}) \leq F_{X}(x_{2})$
* For $x_{1}<x_{2}$, $Pr(x_{1}<X \leq x_{2})= F_{X}     (x_{1})- F_{X}(x_{2})$ 

 **A random variable cannot take on negative values.**

The random variable takes on values in the range [ 0, 1 ) with equal probability.

* CDF can have discontinuities (Mixed random variable)

---

*PDF (Probability density function)*

* Probability that a random variable lies in an infinitesimal interval about the point X=x.

* $f_{X}(x)=\frac{dF_{X}(x)}{dx}$

* $f_{X}(x) \geq 0$
* $F_{X}(x)=\int_{-\infty}^{x} f_{X}(y)dy$
* Area from $-\infty$ to $\infty$ =1

---
Gaussian Random Variable(normal RV)

PDF of Gaussian RV :

 $$ f_{X}(x)= \frac{1}{\sqrt{2\pi\sigma^2}}exp(-\frac{(x-m)^2}{2\sigma^2})$$

** m is mean and $\sigma$ is standard deviation**
when m=0 and $\sigma$=1 , it is called standard normal random variable.

### CDF of Gaussian RV

  $$F_{X}(x)=\int_{-\infty}^{x}\frac{1}{\sqrt{2\pi\sigma^2}}exp(-\frac{(y-m)^2}{2\sigma^2})dy$$

To calculate the above, it has to be converted into a standard form : Q function or  $\phi$ function. 

$$Pr(X \leq x) = \int_{\frac{x-m}{\sigma}}^{\infty} \frac{1}{\sqrt{2\pi}}exp(-\frac{t^2}{2})dt$$

$$=Q(\frac{x-m}{\sigma})$$
---
### Conditional distribution

A random variable X conditioned on event A having occurred :
$$F_{X|A}(x)=Pr(X \leq x |A)$$

**Properties simillar to CDF**

### Expectation of RV

$$E[X]=\int_{-\infty}^{\infty}x f_{X}(x)dx$$

Average,mean,expectation,first moment are the same thing

### Expected values of functions of RV:
Replace x with the function:

$$E[g(x)]=\int_{-\infty}^{\infty}g(x) f_{X}(x)dx$$

For discrete RV, it becomes :

$$E[g(x)]=\Sigma_{k} g(x_{k})P_{X}(x_{k})$$

![](table.PNG)

*For $n^{th}$ moment, the x in integral changes to $x^n$*

- The zeroth moment is simply the area under the PDF and must be one for any random variable. 
-  The second moment is the mean-squared value

---
#### Central Moments
Used to get accurate output when the signal is fluctuated by minor noise. Because of the same, randomness of signal cannot be characterized.

$n^{th}$ central moment of a RV X :

$$E[(X-\mu_{X}^{n})]=\int (x-\mu_{X})^n f_{X}(x)dx $$

- With central moments, the mean is subtracted from the variable before the moment is taken in order to remove the bias in the higher moments due to the mean.
-  the first central moment is $E[(X-\mu_{X})]=E[X]-\mu_{X}=0$. 

Second central moment is hence the lowest central moment.(Variance)


$$\sigma_{X}^{2}=E[(X-\mu_{X})^2]=E[X^{2}-\mu_{X}^{2}]$$


Standard Deviation:
$ \sigma_{X}=\sqrt{E[(X-\mu_{X})^2]}$

Variance and the standard deviation serve as a measure of the width of the PDF of a random variable.

*The third central moment is known as the skewness and is a measure of the symmetry of the PDF about the mean.* 

*The fourth central moment is called the kurtosis and is a measure of the peakedness of a random variable near
the mean.*
