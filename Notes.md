## Random Variables and Density functions 
---

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


 