"""does stuff"""
from sympy import symbols, Symbol, pretty_print, Expr, Rational, I

if __name__ == '__main__':
    x: Symbol = symbols('x')
    a: Symbol = symbols('alpha:100')
    b: Symbol = symbols('beta:100')
    m: list[Expr] = [None]*100
    f: list[Expr] = [None]*100

    m[0] = (1-(-1)**x)/2
    f[0] = (x - m[0])/2
    m[1] = (1-(-1)**f[0])/2
    f[1] = (x - m[1])/2

#     current: Expr = m[1].replace(
#             (-1)**((-1)**x/4 + x/2 - 1/4),
#             (-1)**((-1)**x/4 + x/2)/(a[2]+b[2]))
    current = m[1]

    z = 1/4**Rational(1/2)+I/4**Rational(1/2)
    current = current.replace(
        (-1)**((-1)**x/4 + x/2 - 1/4),
        z**(-1)**x * (I**x) * z
    ).replace(
        (1/2 + I/2)**((-1)**x),
        (Rational(1/2) + I*(-1)**x/2)
    ).expand().subs(
        I*I**x, I**(x+1)
    ).replace(
        (-1)**x,
        I**(2*x)
    ).subs({
        I**(2*x)*I**(x+1): I**(-x+1),
        I**(3*x): I**(-x),
    })

    current = (current * 4*I).expand()

    z = (((-1)**(x+1)-1)/2 + I*((-1)**(x)-1)/2)
    g = (((((
                            ((((((-1)**((x**2 + x)/2)).subs(x, x+1) + 1) / 2).expand()*2-1)*(-1))
                            .subs((-1)**(x**2/2), z)
                            .expand()
                            .subs({
                                (-1)**(5*x/2): I**x,
                                (-1)**(3*x/2): I**(3*x),
                                I*I**x: I**(x+1),
                            })
                            .subs({
                                I**(2*x)*I**(x+1): I**(3*x+1)
                            })*2)
                        .factor()/(-1 - I))
                .expand()
                .subs({
                    I*I**x: I**(x+1),
                    I**(3*x): I**(-x)
                })*(-1))
            .expand()
            .subs({
                I*I**x: I**(x+1),
            })
            .factor()/I)
        .expand()
        .subs({
            I*I**(-x): I**(1-x),
        }))
    pretty_print(g)
    # pretty_print([g.subs(x, n).expand() for n in range(4)])
