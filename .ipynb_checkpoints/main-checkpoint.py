"""does stuff"""
from sympy import Expr, Symbol, pretty_print, symbols, Rational, I, Mod


def mat_print(fun: Expr, size: int = 4) -> None:
    """ prints stuff """
    x: Symbol = symbols('x')
    pretty_print([fun.subs(x, i) for i in range(size)])


def cell_print(fun: Expr, length: int = 80) -> None:
    """ prints divider """
    print(fun)
    pretty_print(fun)
    print("="*length)


def reduce_mod_4() -> None:
    """ reduces mod 4 """
    x: Symbol = symbols('x')
    m: list[Expr] = [Expr()]*100
    f: list[Expr] = [Expr()]*100

    m[0] = (1-(-1)**x)/2
    f[0] = (x - m[0])/2
    cell_print(m[0])

    m[1] = (1-(-1)**f[0]) + m[0]
    f[1] = (x - m[1])/2
    cell_print(m[1])

    # prove via induction that g = h
    # g is a term of m[1]
    g: Expr = (-1)**((-1)**x/4 + x/2 - Rational(1/4))
    mat_print(g)

    h: Expr = (-1)**((x**2 + x)/2)
    h = h.replace(x, x-1)
    h = h.expand()
    mat_print(h)
    cell_print(h)
    # end induction proof

    # begin h reduction
    htemp1: Expr = (-1)**((x**2)/2)
    htemp2: Expr = m[0]*I + m[0].replace(x, x+1).simplify()
    mat_print(htemp1)
    mat_print(htemp2)

    cell_print(h)
    mat_print(h)
    h = h.replace(htemp1, htemp2)
    h = h.expand()
    h = h.replace((-1)**(x/2), I**x)
    h = h.replace((-1)**(0-x/2), I**(0-x))  # 0 - makes mypy happy
    h = h.expand()
    h = h.subs(I*I**x, I**(x+1))
    h = h.subs(I*I**(0-x), I**(0-x+1))
    mat_print(h)
    cell_print(h)
    # h reduction complete

    # introduce reduced term
    mat_print(m[1])
    m[1] = m[1].replace(g, h)
    mat_print(m[1])

    # normalize
    m[1] = m[1].replace(I**(0-x), I**(3*x))
    m[1] = m[1].replace((-1)**x, I**(2*x))
    m[1] = m[1].replace(I**(1-x), I**(3*x+1))
    cell_print(m[1])


def gen_sum(size: int, num: int) -> Expr:
    """ generates then mods """
    x: Symbol = symbols('x')
    return sum(Mod(num*(-2)**i, 2**size)*x**i for i in range(size))


def mod_gen():
    """ generates and then does a mod """
    f = gen_sum(1, 1)
    pretty_print(f)


if __name__ == '__main__':
    # reduce_mod_4()
    mod_gen()
