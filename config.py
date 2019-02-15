#window_width = 20.5 * 2
#window_width = 15.39

#grid_steps = 257
#grid_steps = 513
#grid_steps = 1025
#grid_steps = 2049

#grid_steps = 513; window_width = 513 * .03  # 15.39
grid_steps = 641; window_width = 641 * .025  # 16.025
#grid_steps = 769; window_width = 769 * .02  # 15.38

#xi_step_size = .04
#xi_step_size = .02
#xi_step_size = .01
xi_step_size = .005
#xi_step_size = .002
#xi_step_size = .001
xi_steps = int(3000 // xi_step_size)

diagnostics_each_N_steps = int(1 / xi_step_size)
#diagnostics_each_N_steps = int(.1 / xi_step_size)

field_solver_subtraction_trick = 1

reflect_padding_steps = 5
plasma_padding_steps = 10
plasma_coarseness, plasma_fineness = 3, 2


from numpy import cos, exp, pi, sqrt

def beam(xi_i, x, y):
    xi = -xi_i * xi_step_size
    #COMPRESS, BOOST, SIGMA, SHIFT = 3, 3, 1, 0  # harsh
    #COMPRESS, BOOST, SIGMA, SHIFT = 1, 3, 1, 0  # profound. implies fixed virtplasma boundary
    COMPRESS, BOOST, SIGMA, SHIFT = 1, 1, 1, 0
    if xi < -2 * sqrt(2 * pi) / COMPRESS:
        return 0
    r = sqrt(x**2 + (y - SHIFT)**2)
    return (.05 * BOOST * exp(-.5 * (r / SIGMA)**2) *
            (1 - cos(xi * COMPRESS * sqrt(pi / 2))))

